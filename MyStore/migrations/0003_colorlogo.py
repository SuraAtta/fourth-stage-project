# Generated by Django 4.0.6 on 2023-04-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyStore', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_code', models.CharField(help_text='ادخل اللون مثل: OxFF45B9EE', max_length=12, verbose_name='لون الثيم')),
                ('image', models.ImageField(upload_to='images/', verbose_name='لوكو')),
            ],
        ),
    ]
