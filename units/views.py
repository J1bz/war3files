from django.views.generic import ListView, DetailView

from units.models import Race, Unit


class RaceListView(ListView):
    model = Race
    template_name = 'race_list.html'


class RaceDetailView(DetailView):
    model = Race
    template_name = 'race_detail.html'


class UnitDetailView(DetailView):
    model = Unit
    template_name = 'unit_detail.html'
