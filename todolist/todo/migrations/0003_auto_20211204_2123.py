# Generated by Django 3.2.9 on 2021-12-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_input_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='date',
        ),
        migrations.AddField(
            model_name='input',
            name='compulsory',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='input',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='input',
            name='task',
            field=models.CharField(default='', max_length=100),
        ),
    ]