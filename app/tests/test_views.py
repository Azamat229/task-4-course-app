from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from app.models import Category, Course, Contact, Branch
import json



class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(
            name='Office systems',
            description='office systems',
            category=Category.objects.create(
                id=1
            ),
            logo='someLogo',
            contact=Contact.objects.create(
                id=1
            ),
            branch=Branch.objects.create(
                id=1
            )
        )
        self.detail_url = reverse('detail', kwargs={'pk': self.course.pk})

    def test_list_GET(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)

    def test_list_by_name_GET(self):
        resp = self.client.get(reverse('list'))
        self.assertEqual(resp.status_code, 200)

    def test_detail_by_id(self):
        resp = self.client.get(self.detail_url)
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        data = {
            "name": "new course",
            "description": "new course description",
            "logo": "фото",
            "category": 1,
            "contact": 1,
            "branch": 1
        }
        resp = self.client.post(reverse('list'), data, format='json')
        self.assertEqual(resp.status_code, 201)

    # def test_delete_course(self):
        # course1 = Course.objects.create(
        #     name='Office systems',
        #     description='office systems',
        #     category=Category.objects.create(
        #         id=1
        #     ),
        #     logo='someLogo',
        #     contact=Contact.objects.create(
        #         id=1
        #     ),
        #     branch=Branch.objects.create(
        #         id=1
        #     )
        # )
        #
        # res = self.client.delete(self.detail_url, json.dump({
        #     'id': 2
        # }))
        # self.assertEquals(res.status_code, 204)

    # def test_delete_course(self):
    #     """Test deleting course"""
    #     res = self.client.delete(
    #         reverse('/courses/4', kwargs={'pk': self.course.pk}))
    #     self.assertEquals(res.status_code, 204)


