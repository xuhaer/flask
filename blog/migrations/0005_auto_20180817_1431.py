# Generated by Django 2.0.7 on 2018-08-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180813_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='digest_img',
            field=models.CharField(blank=True, help_text='可选项，若为空则取正文中第一张图片', max_length=256),
        ),
    ]
