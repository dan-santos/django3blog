# Generated by Django 3.1.2 on 2020-10-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]