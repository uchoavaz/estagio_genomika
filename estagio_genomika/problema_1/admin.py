from django.contrib import admin
from .models import PhenoDbGene
from .models import PhenoDbHpo


class PhenoDbGeneAdmin(admin.ModelAdmin):
    search_fields = ['gene_id', 'gene']
    list_display = (
        'gene_id',
        'gene')


class PhenoDbHpoAdmin(admin.ModelAdmin):
    search_fields = ['hpo_id', 'hpo_name']
    list_display = (
        'hpo_id',
        'hpo_name')

admin.site.register(PhenoDbGene, PhenoDbGeneAdmin)
admin.site.register(PhenoDbHpo, PhenoDbHpoAdmin)
