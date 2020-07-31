from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #if the  User is deleted their post are deleted as well
    
    def __str__(self):
        return self.title

    #this based function allows us to redirect the user after creating his post to the post-detail url
    #in this case we used the reverse methode instead of using redirect method, because reverse return 
    #the url as a string, however redirect will redirect the user to a specific root 
    
    def get_absolute_url(self):
    	return reverse('post-detail', kwargs={'pk': self.pk})
    
