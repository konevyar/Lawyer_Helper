# Generated by Django 4.1.7 on 2023-02-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LawHelp', '0008_remove_case_inner_id_alter_case_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_card',
            field=models.URLField(null=True),
        ),
    ]
