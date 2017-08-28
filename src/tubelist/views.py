from django.shortcuts import render
from django.views import View
# Create your views here.

class MainView(View):
	
	def get(self, request, *args, **kwargs):
		# name = 'lager'
		# instance = get_object_or_404(BeerType, name__iexact=name)
		# print(instance.beertype_beers.all())
		context = {}
		return render(request, "index.html", context) 