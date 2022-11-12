from django import forms

from . import models
from .forms_mixins import CreateTaskFormMixin, CreateTaskFormMeta


class SubscriptionsForm(CreateTaskFormMixin):
    class Meta(CreateTaskFormMeta):
        model = models.SubscriptionTask
        fields = (
            'link_channel',
            'gender',
            'count',
            'to_start',
            'duration',
            'duration_value',
            'quick',
            'read_last_posts',
        )
        labels = {
            'duration':'Продолжительность добавления подписчиков',
        }



class ViewsForm(CreateTaskFormMixin):
    class Meta(CreateTaskFormMeta):
        labels = {
            'count': 'Количество просмотров на пост',
            'spread': 'Разброс просмотров (-5%)',
            'duration': 'Продолжительность добавления просмотров',
            'count_posts': 'Укажите количество последних постов для накрутки',
        }
        model = models.ViewTask
        fields = (
            'link_channel',
            'count',
            'spread',
            'count_posts',
            'duration',
            'duration_value',
            'to_start',
            'quick',
            'view_as_sub'
        )


class ViewsSubForm(CreateTaskFormMixin):
    class Meta(CreateTaskFormMeta):
        model = models.ViewTask
        labels = {
            'count': 'Количество просмотров на пост',
            'count_posts': 'Среднее количество постов в сутки для просмотров',  
            'spread': 'Разброс просмотров (-5%)',
            'duration': 'Продолжительность добавления просмотров'
        }
        fields = (
            'link_channel',
            'duration_sub',
            'count_posts',
            'count',
            'spread',
            'duration',
            'duration_value',
            'to_start',
            'quick',
            'view_as_sub'
        )

class ReactionsForm(CreateTaskFormMixin):
    class Meta(CreateTaskFormMeta):
        model = models.ReactionsTask
        fields = (
            'link_post',
            'count',
            'duration',
            'duration_value',
            'reactions',
            'quick',
        )
        labels = {
            'duration': 'Продолжительность добавления реакций'
        }

class ReactionsSubForm(CreateTaskFormMixin):
    class Meta(CreateTaskFormMeta):
        model = models.ReactionsTask
        fields = (
            'link_channel',
            'duration_sub',
            'count_posts',
            'count',
            'spread',
            'duration',
            'duration_value',
            'reactions',
            'spread',
            'quick',
        )
        labels = {
            'duration': 'Продолжительность добавления реакций',
            'count_posts': 'Среднее количество постов в сутки для реакций'
        }


class CommentsForm(CreateTaskFormMixin):
    class Meta(CreateTaskFormMeta):
        model = models.CommentTask
        fields = (
            'link_post',
            'comments',
        )


class VotingForm(CreateTaskFormMixin):
    class Meta(CreateTaskFormMeta):
        model = models.VotingTask
        fields = (
            'link_channel',
            'link_post',
            'count',
            'number_button',
            'duration',
            'duration_value',
            'to_start',
            'quick',
        )
        labels = {
            'duration': 'Продолжительность добавления голосов',
        }

class VotingSubForm(CreateTaskFormMixin):
    class Meta(CreateTaskFormMeta):
        model = models.VotingTask
        fields = (
            'link_channel',
            'duration_sub',
            'count_posts',
            'count',
            'number_button',
            'duration',
            'duration_value',
            'to_start',
            'quick',
            'spread',
        )
        labels = {
            'count_posts': 'Среднее количество постов в сутки для голосования',
            'duration': 'Продолжительность добавления голосов',
        }


class RepostsForm(CreateTaskFormMixin):
    class Meta(CreateTaskFormMeta):
        model = models.RepostTask
        fields = {
            'link_post',
            'count',
        }

class RepostsSubForm(CreateTaskFormMixin):
    class Meta(CreateTaskFormMeta):
        model = models.RepostTask
        fields = {
            'link_channel',
            'count_posts',
            'duration_sub',
            'count',
        }
        labels = {
            'count_posts': 'Среднее количество постов в сутки для репостов',
        }

class LoginForm(CreateTaskFormMixin):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'flexCheckDefault'}), required=False)
