from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .forms import RegisterForm, UserForm
from cars.models import Order

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'accounts/login.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        user_form = UserForm(instance=request.user)
        orders = Order.objects.filter(user=request.user)
        context = {
            'user_form': user_form,
            'orders': orders,
        }
        return render(request, 'accounts/profile.html', context)
    
    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
        orders = Order.objects.filter(user=request.user)
        context = {
            'user_form':user_form,
            'orders': orders
        }
        return render(request, 'accounts/profile.html', context)
        

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    
@method_decorator(login_required, name='dispatch')
class OrderHistoryView(View):
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        context = {
            'orders': orders,
        }
        return render(request, 'accounts/profile.html', context)
