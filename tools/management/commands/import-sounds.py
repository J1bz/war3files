from os import listdir
from os.path import join, isfile, isdir, basename, dirname

from django.core.management.base import BaseCommand
from django.core.files import File

from tools.apps import (
    RACE_ICONS, REPLACEABLE_ICONS_DIR, UNITS_MAPPING)
from tools.utils import cmd
from units.models import Race, Unit
from sounds.models import Sound


class Command(BaseCommand):
    help = """Import units sounds from a standard warcraft 3 mpq file tree"""

    def add_arguments(self, parser):
        parser.add_argument('-r', '--root', default='.',
                            help='Extracted mpq documents root')

    def handle(self, *args, **options):
        self.root = options['root']

        for r, r_root, r_icon in self.get_races():
            self.handle_race(r, r_icon)

            for u, u_root, u_icon, categories in self.get_units(r_root):
                self.handle_unit(r, u, u_icon, categories)

                for s, s_path in self.get_sounds(u_root):
                    self.handle_sound(r, u, s_path)

    def get_races(self):
        units_root = join(self.root, 'Units')

        for race in listdir(units_root):
            race_root = join(units_root, race)
            if not isdir(race_root):
                continue

            icon_file = RACE_ICONS.get(race, None)
            if icon_file is None:
                self.stdout.write(
                    "{} race icon not found : using a question mark instead".
                    format(race))
                icon_path = self.get_question_mark_path()
            else:
                icon_path = join(self.root, icon_file)

            yield race, race_root, icon_path

    def get_question_mark_path(self):
        return join(self.root, REPLACEABLE_ICONS_DIR, 'BTNSelectHeroOn.blp')

    def get_units(self, race_root):
        for unit in listdir(race_root):
            categories = self.get_categories(unit)

            unit_root = join(race_root, unit)
            if not isdir(unit_root):
                continue

            icon_path = self.get_unit_icon_path(unit)

            yield unit, unit_root, icon_path, categories

    def get_categories(self, unit):
        return UNITS_MAPPING.get(unit, {}).get('categorization', ())

    def get_unit_icon_path(self, unit):
        if not hasattr(self, 'buttons'):
            self.buttons = join(self.root, REPLACEABLE_ICONS_DIR)
        buttons = self.buttons

        icon_path = join(buttons, 'BTN{}.blp'.format(unit))
        if not isfile(icon_path):
            replace = UNITS_MAPPING.get(unit, {}).get('replaceable_icon', None)
            if replace is None:
                self.stdout.write(
                    "{} not found for unit {} and its replaceable "
                    "icon is not defined : using a question mark instead".
                    format(icon_path, unit))

                return self.get_question_mark_path()

            replaceable_icon = join(REPLACEABLE_ICONS_DIR,
                                    'BTN{}.blp'.format(replace))

            icon_path = join(self.root, replaceable_icon)
            if not isfile(icon_path):
                self.stdout.write(
                    "Unit {} has no icon and its replaceable icon {} "
                    "is not a file : using a question mark instead".
                    format(unit, icon_path))

                return self.get_question_mark_path()

        return icon_path

    def get_sounds(self, unit_root):
        for sound in listdir(unit_root):
            sound_path = join(unit_root, sound)
            if not isfile(sound_path) or sound_path[-4:] != '.wav':
                continue

            yield sound, sound_path

    def handle_race(self, race, icon):
        icon_dir = dirname(icon)
        cmd('BLPConverter', '--format', 'png', '--dest', icon_dir, icon)

        png_icon = icon[:-4] + '.png'

        with open(png_icon, 'rb') as fh:
            i = File(fh)
            Race.objects.get_or_create(
                name=race,
                icon=i,
            )

    def beautiful_name(self, name):
        beautiful_name = name[0]
        for letter in name[1:]:
            if letter.isupper():
                beautiful_name += ' ' + letter.lower()
            else:
                beautiful_name += letter

        return beautiful_name

    def handle_unit(self, race, unit, icon, categories):
        icon_dir = dirname(icon)
        cmd('BLPConverter', '--format', 'png', '--dest', icon_dir, icon)

        png_icon = icon[:-4] + '.png'

        heroic = True if 'heroic' in categories else False
        special = True if 'special' in categories else False
        campaign = True if 'campaign' in categories else False

        r = Race.objects.get(name=race)
        with open(png_icon, 'rb') as fh:
            i = File(fh)
            Unit.objects.get_or_create(
                name=self.beautiful_name(unit),
                race=r,
                icon=i,
                heroic=heroic,
                special=special,
                campaign=campaign,
            )

    def handle_sound(self, race, unit, sound):
        r = Race.objects.get(name=race)
        u = Unit.objects.get(name=self.beautiful_name(unit), race=r)

        name = basename(sound)[:-4]

        with open(sound, 'rb') as fh:
            s = File(fh)
            Sound.objects.get_or_create(
                name=name,
                unit=u,
                audio=s,
            )
