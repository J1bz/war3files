from os import listdir
from os.path import join, isfile, isdir, basename, dirname

from django.core.management.base import BaseCommand
from django.core.files import File
from django.template.defaultfilters import slugify

from tools.apps import (
    RACES_MAPPING, REPLACEABLE_ICONS_DIR, UNITS_MAPPING)
from tools.utils import cmd
from units.models import Race, Unit, Sound


class Command(BaseCommand):
    help = """Import units sounds from a standard warcraft 3 mpq file tree"""

    def add_arguments(self, parser):
        parser.add_argument('-r', '--root', default='.',
                            help='Extracted mpq documents root')

    def handle(self, *args, **options):
        self.root = options['root']

        for race, r_icon, r_root in self.get_races():
            for u_race, unit, u_root, u_icon, cats in self.get_units(r_root):
                real_race = u_race or race
                u = self.handle_unit(real_race, r_icon, unit, u_icon, cats)

                for sound, s_path in self.get_sounds(u_root):
                    self.handle_sound(u, s_path)

    def get_races(self):
        units_root = join(self.root, 'Units')

        for race in listdir(units_root):
            race_root = join(units_root, race)
            if not isdir(race_root):
                continue

            name = self.get_race_name(race)
            icon = self.get_race_icon_path(race)

            yield name, icon, race_root

    def get_race_name(self, race):
        name = RACES_MAPPING.get(race, {}).get('name', None)
        if name is None:
            self.stdout.write("{0} name not found : using '{0}' by default".
                              format(race))
            return race
        return name

    def get_race_icon_path(self, race):
        icon_file = RACES_MAPPING.get(race, {}).get('icon', None)
        if icon_file is None:
            self.stdout.write(
                "{} race icon not found : using a question mark instead".
                format(race))
            icon_path = self.get_question_mark_path()
        else:
            icon_path = join(self.root, icon_file)

        return icon_path

    def get_question_mark_path(self):
        return join(self.root, REPLACEABLE_ICONS_DIR, 'BTNSelectHeroOn.blp')

    def get_units(self, race_root):
        for unit in listdir(race_root):
            if self.is_unit_ignored(unit):
                continue

            race = self.get_unit_race(unit)
            name = self.get_unit_name(unit)
            categories = self.get_unit_categories(unit)

            unit_root = join(race_root, unit)
            if not isdir(unit_root):
                continue

            icon_path = self.get_unit_icon_path(unit)

            yield race, name, unit_root, icon_path, categories

    def is_unit_ignored(self, unit):
        return UNITS_MAPPING.get(unit, {}).get('ignore', False)

    def get_unit_race(self, unit):
        return UNITS_MAPPING.get(unit, {}).get('race', None)

    def get_unit_name(self, unit):
        custom_name = UNITS_MAPPING.get(unit, {}).get('name', None)
        return custom_name or self.beautiful_name(unit)

    def beautiful_name(self, name):
        beautiful_name = name[0]
        for letter in name[1:]:
            if letter.isupper():
                beautiful_name += ' '

            beautiful_name += letter

        return beautiful_name

    def get_unit_categories(self, unit):
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
        r, created = Race.objects.get_or_create(name=race)

        if created:
            # slugs are supposed to be unique, but a unique name implies a
            # unique slug in our case
            r.slug = slugify(race)

            icon_dir = dirname(icon)
            cmd('BLPConverter', '--format', 'png', '--dest', icon_dir, icon)

            png_icon = icon[:-4] + '.png'

            with open(png_icon, 'rb') as fh:
                i = File(fh)
                r.icon = i
                r.save()

        return r, created

    def handle_unit(self, race, race_icon, unit, icon, categories):
        icon_dir = dirname(icon)
        cmd('BLPConverter', '--format', 'png', '--dest', icon_dir, icon)

        png_icon = icon[:-4] + '.png'

        heroic = True if 'heroic' in categories else False
        special = True if 'special' in categories else False
        campaign = True if 'campaign' in categories else False

        r, created = self.handle_race(race, race_icon)

        with open(png_icon, 'rb') as fh:
            i = File(fh)
            u, created = Unit.objects.get_or_create(
                name=unit,
                slug=slugify(unit),
                race=r,
                icon=i,
                heroic=heroic,
                special=special,
                campaign=campaign,
            )

        return u

    def handle_sound(self, unit, sound):
        name = basename(sound)[:-4]

        with open(sound, 'rb') as fh:
            a = File(fh)
            s, created = Sound.objects.get_or_create(
                name=name,
                slug='{}-{}'.format(unit.slug, slugify(name)),
                unit=unit,
                audio=a,
            )

        return s
