from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.cat_page),
    path('updateCat/',views.updateCat),
    path('remove_cat/',views.remove_cat),
]