# Generated by Django 4.0.4 on 2022-07-11 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_alter_doctor_spe_id'),
        ('general', '0002_alter_categorys_catname_alter_items_itemname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys',
            name='Superviser_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='doctors.superviser_doctor'),
        ),
    ]