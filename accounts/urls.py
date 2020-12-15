from django.urls import path, include
from .views import *

app_name = 'core'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profileview'),
    
]
