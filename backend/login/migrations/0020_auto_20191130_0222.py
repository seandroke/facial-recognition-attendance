# Generated by Django 2.2.7 on 2019-11-30 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_auto_20191127_0335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classes',
            options={'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name_plural': 'Students'},
        ),
    ]
