# Generated by Django 4.0.4 on 2022-07-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_remove_ray_report_doc_id_remove_ray_report_patien_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='ImagePathstring',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]