from django import forms

class TSPForm(forms.Form):
    num_nodes = forms.IntegerField(label='Número de ciudades', min_value=1)
    min_weight = forms.IntegerField(label='Peso mínimo del trayecto', min_value=1)
    max_weight = forms.IntegerField(label='Peso máximo del trayecto', min_value=1)
    start_node = forms.IntegerField(label='Número de inicio', min_value=0)