# APEF API
Api específica para **Agendamento de Procedimentos Estéticos Fáciais.**

Através desta api, será possível:
> * Agendar procedimentos.
> * Listar os procedimentos agendados.
> * Consultar procedimentos atravéz de filtros especificos.
> * Alterar dados de um procedimento agendado.
> * Cancelar um procedimento agendado.
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


