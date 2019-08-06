from django.urls import path

from .views import ContactView, ThanksView


app_name = 'feedback'
urlpatterns = [
	path('', ContactView.as_view(), name='contact'),
	path('thanks/', ThanksView.as_view(), name='thanks'),
]