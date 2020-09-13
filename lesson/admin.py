from django.contrib import admin
from lesson.models import Lesson, Homework, Exam, LessonContent
# Register your models here.


class LessonAdmin(admin.ModelAdmin):
	list_display = ('title','lessonID','description','create_at','update_at')
	list_filter = ('lessonID',)

class detaAdmin(admin.ModelAdmin):
	list_display = ('userID','title','create_at','update_at')
	list_filter = ('userID','create_at','update_at')

admin.site.register(Lesson,detaAdmin)
admin.site.register(LessonContent,LessonAdmin)
admin.site.register(Homework,LessonAdmin)
admin.site.register(Exam,LessonAdmin)