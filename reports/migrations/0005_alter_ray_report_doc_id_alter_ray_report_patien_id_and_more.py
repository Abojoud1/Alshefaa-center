# Generated by Django 4.0.4 on 2022-07-11 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_alter_doctor_spe_id'),
        ('patients', '0002_alter_patients_fname_alter_patients_lname'),
        ('general', '0003_alter_categorys_superviser_id'),
        ('reports', '0004_alter_report_mat_id_alter_report_report_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ray_report',
            name='doc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='doctors.doctor'),
        ),
        migrations.AlterField(
            model_name='ray_report',
            name='patien_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='patients.patients'),
        ),
        migrations.AlterField(
            model_name='report',
            name='cat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='general.categorys'),
        ),
        migrations.AlterField(
            model_name='report',
            name='item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='general.items'),
        ),
    ]