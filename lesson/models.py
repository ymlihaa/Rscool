from django.db import models
from account.models import MyUser
from djrichtextfield.models import RichTextField
# Create your models here.
class Lesson(models.Model):
	userID = models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=False)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class LessonContent(models.Model):
	lessonID = models.ForeignKey(Lesson,on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	content = models.FileField(upload_to='lesson-Content',blank=True)
	rich_content = RichTextField(null=True,blank=True)

	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Homework(models.Model):
	lessonID = models.ForeignKey(Lesson,on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	content = models.FileField(upload_to='homework',blank=True)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Exam(models.Model):
	lessonID = models.ForeignKey(Lesson,on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	content = models.FileField(upload_to='exam',blank=True)
	create_at = models.DateTimeField(verbose_name='Eklenme Tarihi',auto_now_add=True)
	update_at = models.DateTimeField(verbose_name='Güncellenme Tarihi',auto_now=True)

	def __str__(self):
		return self.title



