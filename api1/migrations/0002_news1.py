# Generated by Django 3.2.9 on 2022-01-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='static/images')),
                ('news', models.CharField(max_length=10000)),
            ],
        ),
    ]