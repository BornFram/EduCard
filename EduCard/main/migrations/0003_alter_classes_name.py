# Generated by Django 4.1.5 on 2023-01-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_classes_name_alter_items_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='name',
            field=models.CharField(max_length=200, verbose_name='class'),
        ),
    ]