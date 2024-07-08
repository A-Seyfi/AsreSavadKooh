from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    usernamefield = models.CharField(max_length=25, null=True,verbose_name='نام کاربری')
    password = models.CharField(max_length=50, verbose_name='رمز عبور')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()


