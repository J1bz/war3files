from django.contrib import admin
from units.models import Race, RaceForm, Unit, UnitForm


class RaceAdmin(admin.ModelAdmin):
    form = RaceForm
    list_display = ('name',)
    search_fields = ('name',)


class UnitAdmin(admin.ModelAdmin):
    form = UnitForm
    list_display = ('name', 'race', 'icon', 'building', 'heroic',)
    search_fields = ('name', 'race__name',)

admin.site.register(Race, RaceAdmin)
admin.site.register(Unit, UnitAdmin)
