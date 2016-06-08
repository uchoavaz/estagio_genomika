
from django.core.management import BaseCommand
from problema_1.update_local import UpdateLocal

'''
Classe que gerencia os argumentos no manage.py
'''
class Command(BaseCommand):
    '''
    Funcao para adicionar um argumento pelo comando no terminal
    '''

    def handle(self, *args, **options): 
        UpdateLocal().update()
