from __future__ import unicode_literals

from django.db import models


class PhenoDbGene(models.Model):
    '''
    Modelo do banco da tabela PhenoDbGene
    '''
    gene_id = models.CharField(
        verbose_name='Gene ID', max_length=10, unique=True)
    gene = models.CharField(verbose_name='Gene', max_length=15)

    class Meta:
        verbose_name = (u'Gene')
        verbose_name_plural = (u'Genes')

    def __str__(self):
        return self.gene_id

    def __repr__(self):
        return self.gene_id

    def __unicode__(self):
        return self.gene_id


class PhenoDbHpo(models.Model):
    '''
    Modelo do banco da tabela PhenoDbHpo
    '''
    hpo_id = models.CharField(
        verbose_name='HPO ID', max_length=10, unique=True)
    hpo_name = models.CharField(verbose_name='Nome do HPO', max_length=255)
    gene = models.ManyToManyField(PhenoDbGene, related_name='hpo')

    class Meta:
        verbose_name = (u'HPO')
        verbose_name_plural = (u'HPO')

    def __str__(self):
        return self.hpo_id

    def __repr__(self):
        return self.hpo_id

    def __unicode__(self):
        return self.hpo_name

'''
Relacao: PhenoDbGene N <--> N PhenoDbHpo
'''
