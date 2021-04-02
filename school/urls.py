from django.urls import path, include
from school import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', views.StudentsViewSet)
router.register('courses', views.CoursesViewSet)

app_name = 'school'

urlpatterns = [
    path('', include(router.urls))
]