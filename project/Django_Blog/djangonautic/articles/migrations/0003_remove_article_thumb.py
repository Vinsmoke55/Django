# Generated by Django 4.2.2 on 2023-07-06 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumb',
        ),
    ]
