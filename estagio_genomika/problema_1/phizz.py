
# -*- coding: utf-8 -*-
import json
from .models import PhenoDbHpo
from django.core.exceptions import ObjectDoesNotExist
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Phizz:


    def __init__(self, hpo_id):
        self.data_form(hpo_id)

    def data_form(self, hpo_id):
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
        file_name = data['hpo_term'].replace(':', '_') + '.json'
        path = os.path.join(BASE_DIR, 'problema_1/', file_name)
        with open(path, 'w+') as outfile:
            json.dump(data, outfile)
