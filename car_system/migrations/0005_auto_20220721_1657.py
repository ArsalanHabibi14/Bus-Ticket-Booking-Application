# Generated by Django 3.2.7 on 2022-07-21 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_system', '0004_auto_20220721_0802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={},
        ),
        migrations.AlterModelOptions(
            name='goal',
            options={},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={},
        ),
        migrations.AddField(
            model_name='car',
            name='is_avaliable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='chairs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='expire_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_system.goal'),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='total_chairs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='goal',
            name='goal_province',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='goal',
            name='province',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_system.car'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_pdf',
            field=models.FileField(blank=True, null=True, upload_to='ticket/'),
        ),
    ]
