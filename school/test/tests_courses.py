from rest_framework.test import APITestCase
from school.models import Course
from django.urls import reverse
from rest_framework import status


class CoursesTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('school:Courses-list')
        self.course1 = Course.objects.create(
            code='CTT1', description='Test Course', level='I')
        self.course2 = Course.objects.create(
            code='CTT2', description='Test Course 2', level='A')

    def test_list_course_request(self):
        """Test for get courses request"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        """Test for create courses"""
        payload = {"code": 'CTT3', "description": 'Test Course', "level": 'I'}
        response = self.client.post(self.list_url, payload)

        exists = Course.objects.filter(code='CTT3').exists()

        self.assertTrue(exists)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete_course(self):
        """Should delete a course"""
        course = Course.objects.create(
            code='CTTD', description='Test Course delete', level='A')

        url = reverse('school:Courses-detail', kwargs={'pk': course.id})
        response = self.client.delete(url)

        exists = Course.objects.filter(pk=course.id).exists()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(exists)

    def test_update_course(self):
        """Should update a course with put"""
        payload = {"code": 'CTT1',
                   "description": 'Test Course Update', "level": 'B'}

        url = reverse('school:Courses-detail', kwargs={'pk': self.course1.id})
        response = self.client.put(url, payload)

        course = Course.objects.get(pk=self.course1.id)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(course.description, payload['description'])
