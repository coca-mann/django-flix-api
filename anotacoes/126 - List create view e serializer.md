# List Create View e Serializer com Django Rest Framework

Nesta descrição, vamos explorar como migrar de uma view funcional em Django para uma **Class-Based View (CBV)** usando o **Django Rest Framework (DRF)**. Além disso, vamos criar um **serializer** para converter os dados do modelo `Genre` em JSON, permitindo um código mais limpo e eficiente para trabalhar com APIs. Também vamos ajustar as URLs para utilizar a nova view baseada em classe.

### Visão Geral das Alterações

**Antes:** View funcional (FBV) que processa requisições GET e POST utilizando lógica procedural, sem uso do Django Rest Framework.

**Depois:** Uma view baseada em classe (CBV) utilizando `ListCreateAPIView` do DRF, que abstrai boa parte da lógica de listagem e criação, delegando as operações ao framework de forma mais organizada e eficiente.

---

### Código com Class-Based View (CBV)

#### **View Convertida para CBV com DRF**
Aqui estamos usando `ListCreateAPIView`, que herda de `APIView` e automaticamente trata requisições **GET** (para listar) e **POST** (para criar).

```python
from rest_framework import generics
from apps.genres.models import Genre
from apps.genres.serializers import GenreSerializer

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()  # Define os dados que serão listados
    serializer_class = GenreSerializer  # Define o serializer que será usado para processar os dados
```

- **`queryset = Genre.objects.all()`**: Define o conjunto de objetos que serão retornados na listagem, nesse caso, todos os gêneros cadastrados.
  
- **`serializer_class = GenreSerializer`**: Informa qual serializer será usado para validar, serializar e desserializar os dados do modelo.

---

#### **Serializer**
Um **serializer** é responsável por converter os objetos do Django (modelos) em JSON e vice-versa. O serializer abaixo converte os dados do modelo `Genre` para JSON.

```python
from rest_framework import serializers
from apps.genres.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'  # Inclui todos os campos do modelo no JSON gerado
```

- **`model = Genre`**: Informa que este serializer trabalha com o modelo `Genre`.
- **`fields = '__all__'`**: Diz ao serializer para incluir todos os campos do modelo na serialização. Isso torna o processo automático, sem precisar listar campos manualmente.

---

#### **URLs**
Aqui ajustamos o arquivo `urls.py` para utilizar a nova view baseada em classe, usando o método `as_view()` que converte a CBV em um callable que pode ser usado nas rotas.

```python
from django.contrib import admin
from django.urls import path
from apps.genres.views import GenreCreateListView, genre_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),  # Atualizado para usar a view CBV
]
```

---

### Comparação: View Funcional (FBV) vs. View Baseada em Classe (CBV)

#### **1. Implementação Geral**

**View Funcional (FBV):**

```python
@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name},
            status=201,
        )
```

- A lógica de tratamento de cada método HTTP (GET, POST) é manualmente implementada dentro de um único bloco de código.
- Precisamos gerenciar a serialização dos dados manualmente (transformar objetos em dicionários JSON).

**View Baseada em Classe (CBV) com DRF:**

```python
class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
```

- O DRF lida com toda a lógica por trás dos métodos HTTP de forma automática, com base no tipo de CBV que usamos. `ListCreateAPIView` já sabe lidar com requisições **GET** (listar) e **POST** (criar), reduzindo o código manual.
- A serialização e desserialização de dados são tratadas de forma automática pelo serializer, tornando o código mais limpo e organizado.

#### **2. Benefícios do Django Rest Framework**

- **Abstração da Lógica:** O DRF permite que a lógica repetitiva, como manipulação de requisições e serialização de dados, seja abstraída. Isso melhora a legibilidade e reduz a quantidade de código manual.
  
- **Validação Automática:** Com o uso de serializers, as validações dos dados de entrada e saída são feitas automaticamente, seguindo as regras definidas no modelo Django.
  
- **Mantenibilidade:** Usar CBVs e o DRF facilita a manutenção e escalabilidade do código. Com a separação clara entre a lógica da view e a serialização de dados, é mais fácil adicionar novas funcionalidades ou modificar o comportamento da API.

#### **3. Serialização de Dados**

**Na View Funcional (FBV):**
- Os dados são transformados manualmente de um queryset para uma lista de dicionários, exigindo mais código e risco de erro.

**Na View CBV com DRF:**
- A serialização é feita automaticamente pelo **GenreSerializer**, que transforma os dados do modelo Django diretamente em JSON.
