# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import draceditor.models


class Migration(migrations.Migration):

    replaces = [('core', '0001_initial'), ('core', '0002_auto_20170903_1624'), ('core', '0003_auto_20170903_1729'), ('core', '0004_auto_20170903_1808'), ('core', '0005_auto_20170903_1815')]

    initial = True
    atomic = False

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.ImageField(upload_to='')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Images',
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('summary', models.CharField(blank=True, max_length=255, null=True, verbose_name='Общее')),
                ('body', draceditor.models.DraceditorField(verbose_name='История')),
                ('created_at', models.DateTimeField(verbose_name='Создано в')),
                ('published_at', models.DateTimeField(verbose_name='Опубликовано в')),
                ('uuid', models.UUIDField(blank=True, null=True, unique=True, verbose_name='UUID')),
                ('url_slug', models.CharField(max_length=150, unique=True, verbose_name='URL')),
                ('lang', models.PositiveSmallIntegerField(choices=[(1, 'Rus'), (2, 'Eng')], default=1, verbose_name='Язык')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('is_page', models.BooleanField(default=False, verbose_name='Отдельная страница?')),
                ('head_image', models.ForeignKey(blank=True, db_column='head_image_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Image', verbose_name='Картинка к посту')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'db_table': 'posts',
                'ordering': ('-published_at',),
            },
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.RenameField(
            model_name='image',
            old_name='preview',
            new_name='webp',
        ),
        migrations.AlterField(
            model_name='image',
            name='origin',
            field=models.ImageField(upload_to='p_img/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='webp',
            field=models.ImageField(blank=True, null=True, upload_to='p_img/%Y/%m/%d/'),
        ),
        migrations.RenameModel(
            old_name='Image',
            new_name='PostImage',
        ),
        migrations.AlterModelOptions(
            name='postimage',
            options={'verbose_name': 'Картинка к посту', 'verbose_name_plural': 'Картинки к постам'},
        ),
    ]
