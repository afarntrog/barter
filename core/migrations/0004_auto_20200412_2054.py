# Generated by Django 2.2.12 on 2020-04-12 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200412_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
