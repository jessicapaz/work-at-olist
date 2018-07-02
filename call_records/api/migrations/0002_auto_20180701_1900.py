# Generated by Django 2.0.6 on 2018-07-01 19:00

from django.db import migrations, models
import validators.phone_validator


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='phone_number',
            field=models.BigIntegerField(unique=True, validators=[validators.phone_validator.validate_phone]),
        ),
    ]