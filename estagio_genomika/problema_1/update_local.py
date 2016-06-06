
# -*- coding: utf-8 -*-
import urllib2
from .models import PhenoDbHpo
from .models import PhenoDbGene


class UpdateLocal():

    txt_url = (
        'http://compbio.charite.de/jenkins/job/hpo.annotations.monthly'
        '/lastStableBuild/artifact/annotation/'
        'ALL_SOURCES_TYPICAL_FEATURES_phenotype_to_genes.txt ')

    def update(self):
        self.download_data(self.txt_url)

    def download_data(self, txt_url):

        data = urllib2.urlopen(txt_url)
        for line in data:
            data = line.split('\t')
            self.save(data)

    def save(self, data):
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
