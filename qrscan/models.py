from django.db import models
from home.models import Allocation, Student
import qrcode
from io import BytesIO
from django.core.files import File
import secrets
import json
from PIL import Image

def generate_secret_key():
    return secrets.token_hex(32)

class MessCard(models.Model):
    allocation = models.ForeignKey(Allocation, on_delete=models.CASCADE, help_text="This contains the allocation details", null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text="This contains the student details", null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', help_text="This contains the qr code image", blank=True, null=True)
    secret_key = models.CharField(max_length=64, help_text="This contains the secret key for each student",blank=True, null=True, default=generate_secret_key)

    def __str__(self):
        return f"{self.allocation.student_id} - {self.allocation.email.email}"

    def generate_qr_code(self):
        data = {
            "email": self.allocation.email.email,
            "secret_key": self.secret_key,
            "caterer": self.allocation.caterer.name
        }

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(json.dumps(data))
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white").convert('RGB')

        logo = Image.open('./static/images/iiti_bw.png')
        logo = logo.resize((150, 150))

        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos)

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        file_name = f"qr_{self.student.email}_{self.allocation.student_id}.png"

        self.qr_code.save(file_name, File(buffer), save=False)
        buffer.close()


    def save(self, *args, **kwargs):
        if not self.secret_key:
            self.secret_key = generate_secret_key()
        if self.allocation and not self.student:
            self.student = self.allocation.email
        if not self.qr_code:
            self.generate_qr_code()

        super().save(*args, **kwargs)


class Meal(models.Model):
    mess_card = models.ForeignKey(MessCard, on_delete=models.CASCADE, help_text="This contains the mess card details", null=True, blank=True)
    date = models.DateField(help_text="This contains the date of the meal", auto_now_add=True)
    breakfast = models.BooleanField(help_text="This contains the breakfast status", default=False)
    lunch = models.BooleanField(help_text="This contains the lunch status", default=False)
    dinner = models.BooleanField(help_text="This contains the dinner status", default=False)

    def __str__(self):
        return f"{self.mess_card.allocation.student_id} - {self.date}"

    def save(self, *args, **kwargs):
        if not self.mess_card:
            self.mess_card = MessCard.objects.get(allocation=self.mess_card.allocation)
        super().save(*args, **kwargs)
