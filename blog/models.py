from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	url = models.CharField(max_length=200)
	published_date = models.DateTimeField(blank = True, null = True)
	views = models.IntegerField()
	content = RichTextUploadingField()    
	def publish(self):
		self.published_date = timezone.now()
		views = 0
		self.save()
        
	def __str__(self):
		return self.title
              
class Activities(models.Model):
	sets = models.ForeignKey('Sets', to_field='brief')
	title = models.CharField(max_length=200)
	text = RichTextUploadingField()
	published_date = models.DateTimeField(blank = True, null = True)
	age = models.CharField(max_length=8)
#	The field 'age' has the following format, for example: '42'
#	It means that the activity is for chldren 4 years old or 2 years old

    # XXXXXXX
   
	def publish(self):
		self.published_date = timezone.now()
		self.save()
        
	def __str__(self):
		return self.title
# Create your models here.

class Sets(models.Model):
	author = models.ForeignKey('auth.User')
	brief = models.CharField(max_length=3, unique=True, default = 'sdf')
	title = models.CharField(max_length = 100)
	text = RichTextUploadingField()
	age = models.CharField(max_length=8)
	price = models.IntegerField()	
	main_image = models.ImageField(default='photos/1.jpeg')
	def publish(self):
		self.save()
	def __str__(self):
		return self.title

