# Generated by Django 3.0.14 on 2023-01-19 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drones',
            name='brand',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='drones',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='drones',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('adress', models.TextField(blank=True, max_length=1000)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(blank=True, default='Waiting')),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drone', to='mainapp.Drones')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fetaures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature', to='mainapp.Drones')),
            ],
        ),
    ]
