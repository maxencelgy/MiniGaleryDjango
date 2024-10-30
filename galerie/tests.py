from django.test import TestCase
from .models import Image
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class ImageUploadTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_upload_image(self):
        with open('test_image.jpg', 'rb') as img:
            response = self.client.post(reverse('image-list'), {'title': 'Test Image', 'image': img})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_thumbnail_generation(self):
        image = Image.objects.create(title='Test Image', image='path/to/test_image.jpg')
        self.assertIsNotNone(image.thumbnail)
