# Implementando Lógica de Permissões no Django REST Framework

No Django REST Framework (DRF), o controle de acesso granular pode ser implementado através de permissões personalizadas. Através das permissões, você pode definir regras específicas sobre quem pode acessar ou modificar os recursos da sua API.

#### Classe `BasePermission`

Para criar uma permissão personalizada, você herda da classe `BasePermission` do DRF. Essa classe fornece uma estrutura básica para definir regras de permissão através de dois métodos principais:

- `has_permission(self, request, view)`: Verifica se a requisição tem permissão de acesso em geral.
- `has_object_permission(self, request, view, obj)`: Verifica se a requisição tem permissão de acesso a um objeto específico.

#### Exemplo de Implementação: `GenrePermissionClass`

Vamos considerar um exemplo onde você deseja controlar o acesso às operações de leitura e escrita na sua API de gêneros de filmes. Abaixo está a implementação da classe de permissão `GenrePermissionClass`, que verifica as permissões do usuário com base no método HTTP da requisição:

```python
from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # Permitir GET, OPTIONS e HEAD se o usuário tiver a permissão 'view_genre'
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genre')
        
        # Permitir POST se o usuário tiver a permissão 'add_genre'
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        # Negar acesso para outros métodos HTTP
        return False
```

#### Explicação da Lógica

- **GET, OPTIONS, HEAD**: Esses métodos geralmente são usados para recuperar dados. A permissão `'genres.view_genre'` é verificada para permitir que o usuário visualize os gêneros.
- **POST**: Este método é usado para criar novos recursos. A permissão `'genres.add_genre'` é verificada para permitir que o usuário adicione novos gêneros.
- **Outros Métodos HTTP**: Para qualquer outro método HTTP (como PUT, DELETE), o acesso é negado retornando `False`.

#### Aplicando a Classe de Permissão na View

Para utilizar esta classe de permissão na sua view, você deve definir a propriedade `permission_classes` na classe de view correspondente:

```python
# apps/genres/views.py

from rest_framework import generics
from apps.genres.models import Genre
from apps.genres.serializers import GenreSerializer
from apps.genres.permissions import GenrePermissionClass

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (GenrePermissionClass,)

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (GenrePermissionClass,)
```
