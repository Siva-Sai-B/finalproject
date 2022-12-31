from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog import Forms
from .models import Post 
from django.contrib import messages
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
posts = [post for post in Post.objects.all()]

class PostListView(ListView):
    model=Post 
    template_name='blog/home.html'  # we should name html template as <app>/<model>_<viewtype>.html to skip this line
    context_object_name='posts'    #in class based views as we given model=Post, the default name given to Post objects is objectlist. As in home.html we used 'posts' as list of post objects so we set name 'posts' to objectlists. Or if we use objectlist in template then we can skip this line
    ordering=['-date_posted']   #to get the latest post first

class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content'] 
    success_url='../../'
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin,UpdateView):
    model=Post
    fields=['title','content'] 
    success_url='../../'
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post. author:
               return True

        return False
class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin,DeleteView):
    model=Post
    success_url='../../'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post. author:
               return True


def home(request):
    return render(request,'blog/home.html',{'posts':posts})







def about(request):
    return render(request,'blog/about.html')
@login_required
def profile(request):
    if request.method=='POST':

        u_form=Forms.UserUpdateForm(request.POST,instance=request.user)
        p_form=Forms.ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been successfully updated!')
            return redirect('profile')
    else:
        u_form=Forms.UserUpdateForm(instance=request.user)
        p_form=Forms.ProfileUpdateForm(instance=request.user.profile)
    context={'u_form':u_form,'p_form':p_form}
    return render(request,'blog/profile.html',context )
'''
def addpost(request):
    if request.method=='POST':

        addpost_form=Forms.AddPostForm()
        addpost_form.save()
        if 1 :
            addpost_form
           
            messages.success(request,f'New Post has been successfully Posted!')
            return redirect('blog/home.html')
        else:
            messages.error(request,f'New Post has been Failed !')
    else:
        
        addpost_form=Forms.AddPostForm()
  
    context={'addpost_form':addpost_form}
    return render(request,'blog/addpost.html',context)
'''

