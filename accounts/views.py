from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View


class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        signup_form = UserCreationForm()
        return render(request, 'accounts/login.html', {'form': form, 'signup_form': signup_form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        signup_form = UserCreationForm()
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/login.html', {'form': form, 'signup_form': signup_form})


# def login_view(request):
#     form = AuthenticationForm(data=request.POST)
#     signup_form = UserCreationForm()
#     if form.is_valid():
#         user = form.get_user()
#         login(request, user)
#         return redirect('home')
#     return render(request, 'accounts/login.html', {'form': form, 'signup_form': signup_form})


class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        return render(request, 'accounts/signup.html', {'form': form})


# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts:login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect("home")

# def logout_view(request):
#     if request.method == 'GET':
#         logout(request)
#         return redirect("home")
