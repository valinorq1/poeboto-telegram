from django import forms

from core import validators
from core.mixins import AddClassNameMixin

class CreateTaskFormMixin(AddClassNameMixin,forms.ModelForm):
    def clean(self):
        if self.cleaned_data.get('to_start') and not validators.present_or_future_date(self.cleaned_data.get('to_start')):
            self._errors['to_start'] = self.error_class([
                'Дата начала должна быть актуальна по UTC.'])
        return self.cleaned_data

class CreateTaskFormMeta:
    widgets = {
        'to_start': forms.TextInput(attrs={'type':'datetime-local'})
    }
    help_texts = {
        'to_start': 'Опционально, если не нужно отложить задачу, то оставьте поле пустым. Дата начала должна быть актуальна.',
        'link_channel': 'Укажите ссылку на открытый/закрытый канал или группу. Изменять ссылку канала во время накрутки, запрещено!',
        'number_button': 'Если голосовать нужно в случайном порядке, укажите 0.',
        'comments': 'Только для открытых каналов и групп! При указании неверной ссылки (в т.ч. закрытом канале) отмена невозможна, деньги за заказ не возвращаются!'
    }
