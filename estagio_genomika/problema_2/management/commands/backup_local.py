
from django.core.management import BaseCommand
import sys


class Command(BaseCommand):

    def add_arguments(self, hpo):
        hpo.add_argument('poll_id', nargs='+', type=str)

    def handle(self, *args, **options):
        print sys.argv
