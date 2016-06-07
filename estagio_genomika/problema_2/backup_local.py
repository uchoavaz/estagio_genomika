
import os
from django.conf import settings
import datetime
import time

class Backup():

    directory = None
    days_delete = None

    def __init__(self, directory, days_delete):
        self.directory = directory
        self.days_delete = days_delete
        self.create_folder()

    def create_folder(self):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        self.delete_old_bkp(self.days_delete)

    def delete_old_bkp(self, days_delete):
        time_now = (time.time() - (days_delete * 86400))

        files = os.listdir(self.directory)
        for xfile in files:
            file_dir = (self.directory + '/' + xfile)
            date_file = os.stat(file_dir).st_ctime
            if date_file < time_now:
                os.remove(file_dir)

        self.create_backup()

    def create_backup(self):
        db_dir = settings.DATABASES['default']['NAME']
        data_backup = datetime.datetime.now().strftime("%Y%m%d")
        backup_dir = (self.directory + '/hpo_' + data_backup + '.bak')
        backup_command = 'sqlite3 {0} .dump > {1}'.format(db_dir, backup_dir)
        os.system(backup_command)
