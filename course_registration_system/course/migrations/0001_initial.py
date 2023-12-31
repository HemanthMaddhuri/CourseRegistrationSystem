# Generated by Django 4.2.7 on 2023-11-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('instructor', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=30)),
                ('open_seats', models.IntegerField(default=30)),
            ],
        ),
    ]