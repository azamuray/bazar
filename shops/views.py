from django.shortcuts import render

from .models import Shop

def shops(request):
	shop_list = {
		'shops': Shop.objects.all()
	}
	return render(request, 'shops/shops.html', shop_list)