from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('subscriptions/', views.SubscriptionTaskCreateView.as_view(), name='task-create-subscription'),
    path('views/', views.ViewTaskCreateView.as_view(), name='task-create-view'),
    path('views-sub/', views.ViewTaskCreateSubView.as_view(), name='task-create-view-sub'),
    path('reactions/', views.ReactionTaskCreateView.as_view(), name='task-create-reaction'),
    path('reactions-sub/', views.ReactionTaskCreateSubView.as_view(), name='task-create-reaction-sub'),
    path('comments/', views.CommentTaskCreateView.as_view(), name='task-create-comment'),
    path('voting/', views.VotingTaskCreateView.as_view(), name='task-create-voting'),
    path('voting-sub/', views.VotingTaskCreateSubView.as_view(), name='task-create-voting-sub'),
    path('reposts/', views.RepostTaskCreateView.as_view(), name='task-create-repost'),
    path('reposts-sub/', views.RepostTaskCreateSubView.as_view(), name='task-create-repost-sub')
]

urlpatterns.extend(staticfiles_urlpatterns())
