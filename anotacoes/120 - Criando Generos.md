# Criando Gêneros: Manipulando Requisições POST em uma View

Nesta descrição, vamos detalhar o processo de criação de um novo gênero na API Django através de uma requisição **POST**. Estamos usando uma única view (`genre_view`) para tratar tanto as requisições **GET** quanto **POST**. No caso da requisição POST, a view recebe dados no corpo da requisição, cria um novo objeto `Genre` com base nesses dados, e retorna uma resposta JSON com o novo registro, além de um status HTTP 201 para indicar a criação bem-sucedida.

## Código da View (Método POST)

```python
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.genres.models import Genre

@csrf_exempt
def genre_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf8'))  # Decodifica o corpo da requisição JSON
        new_genre = Genre(name=data['name'])  # Cria uma nova instância de Genre com o dado 'name'
        new_genre.save()  # Salva o novo gênero no banco de dados
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name},  # Retorna o gênero criado
            status=201,  # Status HTTP 201 (Criado com sucesso)
        )
```

## Explicando o Processo do Método POST

Abaixo estão os passos e detalhes sobre como o método **POST** da view funciona:

### 1. **Verificação do Método de Requisição**
A view primeiro verifica se o método da requisição é **POST**. Isso é feito através da condição:

```python
elif request.method == 'POST':
```

Quando o método é POST, a view espera receber dados no corpo da requisição que serão usados para criar um novo registro de gênero.

### 2. **Recebendo os Dados do Corpo da Requisição**
Dado que as informações sobre o novo gênero são enviadas via JSON no corpo da requisição, a primeira coisa a ser feita é ler e interpretar esses dados:

```python
data = json.loads(request.body.decode('utf8'))
```

- **`request.body`**: Acessa o corpo bruto da requisição. Como a API está esperando um payload JSON, o corpo será um string codificado.
- **`decode('utf8')`**: Decodifica o corpo para uma string em UTF-8.
- **`json.loads()`**: Converte a string JSON em um dicionário Python. Assim, `data` será um dicionário contendo os dados enviados, como `{'name': 'Action'}`.

### 3. **Criando uma Nova Instância do Modelo `Genre`**
Com os dados decodificados, a próxima etapa é criar uma nova instância do modelo `Genre`, usando o valor do campo `name` fornecido no JSON:

```python
new_genre = Genre(name=data['name'])
```

Aqui, o campo `name` do modelo `Genre` está sendo preenchido com o valor correspondente da chave `'name'` presente no dicionário `data`. Por exemplo, se o JSON enviado for `{"name": "Action"}`, o novo gênero será criado com o nome "Action".

### 4. **Salvando o Objeto no Banco de Dados**
Após criar a instância, precisamos salvar esse novo gênero no banco de dados:

```python
new_genre.save()
```

Este comando executa a inserção do novo registro na tabela correspondente no banco de dados. Ao chamar o método `save()`, o Django também atualiza automaticamente o campo `id` do objeto recém-criado.

### 5. **Retornando uma Resposta JSON**
Uma vez que o novo gênero foi salvo, a view retorna uma resposta JSON contendo os dados do gênero criado:

```python
return JsonResponse(
    {'id': new_genre.id, 'name': new_genre.name},  # Retorna o gênero criado
    status=201,  # Status HTTP 201 (Criado com sucesso)
)
```

- **`{'id': new_genre.id, 'name': new_genre.name}`**: A resposta inclui o ID e o nome do novo gênero, que pode ser útil para o cliente que fez a requisição, caso ele queira referenciar o novo gênero em chamadas subsequentes.
- **`status=201`**: O código de status HTTP 201 indica que o recurso foi criado com sucesso. Esse código é uma prática recomendada em APIs para indicar criação de novos recursos.

### 6. **Exemplo de Requisição POST**
Aqui está um exemplo de uma requisição POST que poderia ser feita para criar um novo gênero:

```json
POST /genres/
Content-Type: application/json

{
    "name": "Action"
}
```

### 7. **Exemplo de Resposta**
A resposta JSON gerada pela view seria algo como:

```json
{
    "id": 1,
    "name": "Action"
}
```

Esta resposta inclui o `id` gerado automaticamente pelo banco de dados e o `name` do novo gênero.

### 8. **Segurança CSRF**
Note que a view foi decorada com o **@csrf_exempt**, desativando a verificação CSRF (Cross-Site Request Forgery) para essa view em particular:

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def genre_view(request):
```

Isso é necessário para aceitar requisições POST sem a necessidade de um token CSRF, o que é comum em APIs que são consumidas por aplicações externas. Porém, isso também pode introduzir vulnerabilidades, então em aplicações de produção, é importante proteger as rotas POST adequadamente.
