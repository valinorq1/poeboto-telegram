from django.contrib import admin
from . import models

admin.site.register(models.ReactionPremium)
admin.site.register(models.ReactionAvailable)
admin.site.register(models.VotingTask)
admin.site.register(models.ViewTask)
admin.site.register(models.ReactionsTask)
admin.site.register(models.SubscriptionTask)
admin.site.register(models.CommentTask)

admin.site.register(models.TaskPrices)