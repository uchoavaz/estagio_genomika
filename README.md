#Teste de Seleção da Genomika

  Neste arquivo estará presente todo o passo-a-passo para se realizar a execução dos scripts solicitados nos problemas deste Teste de uma forma bem detalhada.
  
Preparando a Máquina
------------
* Este projeto pode ser rodado em sistema UNIX.Neste caso, a plataforma de teste foi o Ubuntu 14.04 x64

1 - Instalando o pip:

    sudo apt-get update
    sudo apt-get -y install python-pip

2 - Instalando o git :
    
    sudo apt-get install git-all

3 - Vá um diretório a sua escolha(recomendo 'cd /home/user') e baixe o repositório do projeto com o comando :

    git clone https://github.com/uchoavaz/estagio_genomika.git


Resolução do Teste
------------

- Problema 1

  Neste problema, foi pedido pra se fazer um script que baixasse um .txt que esta contido em uma url e depois salva-lo na máquina local e , após isso, salvar todos os dados em um banco de dados local.
  
  Normalizei todas as entidades do banco, criando duas tabelas(PhenoDbHpo e PhenoDbGene) que se relacionam com o tipo de N para N e configurei o script em python para que não houvesse repetições de dados em ambas as tabelas.
  
  Para rodar o script que "puxa" todas essas informções, vá para o diretório em que foi baixado o projeto.
  
  Ex: 'cd /home/user/'
  
  Depois, vá para o diretório :
  
      cd /estagio_genomika/estagio_genomika
  
  e rode o script :
  
      python manage.py update_local
  
  o download do arquivo gerado('hpo_genes.txt') fica no mesmo diretório do script:
  
      /home/user/estagio_genomika/estagio_genomika/problema_1
  
  *Lembrando que são quase 400 mil linhas de dados e o banco é o sqlite3, então, pode-se demorar horas para concluir a tarefa
