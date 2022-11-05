# Generated by Django 4.1.2 on 2022-10-28 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('urlToken', models.CharField(db_index=True, max_length=100)),
                ('pax', models.PositiveSmallIntegerField(default=1)),
                ('rsvp', models.BooleanField(default=None)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=254)),
                ('mobile', models.CharField(blank=True, db_index=True, max_length=32)),
                ('confirmedCompany', models.BooleanField(default=None)),
                ('vaccinationStatus', models.BooleanField(default=None)),
                ('allergies', models.CharField(blank=True, max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
