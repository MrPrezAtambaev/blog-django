# Generated by Django 4.2.1 on 2023-05-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
