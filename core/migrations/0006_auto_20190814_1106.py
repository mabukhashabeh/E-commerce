# Generated by Django 2.1.5 on 2019-08-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190814_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='/no-image.png/', upload_to=''),
        ),
    ]
