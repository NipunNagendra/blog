# Generated by Django 4.1 on 2022-08-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtext', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
