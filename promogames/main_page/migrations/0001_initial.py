# Generated by Django 4.1.5 on 2023-01-26 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='main_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('store', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=100)),
                ('link_url', models.CharField(max_length=100)),
                ('discount_price', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]