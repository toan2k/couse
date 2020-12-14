from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
from products.models import Course


class HomeView(View):
    def get(self, request):
        object_list = Course.objects.all()
        context = {
            'title': 'EduChamp - Home Page',
            'object_list': object_list
        }
        return render(request, 'home.html', context)


class CourseView(View):
    def get(self, request):
        object_list = Course.objects.all()
        context = {
            'title': 'EduChamp - Courses Page',
            'object_list': object_list
        }
        return render(request, 'courses.html', context)


class AboutView(View):
    def get(self, request):
        context = {
            'title': 'EduChamp - About Page'
        }
        return render(request, 'about.html', context)


class CourseDetailsView(View):
    def get(self, request):
        context = {
            'title': 'EduChamp - Course Details Page'
        }
        return render(request, 'coursedetails.html', context)


class ProfileView(View):
    def get(self, request):
        context = {
            'title': 'EduChamp - Profile Page'
        }
        if request.user.is_authenticated:
            return render(request, 'profile.html', context)
        return redirect("/login")


class CartView(View):
    def get(self, request):
        context = {
            'title': 'EduChamp - Cart Page'
        }
        return render(request, 'cart.html', context)


class LoginView(View):

    def get(self, request):

        form = LoginForm(request.POST or None)
        context = {
            'title': 'EduChamp - Login Page',
            'form_login': LoginForm(),
        }
        print("User login in")
        # print(request.user.is_authenticated())

        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect("/login")

            else:
                print("Error")
        return render(request, 'login.html', context)


def login123(request):
    if request.user.is_authenticated:
        return redirect("/profile")
    form = LoginForm(request.POST or None)
    context = {
        'title': 'EduChamp - Login Page',
        'form_login': LoginForm(),
    }
    print("User login in")
       # print(request.user.is_authenticated())

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect("/profile")

        else:
            print("Error")
    return render(request, 'login.html', context)


class RegisterView(View):
    def get(self, request):
        context = {
            'title': 'EduChamp - Register Page'
        }
        return render(request, 'register.html', context)

User = get_user_model()
def register_page(request):
    if request.user.is_authenticated:
        return redirect("/profile")
    form = RegisterForm(request.POST or None)

    context = {
            'title': 'EduChamp - Register Page',
            'form_register': RegisterForm(),
        }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user_new = User.objects.create_user(username, email, password)
        user_new.save()
        return redirect("/login")
    return render(request, 'register.html', context)

class ContactView(View):
    def get(self, request):
        contact_form = ContactForm(request.POST or None)
        context = {
            'title': 'EduChamp - Contact Page',
            'form': contact_form
        }
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
        return render(request, 'contact.html', context)


class BlogView(View):
    def get(self, request):
        context = {
            'title': 'EduChamp - Blog Page'
        }
        return render(request, 'blog.html', context)


class BlogDetailsView(View):
    def get(self, request):
        context = {
            'title': 'EduChamp - Blog Details Page'
        }
        return render(request, 'blogdetails.html', context)


class EventView(View):
    def get(self, request):
        context = {
            'title': 'EduChamp - Event Page'
        }
        return render(request, 'event.html', context)


class EventDetailsView(View):
    def get(self, request):
        context = {
            'title': 'EduChamp - Event Details Page'
        }
        return render(request, 'eventdetails.html', context)
