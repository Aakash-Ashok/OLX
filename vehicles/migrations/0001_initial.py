# Generated by Django 4.2.4 on 2023-10-09 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('km_driven', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('owner_type', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
