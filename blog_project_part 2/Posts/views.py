from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse_lazy
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView


# Create your views here.
@login_required
def add_post(request):
    if request.method=='POST':
       post_form=forms.PostForm(request.POST)
       if post_form.is_valid():
           post_form.instance.author=request.user
           post_form.save()
           return redirect ("homepage")
    else:
        post_form=forms.PostForm()
    return render(request, 'add_post.html', {'form':post_form})

# add post using class based view
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Posts
    form_class= forms.PostForm
    template_name='add_post.html'
    success_url= reverse_lazy('profile')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


@login_required
def edit_post(request,id):
    post=models.Posts.objects.get(pk=id)
    post_form=forms.AuthorForm(instance=post)
    if request.method=='POST':
       post_form=forms.AuthorForm(request.POST, instance=post)
       if post_form.is_valid():
           post_form.instance.author=request.user
           post_form.save()
           return redirect ("homepage")
    return render(request, 'add_post.html', {'form':post_form})

# edit post with class based view
@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model=models.Posts
    form_class= forms.PostForm
    template_name='add_post.html'
    success_url=reverse_lazy('homepage')
    pk_url_kwarg= 'id'

@login_required
def delete_post(request,id):
    post=models.Posts.objects.get(pk=id)
    post.delete()
    return redirect("homepage")

# delete class based view
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model=models.Posts
    template_name='delete_post.html'
    success_url=reverse_lazy('homepage')
    pk_url_kwarg='id'

class DetailPostView(DetailView):
    model=models.Posts
    pk_url_kwarg='id'
    template_name= 'post_details.html'

    def post(self, request, *args,**kwargs):
        comment_form =forms.CommentForm(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post= post
            new_comment.save()
        return self.get(request, *args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        post = self.object
        comments= post.comments.all()
        comment_form= forms.CommentForm()

        context['comments']=comments
        context['comment_form']=comment_form
        return context
