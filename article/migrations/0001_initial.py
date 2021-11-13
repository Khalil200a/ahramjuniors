# Generated by Django 3.2.9 on 2021-11-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='article/image/')),
                ('date', models.CharField(blank=True, max_length=200)),
                ('document', models.FileField(blank=True, null=True, upload_to='article/doc')),
            ],
        ),
    ]
