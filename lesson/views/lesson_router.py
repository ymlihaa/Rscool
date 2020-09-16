from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from lesson.models import Lesson, LessonContent, Homework, Exam



def lessonRedirect(request,lessonID):
	print(lessonID)
	data = LessonContent.objects.filter(lessonID=lessonID)

	return render(request,'page/lessons.html',{'data':data})

