# Generated by Django 4.0.3 on 2022-04-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_quote_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='email',
            field=models.EmailField(blank=True, max_length=30, null=True, verbose_name='Почтовый адрес'),
        ),
    ]