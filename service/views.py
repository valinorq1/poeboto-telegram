from django.views import generic

from .views_mixins import CreateTaskMixin, CreateTaskSubMixin
from . import forms
from . import models


class HomeView(generic.TemplateView):
    template_name = 'service/home.html'

class AboutView(generic.TemplateView):
    template_name = 'service/about.html'


class SubscriptionTaskCreateView(CreateTaskMixin):
    form_class = forms.SubscriptionsForm
    template_name = 'service/subscriptions.html'
    class Meta:
        model = models.SubscriptionTask


class ViewTaskCreateView(CreateTaskMixin):
    form_class = forms.ViewsForm
    template_name = 'service/views.html'
    class Meta:
        model = models.ViewTask
class ViewTaskCreateSubView(CreateTaskSubMixin,ViewTaskCreateView):
    form_class = forms.ViewsSubForm


class ReactionTaskCreateView(CreateTaskMixin):
    template_name = 'service/reactions.html'
    form_class = forms.ReactionsForm
    class Meta:
        model = models.ReactionsTask
class ReactionTaskCreateSubView(CreateTaskSubMixin,ReactionTaskCreateView):
    form_class = forms.ReactionsSubForm


class CommentTaskCreateView(CreateTaskMixin):
    template_name = 'service/comments.html'
    form_class = forms.CommentsForm
    class Meta:
        model = models.CommentTask


class VotingTaskCreateView(CreateTaskMixin):
    template_name = 'service/voting.html'
    form_class = forms.VotingForm
    class Meta:
        model = models.VotingTask
class VotingTaskCreateSubView(CreateTaskSubMixin,VotingTaskCreateView):
    form_class = forms.VotingSubForm


class RepostTaskCreateView(CreateTaskMixin):
    template_name = 'service/reposts.html'
    form_class = forms.RepostsForm
    class Meta:
        model = models.RepostTask
class RepostTaskCreateSubView(CreateTaskSubMixin,RepostTaskCreateView):
    form_class = forms.RepostsSubForm
