# Generated by Django 2.2.12 on 2020-04-12 20:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200412_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=250, primary_key=True, serialize=False),
        ),
    ]
