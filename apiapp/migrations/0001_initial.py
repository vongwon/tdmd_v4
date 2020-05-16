# Generated by Django 3.0.5 on 2020-04-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actorid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('photo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('year', models.CharField(blank=True, max_length=4)),
                ('length', models.CharField(blank=True, max_length=10)),
                ('genres', models.CharField(blank=True, max_length=100)),
                ('rate', models.IntegerField(blank=True, default=0)),
                ('poster', models.URLField(blank=True, default='')),
                ('plot', models.CharField(blank=True, max_length=500)),
                ('trailer', models.URLField(blank=True, default='')),
            ],
        ),
    ]