from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy


class CreateTaskMixin(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    success_url = reverse_lazy('account-cart')
    success_message = 'Задание успешно создано. Спасибо что пользуетесь нашим сервисом!'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.instance.set_price()
        return super().form_valid(form)

class CreateTaskSubMixin(CreateTaskMixin):
    def form_valid(self, form):
        form.instance.subscription = True
        return super().form_valid(form)
