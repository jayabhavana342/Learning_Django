from django.urls import path

from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView
)

app_name = 'restaurants'

urlpatterns = [
    path('', RestaurantListView.as_view(), name='list'),
    path('create/', RestaurantCreateView.as_view(), name='create'),
    # path('<slug:slug>/', RestaurantDetailView.as_view(), name="detail"),
    path('<slug:slug>/edit', RestaurantUpdateView.as_view(), name="detail"),
]
