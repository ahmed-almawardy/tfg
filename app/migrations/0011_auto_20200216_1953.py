# Generated by Django 2.2.6 on 2020-02-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200216_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='info_type',
            field=models.CharField(choices=[('About', 'About'), ('Rules', 'Rules')], max_length=20),
        ),
    ]