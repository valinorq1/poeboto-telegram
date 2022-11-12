from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator


User = get_user_model()


# TaskSubscriptionMixin 
# TaskDurationMixin
# TaskToStartMixin
# TaskChannelMixin
# TaskMultiplePostMixin
# TaskSinglePostMixin


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class TaskSubscriptionMixin(models.Model):
    subscription = models.BooleanField('подписка', default=False)
    duration_sub = models.IntegerField('длительность подписки',null=True,blank=True,validators=[MinValueValidator(2,message="Подписка оформляется на минимум 2 дня.")])
    count_posts = models.IntegerField('кол-во публикаций', null=True, validators=[MinValueValidator(1,message='Количетсво публикаций должно быть положительным числом')])
    @property
    def duration_sub_remainder(self):
        # TODO
        return False
    class Meta:
        abstract = True


class TaskDurationMixin(models.Model):
    DURATION_VALUES = [
        ('minute', 'МИНУТ'),
        ('hour', 'ЧАСОВ'),
    ]
    duration = models.IntegerField('продолжительность услуги')
    duration_value = models.CharField(default="minutes",choices=DURATION_VALUES, max_length=55)
    class Meta:
        abstract = True


class TaskToStartMixin(models.Model):
    to_start = models.DateTimeField('время начала (в UTC формате)',null=True,blank=True)
    class Meta:
        abstract = True


class TaskChannelMixin(models.Model):
    link_channel = models.URLField('ссылка на канал', max_length=120)
    class Meta:
        abstract = True


class TaskMultiplePostMixin(models.Model):
    link_posts = models.CharField('сылка на пост, номер поста или интервал постов',max_length=500)
    class Meta:
        abstract = True


class TaskSinglePostMixin(models.Model):
    link_post = models.URLField('ссылка на пост')
    class Meta:
        abstract = True


class Task(models.Model):
    count = models.IntegerField('количество на пост', validators=[MinValueValidator(1,message = 'Количество должно быть положительным числом')], default=1)
    count_done = models.IntegerField('выполненный объем', default=0)
    price = models.IntegerField('стоимость', default=0)    

    quick = models.BooleanField('максимальная скорость', default=False)

    viewed = models.BooleanField('просмотрен', default=False)
    done = models.BooleanField('обработан', default=False)
    created = models.DateTimeField('время создания', auto_now_add=True)

    class Meta:
        abstract = True


class Reaction(models.Model):
    name = models.CharField('эмоция',max_length=1,unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True