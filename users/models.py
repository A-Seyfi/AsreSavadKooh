from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()