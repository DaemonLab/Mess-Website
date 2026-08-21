from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from home.models import Student


class StudentCsvImportTests(TestCase):
	def setUp(self):
		user = get_user_model().objects.create_superuser(
			username="admin",
			email="admin@example.com",
			password="test-password",
		)
		self.client.force_login(user)

	def test_imports_valid_rows_and_reports_invalid_rows(self):
		csv_content = (
			"S.No.,Unit No.,Room No,Roll No,Name,Course,Department,Institute Email ID\n"
			"1,A,201,260003011,JOHN DOE,B.Tech,ME,me260003011@iiti.ac.in\n"
			"2,B,202,,Missing Roll,B.Tech,ME,missing@example.com\n"
		)
		upload = SimpleUploadedFile(
			"students.csv", csv_content.encode("utf-8"), content_type="text/csv"
		)

		response = self.client.post(
			reverse("admin:home_student_import_csv"),
			{"hostel": "AG", "csv_file": upload},
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(Student.objects.count(), 1)
		student = Student.objects.get()
		self.assertEqual(student.hostel, "AG")
		self.assertEqual(student.roll_no, "260003011")
		self.assertContains(response, "Row")
		self.assertContains(response, "Missing value for: roll no.")
