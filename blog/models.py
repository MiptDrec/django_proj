from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	url = models.CharField(max_length=200)
	published_date = models.DateTimeField(blank = True, null = True)
	views = models.IntegerField()
    
	def publish(self):
		self.published_date = timezone.now()
		views = 0
		self.save()
        
	def __str__(self):
		return self.title
              
class Activities(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	published_date = models.DateTimeField(blank = True, null = True)
	age = models.PositiveIntegerField()
    # XXXXXXX
	Lepka = 'lep'
	Math = 'mat'
	drawing = 'dra'
	motorika = 'mot'
	none_cat = 'non'
	category_choice = ( (Lepka, 'Лепка'), (Math, 'Математика'), (drawing, 'Рисование'), (motorika, 'Моторика'))
	category = models.CharField(max_length=3, choices = category_choice, default = none_cat)
    
	def publish(self):
		self.published_date = timezone.now()
		self.save()
        
	def __str__(self):
		return self.title
# Create your models here.

class Sets(models.Model):
	name = models.CharField(max_length = 100)
	title = models.CharField(max_length = 100)
	text = models.TextField()
	pic = models.ImageField(upload_to = 'pic_folder/')
	photos = []
	def add_photo(self, photo):
		photos.append(photo)	
#	pictures = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/1.jpg')

#	def insert_photo(self, photo):
#		self.pictures.append(photo)	
	def publish(self):
		self.save()
