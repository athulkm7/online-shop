# Generated by Django 4.1.3 on 2022-12-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='proddetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField()),
                ('Desc', models.CharField(blank=True, max_length=100, null=True)),
                ('Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]