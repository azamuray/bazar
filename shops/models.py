from django.db import models
from django.conf import settings


class Shop(models.Model):
	seller = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Продавец")
	name = models.CharField("Название", max_length=120)
	address = models.CharField("Адрес", max_length=200)
	phone = models.CharField("Телефон", max_length=30)

	class Meta:
		verbose_name = 'магазин'
		verbose_name_plural = 'Магазины'

	def __str__(self):
		return self.name