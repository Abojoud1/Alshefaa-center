# Generated by Django 4.0.4 on 2022-07-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, null=True)),
                ('Address', models.CharField(max_length=20, null=True)),
                ('Phon', models.CharField(max_length=20, null=True)),
                ('Spe_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specializations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SpeName', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Superviser_doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, null=True)),
                ('Phon', models.CharField(max_length=20, null=True)),
                ('WorkStart', models.CharField(max_length=20, null=True)),
                ('WorkEnd', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
