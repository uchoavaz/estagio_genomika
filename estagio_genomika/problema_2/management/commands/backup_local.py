
from django.core.management import BaseCommand
from problema_2.backup_local import Backup
import sys


class Command(BaseCommand):

    def add_arguments(self, hpo):
        hpo.add_argument('poll_id', nargs='+', type=str)

    def handle(self, *args, **options):
        days_delete = 2
        Backup(sys.argv[2], days_delete)
