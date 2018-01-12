from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation
from .forms import RestaurantCreateForm

# Create your views here.

def restaurant_createview(request):
    print(request.GET)
    print(request.POST)

    if request.method == "POST":
        print("post data")
        print(request.POST)
        title = request.POST.get("title")
        location = request.POST.get("location")
        category = request.POST.get("category")

        obj = RestaurantLocation.objects.create(
            name=title,
            location=location,
            category=category

        )
        return HttpResponseRedirect("/restaurants/")

    if request.method == "GET":
        print("get data")



    template_name = 'restaurants/form.html'
    queryset = RestaurantLocation.objects.all()
    context = {}
    return render(request, template_name, context)

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

class RestaurantListView(ListView):

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()
    print(queryset)

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id) #pk = rest_id
    #     return obj

