# Generated by Django 4.1.2 on 2022-10-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_archiveorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('yangi', 'Yangi'), ('olindi', 'Olindi'), ('yetkazildi', 'Yetkazildi!')], default='yangi', max_length=100),
        ),
    ]
