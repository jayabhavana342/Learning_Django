from django.urls import path

from .views import (
    ItemListView,
    ItemDetailView,
    ItemUpdateView,
    ItemCreateView
)

app_name = 'restaurants'

urlpatterns = [
    path('', ItemListView.as_view(), name='list'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('<int:pk>/', ItemDetailView.as_view(), name="detail"),
]
