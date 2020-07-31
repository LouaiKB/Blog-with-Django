from django.db import models
from django.contrib.auth.models import User 
from PIL import Image 

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) 
	"""on_delete=models.CASCADE means that if the user is deleted 
	his profile will be deleted also, but if we delete the profile
	the user won't be deleted """
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'


	def save(self):
		super().save(); 
		img = Image.open(self.image.path)

		#this is in order to resize the image
		if img.height > 300 or img.width > 300:
			outpout_size = (300, 300)
			img.thumbnail(outpout_size)
			img.save(self.image.path)