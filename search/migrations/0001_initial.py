# Generated by Django 5.0.6 on 2024-06-28 21:13

import search.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=search.models.image_upload2)),
                ('features1', models.CharField(choices=[(' Wi-Fi', ' Wi-Fi'), ('parking', 'parking'), ('swimming pool', 'swimming pool'), ('garden', 'garden'), ('The mosque', 'The mosque'), (' Air conditioning', ' Air conditioning'), (' cafe', ' cafe'), ('Barber/beauty salon', 'Barber/beauty salon'), ('Luggage storage', 'Luggage storage'), ('Restaurant', 'Restaurant')], max_length=50)),
                ('features2', models.CharField(choices=[(' Wi-Fi', ' Wi-Fi'), ('parking', 'parking'), ('swimming pool', 'swimming pool'), ('garden', 'garden'), ('The mosque', 'The mosque'), (' Air conditioning', ' Air conditioning'), (' cafe', ' cafe'), ('Barber/beauty salon', 'Barber/beauty salon'), ('Luggage storage', 'Luggage storage'), ('Restaurant', 'Restaurant')], max_length=50)),
                ('features3', models.CharField(choices=[(' Wi-Fi', ' Wi-Fi'), ('parking', 'parking'), ('swimming pool', 'swimming pool'), ('garden', 'garden'), ('The mosque', 'The mosque'), (' Air conditioning', ' Air conditioning'), (' cafe', ' cafe'), ('Barber/beauty salon', 'Barber/beauty salon'), ('Luggage storage', 'Luggage storage'), ('Restaurant', 'Restaurant')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('continent', models.CharField(choices=[('أسيا', 'أسيا'), ('أفريقيا', 'أفريقيا'), ('أمريكا', 'أمريكا'), ('أوروبا', 'أوروبا')], max_length=30)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
