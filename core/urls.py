from django.urls import path, include
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='homeview'),
    path('courses/', CourseView.as_view(), name='CourseView'),
    path('', include('products.urls'), name='CourseDetailsView'),
    path('profile/', ProfileView.as_view(), name='ProfileView'),
    path('login/', login123, name='LoginView'),
    path('register/', register_page, name='RegisterView'),
    path('cart', CartView.as_view(), name='CartView'),
    path('about/', AboutView.as_view(), name='AboutView'),
    path('contact/', ContactView.as_view(), name='ContactView'),
    path('blog/', BlogView.as_view(), name='BlogView'),
    path('blog-details/', BlogDetailsView.as_view(), name='BlogDetailsView'),
    path('events/', EventView.as_view(), name='EventView'),
    path('event-details/', EventDetailsView.as_view(), name='EventDetailsView'),
    
]
