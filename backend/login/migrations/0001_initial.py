# Generated by Django 2.2.6 on 2019-11-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseId', models.IntegerField()),
                ('courseName', models.TextField()),
                ('meetingSchedule', models.TextField()),
            ],
        ),
    ]
