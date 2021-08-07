from django.urls import path
from .views import mark_favourite, FavouriteProductListView
urlpatterns = [
    path('', FavouriteProductListView.as_view(), name='favourite-products'),
    path('mark/<int:id>/', mark_favourite, name='mark-favourite'),
]
