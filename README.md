# Teste Intmed Backend

1. Configurar o ambiente de execução (https://docs.python.org/pt-br/3/library/venv.html)

Após a configuração e inicialização do ambiente e clonagem do projeto, executar os seguintes passos para executar:

1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py runserver 8000

A partir de então a API estará executando no endereço apontado pelo localhost (http://127.0.0.1:8000).

Algumas operações como cadastro, listagem, atualização e deleção estão disponíveis através dos endpoints:

Especialidades: http://127.0.0.1:8000/especialidades/

Médicos: http://127.0.0.1:8000/medicos/

Consultas: http://127.0.0.1:8000/consultas/
