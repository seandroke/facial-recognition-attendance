# Generated by Django 2.2.7 on 2019-11-27 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_auto_20191127_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='studentPicture',
            field=models.FileField(default=1, upload_to='student_pic/'),
        ),
    ]
