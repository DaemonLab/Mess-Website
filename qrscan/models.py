from django.db import models
from home.models import Allocation, Student
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
import secrets

def generate_secret_key():
        return secrets.token_hex(32)

class MessCard(models.Model):
    allocation = models.ForeignKey(Allocation, on_delete=models.CASCADE, help_text="This contains the allocation details", null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text="This contains the student details", null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', help_text="This contains the qr code image" ,blank=True, null=True)
    secret_key = models.CharField(max_length=64, blank=True, null=True, default=generate_secret_key)

    def __str__(self):
        return f"{self.allocation.student_id} - {self.allocation.email.email}"
    
    def generate_qr_code(self):
        data = {"email": self.allocation.email.email, "secret_key": self.secret_key, "caterer": self.allocation.caterer.name}
        qr = qrcode.make(data)

        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        file_name = f"qr_{self.student.email}_{self.allocation.student_id}.png"

        self.qr_code.save(file_name, File(buffer), save=False)
        buffer.close()

    def save(self, *args, **kwargs):
        if not self.secret_key:
            self.secret_key = generate_secret_key()
        self.student = self.allocation.email
        if not self.qr_code:
            self.generate_qr_code()
        super().save(*args, **kwargs)

