# Generated by Django 4.2.3 on 2023-09-29 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_alter_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(null=True, upload_to='post_images/'),
        ),
    ]
