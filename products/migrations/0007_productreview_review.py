# Generated by Django 5.0.7 on 2024-08-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='review',
            field=models.TextField(null=True),
        ),
    ]
