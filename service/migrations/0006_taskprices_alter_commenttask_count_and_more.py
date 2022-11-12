# Generated by Django 4.1.3 on 2022-11-11 16:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_remove_reactionstask_count_post_pday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskPrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription', models.IntegerField()),
                ('views', models.IntegerField()),
                ('reaction', models.IntegerField()),
                ('comment', models.IntegerField()),
                ('vote', models.IntegerField()),
                ('repost', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Цены за накрутку',
                'verbose_name_plural': 'Цены за накрутку',
            },
        ),
        migrations.AlterField(
            model_name='commenttask',
            name='count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Количество должно быть положительным числом')], verbose_name='количество на пост'),
        ),
        migrations.AlterField(
            model_name='commenttask',
            name='link_post',
            field=models.URLField(verbose_name='ссылка на пост'),
        ),
        migrations.AlterField(
            model_name='reactionstask',
            name='count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Количество должно быть положительным числом')], verbose_name='количество на пост'),
        ),
        migrations.AlterField(
            model_name='reposttask',
            name='count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Количество должно быть положительным числом')], verbose_name='количество на пост'),
        ),
        migrations.AlterField(
            model_name='reposttask',
            name='count_posts',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1, message='Количетсво публикаций должно быть положительным числом')], verbose_name='кол-во публикаций'),
        ),
        migrations.AlterField(
            model_name='subscriptiontask',
            name='count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Количество должно быть положительным числом')], verbose_name='количество на пост'),
        ),
        migrations.AlterField(
            model_name='viewtask',
            name='count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Количество должно быть положительным числом')], verbose_name='количество на пост'),
        ),
        migrations.AlterField(
            model_name='viewtask',
            name='count_posts',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1, message='Количетсво публикаций должно быть положительным числом')], verbose_name='кол-во публикаций'),
        ),
        migrations.AlterField(
            model_name='votingtask',
            name='count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Количество должно быть положительным числом')], verbose_name='количество на пост'),
        ),
        migrations.AlterField(
            model_name='votingtask',
            name='link_post',
            field=models.URLField(verbose_name='ссылка на пост'),
        ),
    ]