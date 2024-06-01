from django.shortcuts import render, get_object_or_404, redirect
from .models import TaskCategory
from .forms import TaskCategoryForm

def category_create(request):
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskCategoryForm()
    return render(request, 'category/category_form.html', {'form': form})
