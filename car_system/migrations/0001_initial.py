# Generated by Django 3.2.7 on 2022-07-20 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=200)),
                ('goal_province', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total_chairs', models.IntegerField(default=0)),
                ('chairs', models.IntegerField(default=0)),
                ('expire_time', models.DateTimeField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_system.goal')),
            ],
        ),
    ]