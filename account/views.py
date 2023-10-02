from .models import User
from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "account/Login.html", {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error('username', 'اطلاعات نامعتبر')
        else:
            form.add_error('password', 'اطلاعات نامعتبر')
        return render(request, "account/Login.html", {'form': form})


def user_logout(request):
    logout(request)
    return redirect("/")


class UserRegister(View):
    def get(self, request):
        form = RegisterForm
        return render(request, "account/Register.html", {'form': form})

    def post(self, request):
        context = {'errors': []}

        if request.user.is_authenticated:
            return redirect('home:home')

        if request.method == "POST":
            fullname = request.POST.get('fullname')
            phone_number = request.POST.get('phone_number')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 != password2:
                context['errors'].append('Passwords are not match')
                return render(request, "account/Register.html", context)

            user = User.objects.create_user(fullname=fullname, password=password1, phone_number=phone_number)
            login(request, user)
        return redirect('home:home')
