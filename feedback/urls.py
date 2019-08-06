from django.urls import path

from .views import ContactView, ThanksView


urlpatterns = [
	path('', ContactView.as_view(), name='feedback'),
	path('thanks/', ThanksView.as_view(), name='thanks'),
]