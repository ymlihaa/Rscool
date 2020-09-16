from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from lesson.models import Lesson, LessonContent, Homework, Exam


def profileRedirect(request):
	if request.user.is_authenticated:
		role = request.user.role
		print("user id ", request.user.id)
		Lesson_data = Lesson.objects.filter(userID=request.user.id)

		# data = Lesson.objects.get(userID=request.user.id)
		if role:
			# Burada Hoca sayfasını render et
			return render(request, 'page/profile_page/teacher_profile.html', {'data': Lesson_data})
		else:
			# BURADA ÖĞRENCİ SAYFASINI RENDER ET

			return render(request, 'page/profile_page/student_profile.html', {'data': Lesson_data})

	else:
		# BURADA YETKİSİZ GİRİŞ SAYFASINI RENDER ET
		return render(request,'page/auth_pages/autherr.html')


def accountRedirect(request):
	Lesson_data = Lesson.objects.filter(userID=request.user.id)
	return render(request, 'page/account.html', {'data': Lesson_data})

