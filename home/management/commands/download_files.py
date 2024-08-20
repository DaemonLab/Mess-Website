import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.core.management.base import BaseCommand
from home.models import LongRebate
from messWebsite.settings import CLOUDINARY_STORAGE, MEDIA_ROOT
import requests
import os
import mimetypes

def download_file(url, save_path):
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        # Check if the request was successful
        response.raise_for_status()

        content_type = response.headers.get('Content-Type')
        if content_type:
            extension = mimetypes.guess_extension(content_type)
            file_extension = extension if extension else '.bin'

        # Open the file in write-binary mode and write the content
        with open(f"{save_path}{file_extension}", 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"File downloaded successfully and saved to {save_path}")

        return file_extension

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

class Command(BaseCommand):
    help = 'Fetch Cloudinary image URLs for all entries in LongRebate'
    def handle(self, *args, **options):
        cloudinary.config(
            cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
            api_key=CLOUDINARY_STORAGE['API_KEY'],
            api_secret=CLOUDINARY_STORAGE['API_SECRET'],
        )

        for obj in LongRebate.objects.all():
            file_name = obj.file.name[len(str("media/documents/")):]
            try:
                url = cloudinary.CloudinaryResource(obj.file.url[len(str("/media/")) : ]).build_url()
                if url:
                    file_extension = download_file(url, os.path.join(MEDIA_ROOT, 'documents', file_name))
                    if file_extension:
                        obj.file.name = f"documents/{file_name}{file_extension}"
                        obj.save()
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error fetching URL for public ID {obj.file}: {e}'))

