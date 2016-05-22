from os.path import join

from django.core.management.base import BaseCommand

from tools.utils import cmd


class Command(BaseCommand):
    help = """MPQExtractor CLI tool specific wrapper for warcraft 3 mpqs"""

    def add_arguments(self, parser):
        parser.add_argument('-e', '--extension', required=True,
                            choices=['roc', 'tft'],
                            help='roc or tft files ?')

        parser.add_argument('-a', '--action', default='list',
                            choices=['list', 'extract'],
                            help='List or extract files ?')

        parser.add_argument('-p', '--pattern', default='*',
                            help='Search pattern')

        parser.add_argument('-o', '--output-dir', default='.',
                            help='Where to extract files if action is extract')

        parser.add_argument('-f', '--fullpath', action='store_true',
                            help='Preserve archive path hierarchy')

        parser.add_argument('-lc', '--lowercase', action='store_true',
                            help='Convert file paths to lowercase')

    def handle(self, *args, **options):
        MPQ_DIR = '/home/apps/war3/Warcraft III'
        MPQS = {
            'vanilla': {
                'roc': 'war3.mpq',
                'tft': 'War3x.mpq',
            },
            'patch': {
                'roc': 'War3Patch.mpq',
                'tft': 'War3xlocal.mpq',
            },
        }

        mpq_args = ['MPQExtractor']

        # mpq_args += [
        #     '--patches',
        #     join(MPQ_DIR, MPQS['patch'][options['extension']]),
        # ]
        # mpq_args += ['--prefix', 'base']

        if options['action'] == 'list':
            mpq_args.append('--search')
        elif options['action'] == 'extract':
            mpq_args += ['--dest', options['output_dir']]

            mpq_args.append('--extract')

        mpq_args.append(options['pattern'])

        if options['fullpath']:
            mpq_args.append('--fullpath')

        if options['lowercase']:
            mpq_args.append('--lowercase')

        mpq_args.append(join(MPQ_DIR, MPQS['vanilla'][options['extension']]))

        self.stdout.write(cmd(*mpq_args).decode('utf-8'))
