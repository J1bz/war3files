from django.contrib import admin
from django.utils.html import format_html
from units.models import Race, RaceForm, Unit, UnitForm


class RaceAdmin(admin.ModelAdmin):
    form = RaceForm
    list_display = ('name',)
    search_fields = ('name',)


class UnitAdmin(admin.ModelAdmin):
    form = UnitForm
    list_display = ('show_icon', 'name', 'race', 'building', 'heroic',)
    search_fields = ('name', 'race__name',)

    def show_icon(self, obj):
        return format_html("<img src='{0}' alt='{0}'>".
                           format(obj.icon.url, obj.icon.name))

admin.site.register(Race, RaceAdmin)
admin.site.register(Unit, UnitAdmin)
