# Generated by Django 5.1 on 2024-08-29 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hundred_dollar', models.IntegerField(default=0)),
                ('fifty_dollar', models.IntegerField(default=0)),
                ('twenty_dollar', models.IntegerField(default=0)),
                ('ten_dollar', models.IntegerField(default=0)),
                ('five_dollar', models.IntegerField(default=0)),
                ('two_dollar', models.IntegerField(default=0)),
                ('one_dollar', models.IntegerField(default=0)),
                ('twenty_five_cent', models.IntegerField(default=0)),
                ('ten_cent', models.IntegerField(default=0)),
                ('five_cent', models.IntegerField(default=0)),
            ],
        ),
    ]
