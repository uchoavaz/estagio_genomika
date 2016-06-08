
from django.core.management import BaseCommand
from problema_1.phizz import Phizz
import sys

'''
Classe que gerencia os argumentos no manage.py
'''
class Command(BaseCommand):
    '''
    Funcao para adicionar um argumento pelo comando no terminal
    '''
    def add_arguments(self, hpo):  
        hpo.add_argument('hpo', nargs='+', type=str)
    '''
    Funcao que dispara acoes apos o comando ser digitado
    '''
    def handle(self, *args, **options): 
        hpo = sys.argv[2]
        '''
        Iteracoes para saber se o parametro de entrada corresponde com o esperado
        '''
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
        self.stdout.write('Termo incorreto, informe no formato HP:HPO_ID')
