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

4 - Para instalar as dependencias do projeto vá para o diretório raiz do projeto :

    cd /home/user/estagio_genomika/estagio_genomika/home/user/estagio
  
  e execute :

    pip install -r requirements.txt
Resolução do Teste
------------

- Problema 1

  Neste problema, foi pedido pra se fazer um script que baixasse um .txt que esta contido em uma url, salva-lo na máquina local e por fim, salvar todos os dados em um banco de dados local.
  
  Normalizei todas as entidades do banco, criando duas tabelas(PhenoDbHpo e PhenoDbGene) que se relacionam com o tipo de N para N e configurei o script em python para que não houvesse repetições de dados em ambas as tabelas.
  
  Para rodar o script que "puxa" todas essas informções, vá para o diretório em que foi baixado o projeto.
  
  Ex: 'cd /home/user/'
  
  e entre no diretório raiz do projeto:
  
      cd /estagio_genomika/estagio_genomika
  
  e rode o script :
  
      python manage.py update_local
  
  o download do arquivo gerado('hpo_genes.txt') fica salvo no mesmo diretório do script('update_local.py'):
  
      cd /home/user/estagio_genomika/estagio_genomika/problema_1
  
  *Lembrando que são quase 400 mil linhas de dados e o banco é o sqlite3 então, pode-se demorar horas para concluir a tarefa. O projeto já está populado, caso não queira esperar e passar para as próximas etapas.
  
  Agora, o pŕoximo passo é extrair as informações relacionadas a um determinado HPO_ID passado pelo usuário.Utilize o comando a seguir no diretório raiz do projeto('/home/user/estagio_genomika/estagio_genomika') com um HPO_ID:
  
      python manage.py phizz HPO_ID
  
  *Se tentar passar um HPO_ID incorreto ou não existente, o script retorna uma mensagem
  
  Após ter inserido o comando, as informações relativas a esse HPO_ID estarão disponíveis em um arquivo .json (EX:HP_00000002.json) no mesmo diretório do script('phizz.py'):
  
        cd /home/user/estagio_genomika/estagio_genomika/problema_1

- Problema 2
  
  Neste problema foi pedido um script que fizesse um processo automatizado de backup do banco de dados em um diretorio escolhido pelo usuário
  
  No diretório raiz do projeto('/home/user/estagio_genomika/estagio_genomika') execute o comando para rodar o scrip de backup passando um diretório como argumento(Ex:'/home/user/backup_folder') :
      
        python manage.py backup_local /home/user/backup_folder

  Ele executará o script 'backup_local.py' localizado no diretório ('/home/user/estagio_genomika/estagio_genomika/problema_2'). Este script cria a pasta 'backup_folder' no diretório '/home/user', verifica se existem arquivos com 3 dias ou mais de criação, exclui os mesmos se a afirmação for verdadeira e insere nela um arquivo de backup do banco de dados (sqlite3) com o formato .bak e o nomeia com a sua data de execução(Ex: 'hpo_20160607.bak')
