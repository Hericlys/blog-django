# Generated by Django 4.2.2 on 2023-08-01 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(default='', max_length=255),
        ),
    ]
