from django.shortcuts import render
from django.views import generic
from django.conf import settings
from .models import Restaurant 
from django.contrib.gis.geos import Polygon
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.utils.decorators import method_decorator


class HomePage(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurants/homepage.html', {'GOOGLEAPIKEY':settings.GOOGLEAPIKEY})


@method_decorator(csrf_exempt, name='dispatch')
class ResturantsInMap(generic.View):
    def post(self, request, *args, **kwargs):
        s_lat = request.POST.get('s_lat', None)
        s_lng = request.POST.get('s_lng', None)
        n_lat = request.POST.get('n_lat', None)
        n_lng = request.POST.get('n_lng', None)
        rectangle = (s_lng, s_lat, n_lng, n_lat)
        geometry = Polygon.from_bbox(rectangle)
        queryset = Restaurant.objects.filter(coordinates__contained=geometry)
        restaurants = []
        index = 0
        for rest in queryset:
            restaurants.append([rest.name, rest.coordinates.y, rest.coordinates.x, index])
            index = index + 1
        return JsonResponse({"restaurants": restaurants})
    