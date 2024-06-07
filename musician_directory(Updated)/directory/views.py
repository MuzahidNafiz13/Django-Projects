from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm
# from django.views import View
# from .forms import RegisterForm, UserForm


# class RegisterView(View):
#     def get(self, request):
#         form = RegisterForm()
#         return render(request, 'directory/register.html', {'form': form})

#     def post(self, request):
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#         return render(request, 'directory/register.html', {'form': form})

# class LoginView(View):
#     def get(self, request):
#         form = AuthenticationForm()
#         return render(request, 'directory/login.html', {'form': form})

#     def post(self, request):
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#         return render(request, 'directory/login.html', {'form': form})


class MusicianListView(ListView):
    model = Musician
    template_name = 'directory/musician_list.html'
    context_object_name = 'musicians'

class MusicianCreateView(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'directory/musician_form.html'
    success_url = reverse_lazy('musician_list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Musician '{self.object}' successfully added!")
        return response

class MusicianUpdateView(LoginRequiredMixin, UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'directory/musician_form.html'
    success_url = reverse_lazy('musician_list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Musician '{self.object}' successfully updated!")
        return response

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'directory/album_form.html'
    success_url = reverse_lazy('musician_list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Album '{self.object}' successfully added!")
        return response

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'directory/album_form.html'
    success_url = reverse_lazy('musician_list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Album '{self.object}' successfully updated!")
        return response


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'directory/album_confirm_delete.html'
    success_url = reverse_lazy('musician_list')
    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        messages.success(request, f"Album '{album}' successfully deleted!")
        return super().delete(request, *args, **kwargs)
