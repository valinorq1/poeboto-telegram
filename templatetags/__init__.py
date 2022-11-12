from django import template

from service.models import TaskPrices

register = template.Library()

@register.simple_tag
def get_task_price(task):
	return getattr(TaskPrices.load(),task,None)

