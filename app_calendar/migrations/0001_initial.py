# Generated by Django 3.1.12 on 2025-01-17 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('isFinished', models.BooleanField(default=False)),
            ],
        ),
    ]
