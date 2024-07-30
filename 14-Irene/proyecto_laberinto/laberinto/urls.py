from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_maze/', views.generate_maze, name='generate_maze'),
    path('solve_maze/', views.solve_maze, name='solve_maze'),
]
