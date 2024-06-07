# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Musician, Album
# from .forms import MusicianForm, AlbumForm

# def musician_list(request):
#     musicians = Musician.objects.all()
#     return render(request, 'directory/list_music.html', {'musicians': musicians})

# def musician_create(request):
#     if request.method == 'POST':
#         form = MusicianForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('musician_list')
#     else:
#         form = MusicianForm()
#     return render(request, 'directory/form_music.html', {'form': form})

# def musician_update(request, pk):
#     musician = get_object_or_404(Musician, pk=pk)
#     if request.method == 'POST':
#         form = MusicianForm(request.POST, instance=musician)
#         if form.is_valid():
#             form.save()
#             return redirect('musician_list')
#     else:
#         form = MusicianForm(instance=musician)
#     return render(request, 'directory/form_music.html', {'form': form})

# def musician_delete(request, pk):
#     musician = get_object_or_404(Musician, pk=pk)
#     if request.method == 'POST':
#         musician.delete()
#         return redirect('musician_list')
#     return render(request, 'directory/delete_music.html', {'musician': musician})

# def album_create(request):
#     if request.method == 'POST':
#         form = AlbumForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('musician_list')
#     else:
#         form = AlbumForm()
#     return render(request, 'directory/form_album.html', {'form': form})

# def album_update(request, pk):
#     album = get_object_or_404(Album, pk=pk)
#     if request.method == 'POST':
#         form = AlbumForm(request.POST, instance=album)
#         if form.is_valid():
#             form.save()
#             return redirect('musician_list')
#     else:
#         form = AlbumForm(instance=album)
#     return render(request, 'directory/form_album.html', {'form': form})

# def album_delete(request, pk):
#     album = get_object_or_404(Album, pk=pk)
#     if request.method == 'POST':
#         album.delete()
#         return redirect('musician_list')
#     return render(request, 'directory/delete_album.html', {'album': album})

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

class MusicianListView(ListView):
    model = Musician
    template_name = 'directory/list_music.html'
    context_object_name = 'musicians'

class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'directory/form_music.html'
    success_url = reverse_lazy('musician_list')

class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'directory/form_music.html'
    success_url = reverse_lazy('musician_list')

class MusicianDeleteView(DeleteView):
    model = Musician
    template_name = 'directory/delete_music.html'
    success_url = reverse_lazy('musician_list')

class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'directory/form_album.html'
    success_url = reverse_lazy('musician_list')

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'directory/form_album.html'
    success_url = reverse_lazy('musician_list')

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'directory/delete_album.html'
    success_url = reverse_lazy('musician_list')