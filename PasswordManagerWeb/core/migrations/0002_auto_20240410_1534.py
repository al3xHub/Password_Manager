# Generated by Django 3.1.5 on 2024-04-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='master_password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='site',
            name='website_notes',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
