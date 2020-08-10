# Generated by Django 2.0.5 on 2018-06-27 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='Contact_Number',
            field=models.CharField(default=1, max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Comment',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Email',
            field=models.EmailField(max_length=250, unique=True),
        ),
    ]