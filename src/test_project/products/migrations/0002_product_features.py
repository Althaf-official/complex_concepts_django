# Generated by Django 3.1 on 2023-08-09 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
