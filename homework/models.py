from django.db import models

# Create your models here.


class HomeWork(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)


    content = models.CharField(max_length=200)

    upload = models.FileField(
        verbose_name='Ödev Dosyası', upload_to='homework')

    created_date = models.DateTimeField(auto_now_add=True)
    
    finish_date = models.DateTimeField(auto_now_add=False)



    def __str__(self):
        return self.title