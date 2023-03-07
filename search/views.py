from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from clothe.models import Clothe


# Create your views here.

class SearchListView(ListView):
    model = Clothe
    paginate_by = 8
    template_name = "clothe/clothe_list.html"

    def get_filter_param(self):
        # Grab the absolute url and then retrieve the filter param
        filter_param = self.request.GET.get("filter")
        return filter_param

    def get_queryset(self):

        default_order = "cloth_price"
        order_param = ""
        user_filter = ""

        try:
            order_param = self.request.GET.get('ordering').strip()
        except:
            pass

        try:
            user_filter = self.request.GET.get('filter').strip()
        except:
            pass

        try:
            query = self.request.GET.get('query')
        except:
            pass

        order_by = order_param or default_order

        if(user_filter != ""):
            queryset = Clothe.objects.filter(
                cloth_name__icontains=query, cloth_category=user_filter)
        else:
            queryset = Clothe.objects.filter(cloth_name__icontains=query)

        if(order_param == ""):
            return queryset
        else:
            return queryset.order_by(order_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
