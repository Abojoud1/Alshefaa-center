# Generated by Django 4.0.4 on 2022-07-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.IntegerField(null=1)),
                ('patien_id', models.IntegerField(null=True)),
                ('doc_id', models.IntegerField(null=True)),
                ('cat_id', models.IntegerField(null=True)),
                ('item_id', models.IntegerField(null=True)),
                ('mat_id', models.IntegerField(null=True)),
                ('state', models.TextField(null=True)),
                ('patient_preparation', models.TextField(null=True)),
                ('injection_method', models.CharField(max_length=20, null=True)),
                ('injection_quantity', models.CharField(max_length=20, null=True)),
                ('KV', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('MAS', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('ImagePathstring', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
            ],
        ),
    ]
