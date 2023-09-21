# APEF API
Api específica para **Agendamento de Procedimentos Estéticos Fáciais.**

A API surgil da necessidade real de criar um app que seja simples e ao mesmo 
tempo eficiente, para realizar o controle e os agendamentos de 
procedimentos de uma determinada clínica de estética facial, tendo em vista que os
apps existentes, são complexos e nem um pouco objetivo, dificultando
o bom andamento da clinica.

Através desta api, será possível:
> * Cadastrar um médico esteticista.
> * Listar os médicos cadastrados.
> * Cadastrar um procedimento.
> * Listar os procedimentos cadastrados.
> * Agendar a realização de um procedimento.
> * Listar os procedimentos agendados.
> * Consultar procedimentos atravéz da data.
> * Excluir um procedimento agendado.

---
## Como executar


Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, 
para poder executar os comandos descritos abaixo.

Crie um ambiente virtual usando o comando:

```
python -m venv venv
```

Será criado um diretorio venv na raiz da aplicação e será necessário ativá-lo.

Para linux use o comando para ativar a venv:

```
source venv/bin/activate
```

Para Windows:

```
venv\Scripts\activate
```

Agora podemos instalar as dependências listadas no arquivo `requirements.txt`, 
usando o comando:

```
pip install -r requirements.txt
```

Para executar a API é só usar o comando abaixo:

```
flask run --host 0.0.0.0 --port 5000
```

Para facilitar o desenvolvimento pode-se usar o parâmetro reload, que 
reinicia o servidor automaticamente após uma mudança no código fonte.

 ```
 flask run --host 0.0.0.0 --port 5000 --reload
 ```

 Para abrir a API em um navegador basta digitar na barra de endereços:

 ```
 http://127.0.0.1:5000
 ```

## Como realizar um agendamento

> Antes de qualquer coisa é preciso ter certeza que existem médicos e procedimentos
cadastrados no banco de dados, caso não existam será nescessário realizar o cadastro
dos mesmos.

* Para verificar se existem médicos cadastrados podemos usar a própria documentação da 
API através do Swagger acessando o endpoint /doctors. 

* Para cadastrar um médico pela API podemos usar a própria documentação da 
API através do Swagger acessando o endpoint /doctor. 

* Para verificar se existem procedimentos cadastrados podemos usar a própria documentação da 
API através do Swagger acessando o endpoint /aesthetic_procedures. 

* Para cadastrar um procedimentos pela API podemos usar a própria documentação da 
API através do Swagger acessando o endpoint /aesthetic_procedure.

* Se já existirem médicos e procedimentos cadastrados e só acessar a documentação
Swagger atrravés do endpoint /scheduling para realizar um agendamento.

* Para listar todos os agendamentos usamos o endpoint /schedulings e para agendamentos
por data usamos o endpoint /schedulings_by_date.



