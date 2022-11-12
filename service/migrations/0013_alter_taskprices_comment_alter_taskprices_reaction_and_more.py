# Generated by Django 4.1.3 on 2022-11-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_alter_taskprices_comment_alter_taskprices_reaction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskprices',
            name='comment',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3, verbose_name='Цена за комментарий'),
        ),
        migrations.AlterField(
            model_name='taskprices',
            name='reaction',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3, verbose_name='Цена за реакцию'),
        ),
        migrations.AlterField(
            model_name='taskprices',
            name='reaction_sub',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3, verbose_name='Цена за автореакцию'),
        ),
        migrations.AlterField(
            model_name='taskprices',
            name='repost',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3, verbose_name='Цена за репост'),
        ),
        migrations.AlterField(
            model_name='taskprices',
            name='subscription',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3, verbose_name='Цена за подписку'),
        ),
        migrations.AlterField(
            model_name='taskprices',
            name='view',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3, verbose_name='Цена за просмотр'),
        ),
        migrations.AlterField(
            model_name='taskprices',
            name='view_sub',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3, verbose_name='Цена за автопросмотр'),
        ),
        migrations.AlterField(
            model_name='taskprices',
            name='vote',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3, verbose_name='Цена за голосование'),
        ),
    ]
