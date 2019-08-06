from django.conf import settings
from django.core.mail import send_mail
from django import forms


class ContactForm(forms.Form):
	name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={"class": "form-control"}))
	sender = forms.CharField(label='Почтовый ящик', widget=forms.TextInput(attrs={"class": "form-control"}))
	text = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={"class": "form-control"}))

	def send_email(self):
		name = self.cleaned_data['name']
		sender = self.cleaned_data['sender']
		text = self.cleaned_data['text']
		message = f"""
			Имя: {name}
			Почтовый ящик: {sender}
			Сообщение: {text}
			"""
		send_mail(
			subject='Обратная связь',
			message=message,
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=['azamat.murdalov@mail.ru'],
			fail_silently=False,
		)

		answer = f"""
			Благодарим за обратную связь, {name}.
			Наш менеджер скоро с вами свяжется.

			Сообщение с торговой площадки Bazar
			"""
		send_mail(
			subject='Обратная связь',
			message=answer,
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[sender],
			fail_silently=False,
		)