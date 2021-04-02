from django.urls import path, include
from school import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', views.StudentsViewSet, basename='Students')
router.register('courses', views.CoursesViewSet, basename='Courses')
router.register('registrations', views.RegistrationsViewSet, basename='Registrations')

app_name = 'school'

urlpatterns = [
    path('', include(router.urls)),
    path('students/<int:pk>/registrations/', views.ListRegistrationsViewSet.as_view()),
    path('courses/<int:pk>/students/', views.ListCourseStudentsViewSet.as_view())
]