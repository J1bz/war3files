from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from units.models import Race, Unit


class RaceListView(ListView):
    model = Race
    template_name = 'race_list.html'


def race_detail_view(request, pk):
    try:
        race = Race.objects.get(pk=pk)
    except Race.DoesNotExist:
        raise Http404('Race does not exist')

    melee = Unit.objects.filter(race=race, campaign=False)
    melee_units = melee.filter(heroic=False, special=False)
    melee_heroes = melee.filter(heroic=True, special=False)
    melee_special = melee.filter(special=True)

    campaign = Unit.objects.filter(race=race, campaign=True)
    campaign_units = campaign.filter(heroic=False, special=False)
    campaign_heroes = campaign.filter(heroic=True, special=False)
    campaign_special = campaign.filter(special=True)

    data = {
        'race': race,
        'melee': {
            'units': melee_units,
            'heroes': melee_heroes,
            'special': melee_special,
        },
        'campaign': {
            'units': campaign_units,
            'heroes': campaign_heroes,
            'special': campaign_special,
        }
    }

    return render(request, 'race_detail.html', data)


class UnitDetailView(DetailView):
    model = Unit
    template_name = 'unit_detail.html'
