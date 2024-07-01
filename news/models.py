from django.db import models
from django.urls import reverse
from users.models import UserProfile

class Category(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="id دسته بندی")
    name = models.CharField(max_length=100, verbose_name='دسته بندی')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url', null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return f'( {self.name} - {self.url_title} - {self.id})'


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    cover_image = models.ImageField(upload_to='static/images', verbose_name='تصویر کاور', null=True, blank=True)
    content = models.TextField(verbose_name='محتوا')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='نویسنده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    slide_show = models.BooleanField(default=False, verbose_name='نمایش خبر در اسلایدر دسته بندی')
    is_urgent = models.BooleanField(default=False, verbose_name='نمایش خبر در اسلایدر صفحه اصلی')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='قابل مشاهده / غیرقابل مشاهده')
    

    def get_absolute_url(self):
        return reverse('news-detail', args=[self.slug])
   
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