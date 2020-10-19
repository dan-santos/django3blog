# Generated by Django 3.1.2 on 2020-10-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
