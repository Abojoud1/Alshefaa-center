# Generated by Django 4.0.4 on 2022-07-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys',
            name='CatName',
            field=models.CharField(default='zzz', max_length=20),
        ),
        migrations.AlterField(
            model_name='items',
            name='ItemName',
            field=models.CharField(default='zzz', max_length=20),
        ),
    ]