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

    melee = Unit.objects.filter(campaign=False)
    melee_normal = melee.filter(heroic=False, special=False)
    melee_heroic = melee.filter(heroic=True, special=False)
    melee_special = melee.filter(special=True)

    campaign = Unit.objects.filter(campaign=True)
    campaign_normal = campaign.filter(heroic=False, special=False)
    campaign_heroic = campaign.filter(heroic=True, special=False)
    campaign_special = campaign.filter(special=True)

    data = {
        'race': race,
        'melee': {
            'normal': melee_normal,
            'heroic': melee_heroic,
            'special': melee_special,
        },
        'campaign': {
            'normal': campaign_normal,
            'heroic': campaign_heroic,
            'special': campaign_special,
        }
    }

    return render(request, 'race_detail.html', data)


class UnitDetailView(DetailView):
    model = Unit
    template_name = 'unit_detail.html'
