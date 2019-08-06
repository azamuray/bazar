from django.conf import settings
from django.core.mail import send_mail
from django import forms


class ContactForm(forms.Form):
	name = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)

	def send_email(self):
		password = self.cleaned_data['name']
		message = f'Ваш логин: {password}'
		send_mail(
			subject='Проверка формы',
			message=message,
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=['azamat.murdalov@mail.ru'],
			fail_silently=False,
		)