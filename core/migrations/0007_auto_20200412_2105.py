# Generated by Django 2.2.12 on 2020-04-12 21:05

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
