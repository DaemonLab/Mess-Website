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

	def test_rejects_hostel_name_longer_than_five_characters(self):
		csv_content = (
			"Room No,Roll No,Name,Course,Department,Institute Email ID\n"
			"201,260003012,JANE DOE,B.Tech,ME,me260003012@iiti.ac.in\n"
		)
		upload = SimpleUploadedFile(
			"students.csv", csv_content.encode("utf-8"), content_type="text/csv"
		)

		response = self.client.post(
			reverse("admin:home_student_import_csv"),
			{"hostel": "ABCDE1", "csv_file": upload},
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(Student.objects.count(), 0)
		self.assertContains(response, "Hostel name is too long")

	def test_imports_tab_separated_file_with_bom(self):
		tsv_content = (
			"\ufeffRoom No\tRoll No\tName\tCourse\tDepartment\tInstitute Email ID\n"
			"203\t260003013\tTAB STUDENT\tB.Tech\tME\tme260003013@iiti.ac.in\n"
		)
		upload = SimpleUploadedFile(
			"students.csv", tsv_content.encode("utf-8"), content_type="text/csv"
		)

		response = self.client.post(
			reverse("admin:home_student_import_csv"),
			{"hostel": "AG", "csv_file": upload},
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(Student.objects.count(), 1)
		self.assertTrue(
			Student.objects.filter(email="me260003013@iiti.ac.in").exists()
		)

	def test_reports_missing_required_header(self):
		csv_content = (
			"Room No,Name,Course,Department,Institute Email ID\n"
			"201,NO ROLL,B.Tech,ME,no-roll@example.com\n"
		)
		upload = SimpleUploadedFile(
			"students.csv", csv_content.encode("utf-8"), content_type="text/csv"
		)

		response = self.client.post(
			reverse("admin:home_student_import_csv"),
			{"hostel": "AG", "csv_file": upload},
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(Student.objects.count(), 0)
		self.assertContains(response, "Missing required column: roll no.")

	def test_rejects_duplicates_within_file(self):
		csv_content = (
			"Room No,Roll No,Name,Course,Department,Institute Email ID\n"
			"201,260003014,ONE,B.Tech,ME,dup@example.com\n"
			"202,260003015,TWO,B.Tech,ME,dup@example.com\n"
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
		self.assertContains(response, "Duplicate email in the uploaded file.")

	def test_rejects_existing_email_case_insensitively(self):
		Student.objects.create(
			hostel="AG",
			room_no="200",
			roll_no="260003099",
			name="Existing",
			degree="B.Tech",
			department="ME",
			email="Case@Test.com",
		)

		csv_content = (
			"Room No,Roll No,Name,Course,Department,Institute Email ID\n"
			"201,260003016,NEW,B.Tech,ME,case@test.com\n"
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
		self.assertContains(response, "A student with this email already exists.")
