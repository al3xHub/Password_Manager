# Generated by Django 3.1.5 on 2024-04-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20240424_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='website_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='website_notes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
