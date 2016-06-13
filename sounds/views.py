from django.views.generic import ListView

from sounds.models import Sound


class SoundList(ListView):
    model = Sound
    template_name = 'sound_list.html'
