# Criando uma Classe de Permissão no Django REST Framework

No Django REST Framework (DRF), as permissões são uma maneira fundamental de controlar o acesso a diferentes partes de sua API. As permissões são verificadas para cada requisição e determinam se uma ação específica deve ser permitida ou negada. A criação de classes de permissão personalizadas permite que você implemente regras de acesso complexas e específicas para o seu aplicativo.

#### Conceito de `BasePermission`

`BasePermission` é uma classe base fornecida pelo DRF para a criação de permissões personalizadas. Ao herdar de `BasePermission`, você pode definir métodos que verificam se uma requisição específica deve ser permitida ou negada. Os dois métodos principais que podem ser sobrescritos são:

- `has_permission(self, request, view)`: Verifica permissões de nível de requisição, determinando se a requisição deve ser permitida em geral.
- `has_object_permission(self, request, view, obj)`: Verifica permissões de nível de objeto, determinando se a requisição deve ser permitida para um objeto específico.

#### Exemplo de Implementação de Classe de Permissão

Vamos criar uma classe de permissão personalizada no app `genre`. Primeiro, criaremos um novo arquivo `permissions.py` dentro do diretório do app `genre` e definiremos nossa classe de permissão.

```python
# apps/genres/permissions.py

from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # Implementa a lógica para verificar se a permissão é concedida
        return False
```

Neste exemplo, a classe `GenrePermissionClass` sempre retorna `False`, o que significa que todas as requisições são negadas. Obviamente, em uma aplicação real, você implementaria uma lógica mais complexa para determinar quando uma requisição deve ser permitida.

#### Utilizando a Classe de Permissão na View

Para aplicar essa classe de permissão a uma view, você deve definir a propriedade `permission_classes` na sua classe de view. Veja um exemplo de como aplicar a permissão personalizada a uma view:

```python
# apps/genres/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.genres.models import Genre
from apps.genres.serializers import GenreSerializer
from apps.genres.permissions import GenrePermissionClass

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GenrePermissionClass)

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GenrePermissionClass)
```

Neste exemplo, as permissões `IsAuthenticated` e `GenrePermissionClass` são aplicadas às views `GenreCreateListView` e `GenreRetrieveUpdateDestroyView`. Isso significa que, além de verificar se o usuário está autenticado, a lógica definida em `GenrePermissionClass` também será aplicada para determinar se a requisição deve ser permitida.
