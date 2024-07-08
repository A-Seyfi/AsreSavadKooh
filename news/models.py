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
    author = models.CharField(max_length=200, verbose_name='نویسنده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    slide_show = models.BooleanField(default=False, verbose_name='نمایش خبر در اسلایدر دسته بندی')
    is_urgent = models.BooleanField(default=False, verbose_name='نمایش خبر در اسلایدر صفحه اصلی')
    slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True ,verbose_name='عنوان در url')
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
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت', null=True)
    text = models.TextField(verbose_name='متن نظر', null=True)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f"{self.article} - {self.user}"
    

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
    

class AboutUs(models.Model):
    intro_text = models.TextField(verbose_name='متن معرفی', null=True)
    email = models.EmailField(max_length=100, verbose_name='ایمیل ارتباطی', null=True)
    phone_number = models.CharField(max_length=100, verbose_name='شماره تلفن ارتباظی', null=True)

    class Meta:
        verbose_name = 'صفحه درباره'
        verbose_name_plural = 'مدیریت صفحه درباره'

    def __str__(self):
        return f"{self.email} - {self.phone_number}"