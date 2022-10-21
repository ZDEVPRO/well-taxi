# Generated by Django 4.1.2 on 2022-10-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_user_order_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('yangi', 'Yangi'), ('olindi', 'Olindi')], default='yangi', max_length=100)),
                ('qayerdan', models.CharField(max_length=1000)),
                ('qayerga', models.CharField(max_length=1000)),
                ('person_count', models.CharField(default=1, max_length=100)),
                ('price', models.IntegerField(default=100000)),
                ('client_phone', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=200)),
            ],
        ),
    ]
