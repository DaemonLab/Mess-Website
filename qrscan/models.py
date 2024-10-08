import uuid
from io import BytesIO
from PIL import Image
import qrcode

from django.core.files import File
from django.db import models

from home.models import Allocation, Student


class MessCard(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        help_text="This contains the unique id of the mess card"
    )
    allocation = models.ForeignKey(
        Allocation,
        on_delete=models.CASCADE,
        help_text="This contains the allocation details",
        null=True,
        blank=True
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        help_text="This contains the student details",
    )
    qr_code = models.ImageField(
        upload_to='qr_codes/',
        help_text="This contains the qr code image",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.allocation.student_id} - {self.allocation.email.email}"

    def generate_qr_code(self):
        data = str(self.id)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white").convert('RGB')

        try:
            logo = Image.open('./static/images/iiti_bw.png')
            logo = logo.resize((150, 150))
            pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
            img.paste(logo, pos)
        except FileNotFoundError:
            print("Logo file not found. Proceeding without logo.")
            

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        file_name = f"qr_{self.student.email}_{self.allocation.student_id}.png"

        self.qr_code.save(file_name, File(buffer), save=False)
        buffer.close()

    def save(self, *args, **kwargs):
        if not self.allocation:
            self.allocation = self.student.allocation_set.last()
        if not self.pk:
            super().save(*args, **kwargs)
        if not self.qr_code:
            self.generate_qr_code()
        super().save(*args, **kwargs)


class Meal(models.Model):
    mess_card = models.ForeignKey(
        MessCard,
        on_delete=models.CASCADE,
        help_text="This contains the mess card details",
        null=True,
        blank=True
    )
    date = models.DateField(
        help_text="This contains the date of the meal",
        auto_now_add=True
    )
    breakfast = models.BooleanField(
        help_text="This contains the breakfast status",
        default=False
    )
    lunch = models.BooleanField(
        help_text="This contains the lunch status",
        default=False
    )
    high_tea = models.BooleanField(
        help_text="This contains the high tea status",
        default=False
    )
    dinner = models.BooleanField(
        help_text="This contains the dinner status",
        default=False
    )

    class Meta:
        unique_together = ['mess_card', 'date']

    def __str__(self):
        return f"{self.mess_card.allocation.student_id} - {self.date}"


class MessTiming(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('high_tea', 'High Tea'),
        ('dinner', 'Dinner')
    ]

    meal_type = models.CharField(
        max_length=10,
        choices=MEAL_TYPES,
        help_text="This contains the meal type",
        unique=True,
    )
    start_time = models.TimeField(
        help_text="This contains the start time",
        null=True,
        blank=True
    )
    end_time = models.TimeField(
        help_text="This contains the end time",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.meal_type} Timings"
