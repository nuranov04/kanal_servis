from django.views.generic import ListView

from main.models import Order


class OrderListView(ListView):
    model = Order
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_list'] = Order.objects.all()
        return context

