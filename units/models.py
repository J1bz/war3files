from django.db.models import (
    Model, CharField, ForeignKey, BooleanField, ImageField)
from django.forms import ModelForm


class Race(Model):
    name = CharField(max_length=32)
    icon = ImageField(upload_to='race_icons', null=True, blank=True)

    def __str__(self):
        return self.name


class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ('name', 'icon',)


class Unit(Model):
    name = CharField(max_length=64)
    race = ForeignKey(Race)
    icon = ImageField(upload_to='icons', null=True, blank=True)
    building = BooleanField(default=False)
    heroic = BooleanField(default=False)
    special = BooleanField(default=False)
    campaign = BooleanField(default=False)

    def __str__(self):
        return self.name


class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = (
            'name',
            'race',
            'icon',
            'building',
            'heroic',
            'special',
            'campaign',
        )
