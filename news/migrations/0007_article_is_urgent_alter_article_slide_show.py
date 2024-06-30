# Generated by Django 5.0 on 2024-06-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_article_slide_show_alter_article_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_urgent',
            field=models.BooleanField(default=False, verbose_name='نمایش خبر در اسلایدر صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slide_show',
            field=models.BooleanField(default=False, verbose_name='نمایش خبر در اسلایدر دسته بندی'),
        ),
    ]
