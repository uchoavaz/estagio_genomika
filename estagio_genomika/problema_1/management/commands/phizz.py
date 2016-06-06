
from django.core.management import BaseCommand
from problema_1.phizz import Phizz
import sys


class Command(BaseCommand):

    def add_arguments(self, hpo):
        hpo.add_argument('poll_id', nargs='+', type=str)

    def handle(self, *args, **options):
        hpo = sys.argv[2]
        if hpo[0:2] == 'HP':
            if hpo[2:3] == ':':
                try:
                    int(hpo[3:])
                    Phizz(hpo)
                except ValueError:
                    self.error()
            else:
                self.error()
        else:
            self.error()

    def error(self):
        print 'Termo incorreto, informe no formato HP:HPO_ID'
