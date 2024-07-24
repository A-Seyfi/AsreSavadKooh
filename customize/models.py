from django.db import models

class AboutUs(models.Model):
    intro_text = models.TextField(verbose_name='متن معرفی', null=True)
    email = models.EmailField(max_length=100, verbose_name='ایمیل ارتباطی', null=True)
    phone_number = models.CharField(max_length=100, verbose_name='شماره تلفن ارتباظی', null=True)

    class Meta:
        verbose_name = 'صفحه درباره'
        verbose_name_plural = 'مدیریت صفحه درباره'

    def __str__(self):
        return f"{self.email} - {self.phone_number}"

class Links(models.Model):
    insta_urls = models.URLField(max_length=100, verbose_name="لینک اینستاگرام", blank=True)
    yt_urls = models.URLField(max_length=100, verbose_name="لینک یوتیوب", blank=True)
    linkedin_urls = models.URLField(max_length=100, verbose_name="لینک لینکداین", blank=True)
    fb_urls = models.URLField(max_length=100, verbose_name="لینک فیسبوک", blank=True)
    tt_urls = models.URLField(max_length=100, verbose_name="لینک توییتر", blank=True)

    class Meta:
        verbose_name = 'لینک های فوتر'
        verbose_name_plural = 'مدیریت لینک های فوتر'

    def __str__(self):
        return f"{self.fb_urls} - {self.insta_urls}"
    
class Address(models.Model):
    city = models.CharField(max_length=90, verbose_name='شهر یا منطقه', null=True)
    street = models.TextField(max_length=110, verbose_name='خیابان یا محله', null=True)
    post_code = models.CharField(max_length=50 ,verbose_name='کد پستی یا شماره تلفن', null=True)

    class Meta:
        verbose_name = 'آدرس در فوتر'
        verbose_name_plural = 'مدیریت آدرس در فوتر'

    def __str__(self):
        return f"{self.city} - {self.post_code}"