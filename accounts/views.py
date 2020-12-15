from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import CustomerUser
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
# from django.contrib.auth import authenticate, login, get_user_model
# from django.contrib.auth.models import User


# Create your views here.
class ProfileView(View):
    def get(self, request):
        context = {
            'title': 'EduChamp - Profile Page',
           
        }
        if request.user.is_authenticated:
            return render(request, 'profile.html', context)
        return redirect("/login")

