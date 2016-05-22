from django.contrib import admin
from sounds.models import Sound, SoundForm


class SoundAdmin(admin.ModelAdmin):
    form = SoundForm
    list_display = ('name', 'unit', 'audio',)
    search_fields = ('name', 'unit__name', 'unit__race__name',)


admin.site.register(Sound, SoundAdmin)
