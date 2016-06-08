
# -*- coding: utf-8 -*-
import urllib
from .models import PhenoDbHpo
from .models import PhenoDbGene
import os

'''
Esta classe faz uso do txt, que esta na web, e grava seus dados
no banco de dados local da maquina. Ele distribui os dados entre as tabelas
PhenoDbHpo e PhenoDbGene e faz suas relacoes (N <--> N).Ela nao deixa que os
dados se repitam em cada tabela, pois ha um tratamento, caso suas forem quebradas.
'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class UpdateLocal():

    txt_url = (
        'http://compbio.charite.de/jenkins/job/hpo.annotations.monthly'
        '/lastStableBuild/artifact/annotation/'
        'ALL_SOURCES_TYPICAL_FEATURES_phenotype_to_genes.txt ')

    def update(self):
        self.download_data(self.txt_url)

    def download_data(self, txt_url):
        '''
        Esta funcao baixa o txt para o projeto e
        faz a leitura de todas as linhas do txt
        '''
        file_name = 'hpo_genes.txt'
        file_location = (BASE_DIR + '/problema_1/' + file_name)

        urllib.urlretrieve(txt_url, file_location)

        txt_file = open(file_location)
        for line in txt_file.readlines():
            data = line.split('\t')
            self.save(data)

        txt_file.close()

    def save(self, data):
        '''
        Esta funcao grava todas os dados nas tabelas e faz suas
        relacoes
        '''
        try:
            hpo_id = data[0]
            hpo_name = data[1]
            gene_id = data[2]
            gene_name = data[3].strip('\n')

            gene = PhenoDbGene.objects.get_or_create(
                gene_id=gene_id,
                gene=gene_name
            )
            hpo = PhenoDbHpo.objects.get_or_create(
                hpo_id=hpo_id,
                hpo_name=hpo_name,
            )

            hpo[0].gene.add(gene[0])

        except IndexError:
            pass
