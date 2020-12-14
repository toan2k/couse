from django.urls import path
from .views import *


urlpatterns = [
    path('course/<slug>/', course_details_view, name='CourseDetailsView'),
]
