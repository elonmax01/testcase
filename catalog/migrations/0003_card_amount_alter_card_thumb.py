# Generated by Django 5.0.1 on 2024-01-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='thumb',
            field=models.ImageField(upload_to='media/'),
        ),
    ]