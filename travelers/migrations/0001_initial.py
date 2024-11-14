# Generated by Django 5.1 on 2024-11-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='destination_images/')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('attractions', models.JSONField(blank=True, null=True)),
                ('best_time_to_visit', models.JSONField(blank=True, null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='destinations/')),
                ('additional_images', models.ManyToManyField(blank=True, to='travelers.destinationimage')),
            ],
        ),
    ]