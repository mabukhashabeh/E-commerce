from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='items'),
    path('category/<slug>', views.category_list, name='category'),
    path('product/<slug>/', views.ItemDetalView.as_view(), name='product'),
    path('add-to-cart/<slug>', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', views.remove_from_cart, name='remove-from-cart'),

]