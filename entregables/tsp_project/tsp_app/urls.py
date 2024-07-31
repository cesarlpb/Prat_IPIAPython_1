from django.urls import path
from . import views

urlpatterns = [
    path('', views.tsp_view, name='tsp_view'),
    path('compare/', views.compare_results, name='compare_results'),
    path('delete_all/', views.delete_all_results, name='delete_all_results'),
]
