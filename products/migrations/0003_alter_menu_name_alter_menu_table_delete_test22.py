# Generated by Django 4.0.3 on 2022-04-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_test22'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterModelTable(
            name='menu',
            table='menu',
        ),
        migrations.DeleteModel(
            name='test22',
        ),
    ]
