
import os
from django.conf import settings
import datetime
import time


class Backup():

    '''
    Esta classe gerencia o processo de backup do arquivo
    do banco de dados sqlite3, salvando os arquivos
    em um diretorio escolhido pelo usuario
    '''

    directory = None
    days_delete = None

    def __init__(self, directory, days_delete):
        self.directory = directory
        self.days_delete = days_delete
        self.create_folder()

    def create_folder(self):
        '''
        Este metodo cria a pasta onde ficara
        os arquivos de backup
        '''
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        self.delete_old_bkp(self.days_delete)

    def delete_old_bkp(self, days_delete):
        '''
        Este metodo deletara os backup's com 3 dias
        ou mais
        '''
        time_now = (time.time() - (days_delete * 86400))

        files = os.listdir(self.directory)
        for xfile in files:
            file_dir = (self.directory + '/' + xfile)
            date_file = os.stat(file_dir).st_ctime
            if date_file <= time_now:
                os.remove(file_dir)

        self.create_backup()

    def create_backup(self):
        '''
        Este metodo cria o backup no diretorio escolhido
        pelo usuario
        '''
        db_dir = settings.DATABASES['default']['NAME']
        data_backup = datetime.datetime.now().strftime("%Y%m%d")
        backup_dir = (self.directory + '/hpo_' + data_backup + '.bak')
        if os.path.isfile(db_dir):
            backup_command = 'sqlite3 {0} .dump > {1}'.format(
                db_dir, backup_dir)
        else:
            print ('Arquivo sqlite nao existente')
        os.system(backup_command)
