from os import listdir
from os.path import join, isfile, isdir, basename, dirname

from django.core.management.base import BaseCommand
from django.core.files import File

from tools.apps import (
    RACE_ICONS, ICONS_DIR, CATEGORIZATION, REPLACEABLE_ICONS)
from tools.utils import cmd
from units.models import Race, Unit
from sounds.models import Sound


class Command(BaseCommand):
    help = """Import units sounds from a standard warcraft 3 mpq file tree"""

    def add_arguments(self, parser):
        parser.add_argument('-r', '--root', default='.',
                            help='Extracted mpq documents root')

    def handle(self, *args, **options):
        units_root = join(options['root'], 'Units')

        for race in listdir(units_root):
            race_root = join(units_root, race)
            if not isdir(race_root):
                continue

            race_icon_file = RACE_ICONS.get(
                race, join(ICONS_DIR, 'BTNSelectHeroOn.blp'))
            race_icon_path = join(options['root'], race_icon_file)
            self.handle_race(race, race_icon_path)

            for unit in listdir(race_root):
                categories = CATEGORIZATION.get(unit, ())

                unit_root = join(race_root, unit)
                if not isdir(unit_root):
                    continue

                buttons = join(options['root'], ICONS_DIR)
                icon_path = join(buttons, 'BTN{}.blp'.format(unit))
                if not isfile(icon_path):
                    equivalence = REPLACEABLE_ICONS.get(unit, None)
                    if equivalence is None:
                        self.stdout.write(
                            "{} not found for unit {} and its replaceable "
                            "icon is not defined".format(icon_path, unit))
                        continue

                    replaceable_icon = join(ICONS_DIR,
                                            'BTN{}.blp'.format(equivalence))

                    icon_path = join(options['root'], replaceable_icon)
                    if not isfile(icon_path):
                        self.stdout.write(
                            "Unit {} has no icon and its replaceable icon {} "
                            "is not a file : using a question mark instead".
                            format(unit, icon_path))

                        question_mark = 'SelectHeroOn'
                        icon_path = join(options['root'],
                                         ICONS_DIR,
                                         'BTN{}.blp'.format(question_mark))

                self.handle_unit(race, unit, icon_path, categories)

                for sound in listdir(unit_root):
                    sound_path = join(unit_root, sound)
                    if not isfile(sound_path) or sound_path[-4:] != '.wav':
                        continue

                    self.handle_sound(race, unit, sound_path)

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

        sound_name = basename(sound)[:-4]

        with open(sound, 'rb') as fh:
            s = File(fh)
            Sound.objects.get_or_create(
                name=sound_name,
                unit=u,
                audio=s,
            )
