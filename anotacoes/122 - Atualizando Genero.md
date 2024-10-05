# Atualizando Gênero: Implementando o Método `PUT` na View `genre_detail_view`

Nesta abordagem, vamos descrever como a mesma view `genre_detail_view`, que lida com a exibição de detalhes de um gênero, pode ser estendida para permitir a **atualização** de um gênero existente usando o método **PUT**. Este é um exemplo clássico de como fazer atualizações em uma API sem utilizar o Django Rest Framework, apenas com as ferramentas nativas do Django.

## Estrutura de Código

```python
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from apps.genres.models import Genre

@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)  # Busca o gênero ou retorna 404

    if request.method == 'GET':
        # Retorna os detalhes do gênero
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)

    elif request.method == 'PUT':
        # Atualiza o gênero existente
        data = json.loads(request.body.decode('utf8'))  # Decodifica o JSON da requisição
        genre.name = data['name']  # Atualiza o nome do gênero
        genre.save()  # Salva a alteração no banco de dados
        return JsonResponse(
            {'id': genre.id, 'name': genre.name},  # Retorna o gênero atualizado
        )
```

## Detalhes do Método `PUT`

### 1. **Recebendo o Método `PUT`**
Ao acessar essa view com uma requisição **PUT**, ela espera que o corpo da requisição contenha os dados necessários para atualizar o gênero.

- **Método HTTP PUT**: O método PUT é utilizado para **atualizar** um recurso existente. Neste caso, estamos atualizando um gênero existente no banco de dados.

### 2. **Decodificando o Corpo da Requisição**
Ao receber a requisição, o corpo da mensagem (request body) contém os dados em formato JSON que precisam ser processados. Para isso, utilizamos o método `json.loads()` para transformar o JSON recebido em um dicionário Python.

```python
data = json.loads(request.body.decode('utf8'))
```

- **`request.body`**: Contém o corpo da requisição, que é recebido como uma sequência de bytes.
- **`decode('utf8')`**: Converte a sequência de bytes em uma string legível.
- **`json.loads()`**: Converte a string JSON em um dicionário Python para manipulação.

### 3. **Atualizando os Dados do Gênero**
Após decodificar os dados, o nome do gênero (campo `name`) é atualizado com o novo valor fornecido no corpo da requisição.

```python
genre.name = data['name']
```

### 4. **Salvando no Banco de Dados**
Depois de atualizar o campo `name` no objeto `genre`, a operação de **salvar** no banco de dados é realizada através do método `save()`.

```python
genre.save()
```

- O método `save()` é uma função padrão do Django que persiste as alterações feitas no objeto no banco de dados.

### 5. **Resposta JSON**
Após a atualização, uma resposta JSON é enviada de volta ao cliente, confirmando que o gênero foi atualizado com sucesso. A resposta contém o `id` e o `name` atualizados.

```python
return JsonResponse({'id': genre.id, 'name': genre.name})
```

### Exemplo de Requisição `PUT`
Aqui está um exemplo de como a requisição **PUT** seria feita para atualizar o nome de um gênero:

#### Exemplo de Requisição
```http
PUT /genres/1
Content-Type: application/json

{
    "name": "New Genre Name"
}
```

#### Exemplo de Resposta
```json
{
    "id": 1,
    "name": "New Genre Name"
}
```

### Tratamento de Erros
- Caso o gênero com o ID fornecido na URL não seja encontrado, a função `get_object_or_404` automaticamente retornará um erro **404 (Not Found)**, indicando que o recurso solicitado não existe.
- Se o corpo da requisição não contiver um nome válido, ou estiver malformado, será necessário implementar validações adicionais para garantir que a atualização seja feita corretamente.
