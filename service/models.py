from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.db import models

from core import validators

from . import models_abstract
from .models_abstract import (
    Task,
    TaskSubscriptionMixin ,
    TaskDurationMixin,
    TaskToStartMixin,
    TaskChannelMixin,
    TaskMultiplePostMixin,
    TaskSinglePostMixin
)

GENDERS = [
    ('random', 'Случайно'),
    ('male', 'Мужской'),
    ('female', 'Женский'),
]

PREFIX_VERBOSE_NAME = 'задача ({name})'
PREFIX_VERBOSE_NAME_PLURAL = 'задачи ({name})'

User = get_user_model()

task_customer = lambda related_name : models.ForeignKey(verbose_name='Заказчик',to=User, related_name=related_name, on_delete=models.CASCADE, to_field='email')


class TaskPrices(models_abstract.SingletonModel):
    subscription = models.FloatField('Цена за подписку',default=0)
    view = models.FloatField('Цена за просмотр',default=0)
    view_sub = models.FloatField('Цена за автопросмотр',default=0)
    reaction = models.FloatField('Цена за реакцию',default=0)
    reaction_sub = models.FloatField('Цена за автореакцию',default=0)
    comment = models.FloatField('Цена за комментарий',default=0)
    vote = models.FloatField('Цена за голосование',default=0)
    repost = models.FloatField('Цена за репост',default=0)
    class Meta:
        verbose_name = 'Цены за накрутку'
        verbose_name_plural = 'Цены за накрутку'


class SubscriptionTask(
    TaskChannelMixin,
    TaskDurationMixin,
    TaskToStartMixin,
    Task
):
    customer = task_customer('tasks_subscriptions')
    read_last_posts = models.BooleanField('чтение последних публикаций', default=False)
    gender = models.CharField('предпочтительный пол', default="random", choices=GENDERS, max_length=120)
    class Meta:
        verbose_name = PREFIX_VERBOSE_NAME.format(name='подписки')
        verbose_name_plural = PREFIX_VERBOSE_NAME_PLURAL.format(name='подписки')


class ViewTask(
    TaskChannelMixin,
    TaskSubscriptionMixin,
    TaskDurationMixin,
    TaskToStartMixin,
    Task
):
    customer = task_customer('tasks_views')
    view_as_sub = models.BooleanField('читать подписчиками', default=False)
    spread = models.BooleanField('разброс (5%)', default=False)
    class Meta:
        verbose_name = PREFIX_VERBOSE_NAME.format(name='просмотры')
        verbose_name_plural = PREFIX_VERBOSE_NAME_PLURAL.format(name='просмотры')


class ReactionAvailable(models_abstract.Reaction):    
    class Meta:
        verbose_name = 'реакция'
        verbose_name_plural = 'реакции'

class ReactionPremium(models_abstract.Reaction):
    class Meta:
        verbose_name = 'премиум реакция'
        verbose_name_plural = 'премиум реакции'

class ReactionsTask(
    TaskChannelMixin,
    TaskMultiplePostMixin,
    TaskSubscriptionMixin,
    TaskDurationMixin,
    Task
):
    customer = task_customer('tasks_reactions')
    count_posts = models.IntegerField('количество последних публикаций', null=True, blank=True)
    spread = models.BooleanField('разброс (5%)', default=False)
    link_post = models.URLField('ссылка на публикацию')
    reactions = models.ManyToManyField(ReactionAvailable, verbose_name='реакции')    
    reactions_premium = models.ManyToManyField(ReactionPremium, verbose_name='премиум реакции')
    class Meta:
        verbose_name = PREFIX_VERBOSE_NAME.format(name='реакции')
        verbose_name_plural = PREFIX_VERBOSE_NAME_PLURAL.format(name='реакции')


class CommentTask(
    TaskSinglePostMixin,
    Task
):
    customer = task_customer('tasks_comments')
    comments = models.TextField('комментарии (каждый с новой строки)')
    class Meta:
        verbose_name = PREFIX_VERBOSE_NAME.format(name='комментарии')
        verbose_name_plural = PREFIX_VERBOSE_NAME_PLURAL.format(name='комментарии')


class VotingTask(
    TaskChannelMixin,
    TaskSinglePostMixin,
    TaskSubscriptionMixin,
    TaskDurationMixin,
    TaskToStartMixin,
    Task
):
    customer = task_customer('tasks_voting')
    count_posts = models.IntegerField('количество последних публикаций', null=True, blank=True)
    spread = models.BooleanField('разброс (5%)', default=False)
    number_button = models.IntegerField('Порядковый № кнопки',validators=[MinValueValidator(0,message = 'Номер кнопки не может быть отрицательным')],default=0)
    class Meta:
        verbose_name = PREFIX_VERBOSE_NAME.format(name='голосование')
        verbose_name_plural = PREFIX_VERBOSE_NAME_PLURAL.format(name='голосование')


class RepostTask(
    TaskChannelMixin,
    TaskSinglePostMixin,
    TaskSubscriptionMixin,
    Task
):
    customer = task_customer('tasks_reposts')
    link_post = models.URLField('ссылка на публикацию')    
    class Meta:
        verbose_name = PREFIX_VERBOSE_NAME.format(name='репосты')
        verbose_name_plural = PREFIX_VERBOSE_NAME_PLURAL.format(name='репосты')