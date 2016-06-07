
# -*- coding: utf-8 -*-
import json
from .models import PhenoDbHpo
from django.core.exceptions import ObjectDoesNotExist
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''
Esta classe devolve todas a informacoes relacionadas a um determido hpo_id
em um arquivo json
'''
class Phizz:


    def __init__(self, hpo_id):
        self.data_form(hpo_id)

    def data_form(self, hpo_id):
        '''
        Esta funcao prepara todos os dados antes de serem
        escritos no json
        '''
        response_data = {}
        try:
            hpo = PhenoDbHpo.objects.get(hpo_id=hpo_id)

            genes_list = []

            for gene in hpo.gene.all().values_list('gene', flat=True):
                genes_list.append(gene)

            response_data['hpo_term'] = hpo.hpo_id
            response_data['description'] = hpo.hpo_name
            response_data['genes'] = genes_list

            self.write_file(response_data)
        except ObjectDoesNotExist:
            print('HPO termo não encontrado')

    def write_file(self, data):
        '''
        Esta funcao cria o arquivo json e faz a escritura dos dados
        neste arquivo
        '''
        file_name = data['hpo_term'].replace(':', '_') + '.json'
        path = os.path.join(BASE_DIR, 'problema_1/', file_name)
        with open(path, 'w+') as outfile:
            json.dump(data, outfile)
