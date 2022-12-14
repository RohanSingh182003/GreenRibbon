# Generated by Django 4.1 on 2022-08-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_psychomotor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Psychomotor1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q6', models.TextField()),
                ('q7', models.TextField()),
                ('q8', models.TextField()),
                ('q9a', models.TextField()),
                ('q9b', models.TextField()),
                ('q9c', models.TextField()),
                ('q10a', models.TextField()),
                ('q10b', models.TextField()),
                ('q10c', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Psychomotor2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q11a', models.TextField()),
                ('q11b', models.TextField()),
                ('q11c', models.TextField()),
                ('q12a', models.TextField()),
                ('q12b', models.TextField()),
                ('q12c', models.TextField()),
                ('q13a', models.TextField()),
                ('q13b', models.TextField()),
                ('q13c', models.TextField()),
                ('q14a', models.TextField()),
                ('q14b', models.TextField()),
                ('q14c', models.TextField()),
            ],
        ),
    ]
