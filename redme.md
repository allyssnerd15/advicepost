advice
teste Python

O script está sem o arquivo Docker para inicialização. É possivel rodar direto da maquina utlizando postman.

As requisições POST e PUT esperam uma requisição json. exemplo: { 'id': 'id', 'Nome': 'nome', 'Modelo': modelo, 'Cor': 'cor' }

Caso esteja fora do padrão acima a requisão não será aceita. O arquivo requirements está disponivel para instalar todas as bibliotecas usadas nesse projeto. É aconselhavem que crie um ambiente virtual para executa-lo. exemplo: win: python -m venv {Nome da pasta do ambiente virtual} ativa-lo: nome_da_pasta\Scripts\activate

linux: virtualenv {Nome da pasta do ambiente virtual} ativa-lo: source\nome_da_pasta\activate
