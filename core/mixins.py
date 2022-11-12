from typing import Tuple, Dict, List

from django.http.request import HttpRequest
from django.http.response import HttpResponse


class AddClassNameMixin:
  '''
  Mixin to add html classes to form fields
  Usable for both Form and FilterSet(django_filters) objects
  '''
  class_name: str = 'form-control w-100'
  class_name__checkbox: str = 'form-check-input mb-3'
  not_modify_fields: List[str] = []

  def __init__(self, *args: Tuple, **kwargs: Dict):
    result = super().__init__(*args, **kwargs)
    form = self if hasattr(self,'visible_fields') else self.form

    for field in filter(lambda field: field.name not in self.not_modify_fields, form.visible_fields()):
      if field.widget_type == 'checkbox':
        field.field.widget.attrs['class'] = self.class_name__checkbox
      else:
        field.field.widget.attrs['class'] = self.class_name

    return result
