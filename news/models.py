from django.db import models
from users.models import UserProfile

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return f"{self.name}"


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='نویسنده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
        
    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'

    def __str__(self):
        return f"{self.title} - {self.author}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='خبر')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='کاربر')
    content = models.TextField(verbose_name='محتوا')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f"{self.article} - {self.user}"