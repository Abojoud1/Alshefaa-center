# Generated by Django 4.0.4 on 2022-07-11 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_alter_doctor_name_alter_specializations_spename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Spe_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='doctors.specializations'),
        ),
    ]
