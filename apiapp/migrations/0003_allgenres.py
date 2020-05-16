# Generated by Django 2.2.1 on 2020-05-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_apisearch'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllGenres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_tmdb_id', models.CharField(blank=True, max_length=10, null=True)),
                ('genre_name', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]