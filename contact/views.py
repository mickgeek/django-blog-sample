# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib import messages

from .forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'

    def get_success_url(self):
        return reverse('contact:contact')

    def form_valid(self, form):
        if form.send_email():
            messages.info(self.request, 'Thank you for your message. We will be in touch shortly.')
        else:
            messages.error(self.request, "We couldn't send your message. Please try again later.")
        return super(ContactView, self).form_valid(form)
