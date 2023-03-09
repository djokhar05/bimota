from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from delivery.form import DeliveryForm
from .models import Delivery
from django.views.generic.edit import CreateView
from django.template.loader import render_to_string


from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.


class DeliveryFormView(CreateView):
    form_class = DeliveryForm
    template_name = "delivery/delivery_form.html"
    # success_url = reverse_lazy("order_complete")

    def form_valid(self, form):
        # print(form.cleaned_data)
        # self.send_mail(form.cleaned_data)
        return super(DeliveryFormView, self).form_valid(form)


# "pk": self.pk, "name": self.name, "email": self.email, "address": self.address, "items": self.items, "phone": self.phone

def OrderCompleted(request, pk):
    obj = Delivery.objects.filter(id=pk).values()
    order_details = obj[0]
    context = {'pk': pk}

    # print(context)
    # Generate an order number
    # save the order number to the database along with
    # order name, ordered items, total price

    subject = "BIMOTA - Order Confirmaton"
    message = render_to_string(
        'delivery/order_conf.html', {'name': order_details['name'], 'orderNo': pk, 'phone': order_details['phone'], 'address': order_details['address'], 'items': order_details['items']})
    mail_from = 'support@bimota.com.ng'
    recipient = [order_details['email'], 'orders@bimota.com.ng']

    email = EmailMessage(subject, message, mail_from, recipient)
    email.content_subtype = "html"
    # res = email.send()
    # return HttpResponse('%s' % res)

    return render(request, "delivery/success.html", context)
