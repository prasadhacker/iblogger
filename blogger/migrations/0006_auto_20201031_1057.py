# Generated by Django 3.1.2 on 2020-10-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0005_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='static'),
        ),
    ]
