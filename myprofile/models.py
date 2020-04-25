from django.db import models

# Create your models here.
class Education(models.Model):
	
	course = models.CharField(max_length=100)
	duration = models.CharField(max_length=100)
	college = models.CharField(max_length=100)
	desc= models.TextField()

class Experience(models.Model):
	
	role = models.CharField(max_length=100)
	duration = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	desc= models.TextField()

class Skills(models.Model):
	
	name = models.CharField(max_length=100)
	size = models.CharField(max_length=100)
	volume = models.CharField(max_length=100)
	
class Certificate(models.Model):
	
	name = models.CharField(max_length=100)
	duration = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	desc= models.TextField()	

class Project(models.Model):
	
	name = models.CharField(max_length=100)
	desc= models.TextField()
	logo= models.CharField(max_length=100)

class Contact(models.Model):
	
	title = models.CharField(max_length=100)
	desc= models.TextField()
	logo= models.CharField(max_length=100)