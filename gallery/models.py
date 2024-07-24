from django.db import models

class Gallery(models.Model):
    image = models.ImageField(upload_to='static/images', verbose_name='تصویر', null=True, blank=True)
    title = models.CharField(max_length=300, verbose_name='عنوان', null=True)
    author = models.CharField(max_length=200, verbose_name='نویسنده')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت', null=True)

    class Meta:
        verbose_name = 'گزارش تصویری'
        verbose_name_plural = 'گزارش های تصویری'

    def __str__(self):
        return f"{self.author} - {self.create_date}"
