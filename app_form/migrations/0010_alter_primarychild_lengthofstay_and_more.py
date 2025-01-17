# Generated by Django 4.2.3 on 2023-12-12 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0009_alter_primarychild_middlename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarychild',
            name='lengthOfStay',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='primarychild',
            name='lengthOfStayType',
            field=models.CharField(blank=True, choices=[('Year/s', 'Year/s'), ('Month/s', 'Month/s'), ('Week/s', 'Week/s')], max_length=100, null=True),
        ),
    ]
