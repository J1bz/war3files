from django.contrib import admin
from django.utils.html import format_html
from units.models import Race, RaceForm, Unit, UnitForm, Sound, SoundForm


class RaceAdmin(admin.ModelAdmin):
    form = RaceForm
    list_display = ('show_icon', 'name',)
    search_fields = ('name',)

    def show_icon(self, obj):
        return format_html("<img src='{0}' alt='{0}'>".
                           format(obj.icon.url, obj.icon.name))


class UnitAdmin(admin.ModelAdmin):
    form = UnitForm
    list_display = (
        'show_icon',
        'name',
        'race',
        'building',
        'heroic',
        'special',
        'campaign',
    )
    search_fields = ('name', 'race__name',)

    def show_icon(self, obj):
        return format_html("<img src='{0}' alt='{0}'>".
                           format(obj.icon.url, obj.icon.name))


class SoundAdmin(admin.ModelAdmin):
    form = SoundForm
    list_display = ('name', 'unit', 'audio',)
    search_fields = ('name', 'unit__name', 'unit__race__name',)


admin.site.register(Race, RaceAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Sound, SoundAdmin)
