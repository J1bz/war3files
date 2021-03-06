from os.path import basename

from django.db.models import (
    Model, CharField, ForeignKey, BooleanField, ImageField, FileField,
    SlugField, CASCADE)
from django.forms import ModelForm

from units.storage import OverwriteStorage


class Race(Model):
    name = CharField(max_length=32)
    slug = SlugField(unique=True, max_length=32)
    icon = ImageField(
        max_length=128,
        upload_to='race_icons',
        storage=OverwriteStorage(),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ('name', 'slug', 'icon',)


class Unit(Model):
    name = CharField(max_length=64)
    slug = SlugField(unique=True, max_length=64)
    race = ForeignKey(Race, on_delete=CASCADE)
    icon = ImageField(
        max_length=128,
        upload_to='icons',
        storage=OverwriteStorage(),
        null=True,
        blank=True
    )
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
            'slug',
            'race',
            'icon',
            'building',
            'heroic',
            'special',
            'campaign',
        )


class Sound(Model):
    name = CharField(max_length=64)
    slug = SlugField(unique=True, max_length=64)
    unit = ForeignKey(Unit, on_delete=CASCADE)
    audio = FileField(
        max_length=128,
        upload_to='sounds',
        storage=OverwriteStorage()
    )

    def __str__(self):
        return '{} {}'.format(self.unit.name, basename(self.audio.name))


class SoundForm(ModelForm):
    class Meta:
        model = Sound
        fields = ('name', 'slug', 'unit', 'audio',)
