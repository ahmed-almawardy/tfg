# Generated by Django 2.2.6 on 2020-02-17 17:05

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200216_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to=app.models.file_upload)),
            ],
        ),
        migrations.AlterField(
            model_name='package',
            name='period',
            field=models.CharField(choices=[('Month', 'Month'), ('3months', '3months')], default='Month', max_length=200),
        ),
    ]