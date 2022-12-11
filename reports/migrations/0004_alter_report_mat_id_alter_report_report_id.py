# Generated by Django 4.0.4 on 2022-07-08 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_parachute_material_matname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='mat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reports.parachute_material'),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reports.ray_report'),
        ),
    ]