# Generated by Django 2.0.4 on 2018-05-28 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_auto_20180528_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('education_table_change', 'education_table_change'), ('education_list_delete', 'education_list_delete'), ('education_list_save', 'education_list_save'))},
        ),
    ]
