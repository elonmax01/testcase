# Generated by Django 5.0.1 on 2024-01-22 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_card_tags_delete_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='minskin',
            field=models.CharField(blank=True, choices=[('y', 'yes'), ('n', 'no')], default='y', help_text='Маршрут внутригородской или с выездом за город?', max_length=1),
        ),
    ]
