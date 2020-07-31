from django.shortcuts import render
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView
)
from .models import Post
#from django.http import HttpResponse

def Home(request):
    context = {
            'posts':Post.objects.all()
    }
    return render(request, 'blog\home.html', context)

class PostListView(ListView):
	model = Post 
	template_name = 'blog/home.html' #the template is <app>/<model>_<ViewType>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] #to generate an Post order, basing on the posted date 

class PostDetailView(DetailView):
	model = Post 

#this class is for creating a new view 'POSTs'
class PostCreateView(CreateView):
	model = Post 
	#fields for creating a new View;
	fields = ['title', 'content']
	
	def form_valid(self, form):
		#the form that the user trying to submit, befor you do that take the instance
		#and the author equal to the current loged-in user 
		form.instance.author = self.request.user
		#once we do that we need to validate our form 
		return super().form_valid(form)

def about(request):
    return render(request, 'blog\About.html', {'title':'About page'})
