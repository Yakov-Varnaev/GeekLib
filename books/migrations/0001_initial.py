# Generated by Django 4.0.4 on 2022-04-20 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublishsingHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='publising house name')),
            ],
            options={
                'verbose_name': 'Publishing House',
                'verbose_name_plural': 'Publishing Houses',
                'db_table': 'publishing_houses',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='book name')),
                ('pub_date', models.DateField(verbose_name='Publishing Date')),
                ('author', models.TextField(verbose_name='author`s name')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.publishsinghouse', verbose_name='Publisher')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'books',
            },
        ),
    ]
