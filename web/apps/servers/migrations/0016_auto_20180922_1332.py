# Generated by Django 2.1.1 on 2018-09-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0015_discordemoji_animated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discordserver',
            name='premium_highlight',
            field=models.IntegerField(choices=[(0, 'No Highlight'), (1, 'Yellow - Premium Tier 1 + 2'), (2, 'Pink - Premium Tier 1 + 2'), (3, 'Red - Premium Tier 2')], default=0),
        ),
    ]