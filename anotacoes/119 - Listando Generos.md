# Listando Gêneros: Criando uma View que Retorna um JSON

Neste projeto de API em Django, sem utilizar o Django REST Framework (DRF), estamos criando uma view personalizada para listar os gêneros disponíveis na base de dados. A view será responsável por retornar um **JSON** com todos os registros da tabela de gêneros, oferecendo uma interface simples e direta para a interação via requisições HTTP.

### 1. **Modelo `Genre`**

O modelo `Genre` é uma representação de um gênero no banco de dados. Ele contém apenas um campo, o `name`, que armazena o nome do gênero. Este é um exemplo básico de um modelo que poderá ser expandido conforme as necessidades do projeto.

```python
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
```

- **`name`**: Um campo de texto (`CharField`) com limite de 200 caracteres.
- **`__str__`**: Método para representar o objeto `Genre` como uma string, retornando o nome do gênero.

### 2. **View para Listar Gêneros**

Para listar os gêneros, criamos uma view chamada `genre_view`. Esta view recupera todos os gêneros do banco de dados, formata-os em uma lista de dicionários e retorna como resposta um JSON. O uso da função `JsonResponse` do Django é ideal para este tipo de API, pois facilita a conversão de dados para o formato JSON, que é amplamente utilizado em APIs.

```python
from django.http import JsonResponse
from apps.genres.models import Genre

def genre_view(request):
    genres = Genre.objects.all()  # Busca todos os registros de gênero no banco
    data = [{'id': genre.id, 'name': genre.name} for genre in genres]  # Converte os objetos para dicionários
    return JsonResponse(data, safe=False)  # Retorna o JSON como resposta
```

- **`Genre.objects.all()`**: Consulta o banco de dados e retorna todos os objetos do modelo `Genre`.
- **`data`**: Cria uma lista de dicionários, onde cada dicionário contém o `id` e o `name` de cada gênero. Isso garante que a resposta JSON esteja formatada corretamente, com uma estrutura fácil de consumir por um cliente (frontend ou outra API).
- **`JsonResponse(data, safe=False)`**: Retorna a lista em formato JSON. O parâmetro `safe=False` é necessário quando estamos retornando uma lista como resposta (por padrão, o Django espera um dicionário).

### 3. **Rota para a View**

No arquivo `urls.py` do seu app `genres`, precisamos definir a rota para acessar essa view. Aqui está como definir a URL para a listagem de gêneros:

```python
from django.urls import path
from apps.genres.views import genre_view

urlpatterns = [
    path('genres/', genre_view, name='genre-list'),
]
```

Ao configurar essa URL, agora sua API poderá responder a uma requisição GET em `/genres/` com uma lista de todos os gêneros no formato JSON.

### 4. **Testando a API**

Ao acessar a rota `/genres/` através de um cliente HTTP (como o Postman ou o curl), a resposta será algo parecido com o seguinte, caso haja registros no banco de dados:

```json
[
    {"id": 1, "name": "Action"},
    {"id": 2, "name": "Comedy"},
    {"id": 3, "name": "Drama"}
]
```

Se o banco de dados estiver vazio, a resposta será uma lista vazia:

```json
[]
```
