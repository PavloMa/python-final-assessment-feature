# Generated by Django 3.1.3 on 2022-11-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_auto_20221118_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.CharField(default='[Choice text]', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(default='[Question text]', max_length=255, null=True),
        ),
    ]
