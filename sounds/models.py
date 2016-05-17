from os.path import basename

from django.db.models import Model, CharField, ForeignKey, FileField
from django.forms import ModelForm

from units.models import Unit


class Sound(Model):
    name = CharField(max_length=64)
    unit = ForeignKey(Unit)
    audio = FileField(upload_to='sounds')

    def __str__(self):
        return '{} {}'.format(self.unit.name, basename(self.audio.name))


class SoundForm(ModelForm):
    class Meta:
        model = Sound
        fields = ('name', 'unit', 'audio',)
