from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Clothe


# Create your views here.

class ClotheListView(ListView):
    model = Clothe
    paginate_by = 8

    def get_filter_param(self):
        # Grab the absolute url and then retrieve the filter param
        filter_param = self.request.path.split("/")[-1]
        return filter_param

    def get_queryset(self):
        default_order = "cloth_name"
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

        order_by = order_param or default_order
        # End of sorting code

        filter_param = self.get_filter_param()

        if(filter_param != ""):
            if(user_filter != ""):
                queryset = self.model.objects.filter(
                    cloth_gender=filter_param, cloth_category=user_filter)
            else:
                queryset = self.model.objects.filter(
                    cloth_gender=filter_param)
        else:
            queryset = self.model.objects.all()

        return queryset.order_by(order_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ClotheDetailView(DetailView):
    model = Clothe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
