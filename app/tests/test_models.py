import self as self
from app.models import Category, Branch, Contact, Course
from django.test import TestCase
from app import models


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='IT', img_path='some')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_img_path_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('img_path').verbose_name
        self.assertEquals(field_label, 'img path')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 1300)


class BranchModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Branch.objects.create(latitude='123', longitude='123', address='tryasina 229')

    def test_latitude(self):
        branch = Branch.objects.get(id=1)
        latitude = branch._meta.get_field('latitude').verbose_name
        self.assertEquals(latitude, 'latitude')

    def test_longitude(self):
        branch = Branch.objects.get(id=1)
        longitude = branch._meta.get_field('longitude').verbose_name
        self.assertEquals(longitude, 'longitude')

    def test_longitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('longitude').max_length
        self.assertEquals(max_length, 200)


class CourseTest(TestCase):

    def test_course_str(self):
        """Test the courses string representation"""

        course = models.Course.objects.create(
            name='Office systems',
            description='office systems',
            category=models.Category.objects.create(
                id=1
            ),
            logo='someLogo',
            contact=models.Contact.objects.create(
                id=1
            ),
            branch=models.Branch.objects.create(
                id=1
            )
        )
        self.assertEqual(str(course), course.name)
        self.assertEqual(course.description, course.description)
        self.assertEqual(course.logo, course.logo)
