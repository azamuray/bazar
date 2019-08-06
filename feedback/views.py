from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import View

from .forms import ContactForm


class ContactView(FormView):
	form_class = ContactForm
	template_name = 'feedback/contact.html'
	success_url = 'thanks/'

	def form_invalid(self, form):
		return super().form_invalid(form)

	def form_valid(self, form):
		form.send_email()
		return super().form_valid(form)


class ThanksView(View):
	template_name = 'feedback/thanks.html'

	def get(self, request):
		return render(request, self.template_name)