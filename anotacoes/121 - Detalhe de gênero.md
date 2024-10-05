# Detalhe de Gênero: Usando `get_object_or_404` para Exibir um Gênero Específico

Nesta descrição, vamos abordar a criação de uma nova view no Django chamada `genre_detail_view`, que permite buscar e exibir detalhes de um gênero específico com base no seu ID (primária) fornecido na URL. Utilizamos a função `get_object_or_404`, que é nativa do Django, para buscar o gênero no banco de dados de forma eficiente e retornar uma resposta JSON com os detalhes desse gênero.

## Estrutura de Código

### 1. **Rota Configurada no `urls.py`**
No arquivo `urls.py`, adicionamos uma rota que inclui um parâmetro dinâmico `<int:pk>`, representando o ID do gênero. Essa rota será usada para buscar um gênero específico.

```python
from django.contrib import admin
from django.urls import path
from apps.genres.views import genre_create_list_view, genre_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_create_list_view, name='genre-create-list'),
    path('genres/<int:pk>', genre_detail_view, name='genre-detail-view')
]
```

Aqui, a rota `genres/<int:pk>` mapeia URLs como `genres/1` ou `genres/5`, onde `1` ou `5` seria o ID do gênero que se deseja buscar.

- **`<int:pk>`**: Um parâmetro dinâmico que representa o ID (chave primária) do gênero. Ele é capturado na URL e passado para a view como argumento.

### 2. **View `genre_detail_view`**
No arquivo de views, criamos a view `genre_detail_view`, que recebe o ID como parâmetro e busca o objeto correspondente no banco de dados usando `get_object_or_404`. Esta view retorna uma resposta JSON com os detalhes do gênero encontrado.

```python
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from apps.genres.models import Genre

@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)  # Busca o gênero ou retorna 404
    data = {'id': genre.id, 'name': genre.name}  # Cria um dicionário com os detalhes do gênero
    return JsonResponse(data)  # Retorna a resposta JSON com os dados do gênero
```

## Detalhes da Lógica

### 1. **Recebendo o Parâmetro `pk`**
A função `genre_detail_view` recebe dois argumentos:
- **`request`**: O objeto de requisição, que contém informações sobre a requisição HTTP.
- **`pk`**: O ID (chave primária) do gênero que foi extraído da URL.

Esse ID é então utilizado para buscar o objeto no banco de dados.

### 2. **Usando `get_object_or_404`**
A função `get_object_or_404` do Django é usada para buscar o objeto `Genre` com base no ID fornecido. Se o gênero com o ID especificado não for encontrado, o Django automaticamente retorna uma resposta **404 (Not Found)**.

```python
genre = get_object_or_404(Genre, pk=pk)
```

- **`Genre`**: O modelo que estamos consultando, ou seja, a tabela `Genre` no banco de dados.
- **`pk=pk`**: O critério de busca, onde `pk` (chave primária) é igual ao valor fornecido na URL.

### 3. **Criando a Resposta JSON**
Depois que o gênero é encontrado, criamos um dicionário Python com os detalhes do gênero, contendo o `id` e o `name`:

```python
data = {'id': genre.id, 'name': genre.name}
```

Esse dicionário é então retornado como uma resposta JSON:

```python
return JsonResponse(data)
```

- **`JsonResponse`**: Retorna o dicionário como uma resposta JSON, o que é essencial para uma API. Ele automaticamente serializa o dicionário Python para o formato JSON.

### 4. **Exemplo de Requisição GET**
Quando a URL `genres/<int:pk>` é acessada via uma requisição GET, a view busca o gênero correspondente ao ID fornecido e retorna seus detalhes em JSON. Aqui está um exemplo de como seria uma requisição e resposta:

#### Exemplo de Requisição
```http
GET /genres/1
```

#### Exemplo de Resposta
```json
{
    "id": 1,
    "name": "Action"
}
```

Se não houver um gênero com o ID fornecido, a função `get_object_or_404` retornará automaticamente um erro **404 (Not Found)**.
