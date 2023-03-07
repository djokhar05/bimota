from django.shortcuts import render
from django.urls import reverse_lazy
from contact.form import ContactForm
from django.views.generic import FormView


from django.core.mail import EmailMessage
from django.http import HttpResponse


# Create your views here.


# def contact(request):
#     context = {
#         "route": "Contact",
#         "route_text": "Reach out to us for enquiries and suggestions and complaints"
#     }
#     return render(request, 'contact/contact.html', context)


class ContactFormView(FormView):
    context = {
        "route": "Contact",
        "route_text": "Reach out to us for enquiries and suggestions and complaints"
    }

    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        print(form.cleaned_data)
        self.send_mail(form.cleaned_data)
        return super(ContactFormView, self).form_valid(form)

    def send_mail(self, valid_data):
        subject = valid_data['subject']
        message = valid_data['message']
        mail_from = valid_data['email']
        recipient = ['daniel-strong@live.com']
        # send_mail(subject, message, mail_from, recipient)

        email = EmailMessage(subject, message, mail_from, recipient)
        email.content_subtype = "html"
        res = email.send()
        return HttpResponse('%s' % res)
