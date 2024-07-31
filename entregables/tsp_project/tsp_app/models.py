# tsp_app/models.py
from django.db import models

class RouteResult(models.Model):
    num_nodes = models.IntegerField()
    weight_min = models.IntegerField()
    weight_max = models.IntegerField()
    start_node = models.IntegerField()
    tour = models.TextField()  # Guarda el recorrido como texto
    tour_cost = models.FloatField()
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return f"Resultado {self.id}: Costo {self.tour_cost}"
