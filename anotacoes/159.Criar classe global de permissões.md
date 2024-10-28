# Criando uma Classe Global de Permissões no Django REST Framework

No Django REST Framework (DRF), podemos definir permissões personalizadas para controlar o acesso dos usuários aos diferentes endpoints da API. Uma abordagem eficiente é criar uma classe de permissão global que pode ser reutilizada em várias partes do projeto, centralizando a lógica de permissões.

#### Classe Global de Permissões

A classe `GlobalDefaultPermission` é uma implementação de uma permissão global que verifica se o usuário tem a permissão adequada com base no método HTTP da requisição e no modelo associado à view. Vamos analisar o código e entender como ele funciona.

```python
# core/permissions.py

from rest_framework import permissions

class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )
        if not model_permission_codename:
            return False
        return request.user.has_perm(model_permission_codename)
    
    def __get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method=method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None
    
    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
```

#### Análise do Código

1. **Importação da Classe BasePermission**:
   - O código importa `BasePermission` da biblioteca `rest_framework.permissions`, que serve como a classe base para todas as permissões personalizadas.

2. **Método `has_permission`**:
   - Este método é chamado para verificar se a requisição tem permissão para acessar a view.
   - Primeiro, ele chama o método privado `__get_model_permission_codename` para obter o codename da permissão baseada no método HTTP e na view.
   - Se o codename não for encontrado, a permissão é negada (`return False`).
   - Se o codename for encontrado, a permissão é verificada usando `request.user.has_perm(model_permission_codename)`.

3. **Método Privado `__get_model_permission_codename`**:
   - Este método privado constrói o codename da permissão baseada no método HTTP e na view.
   - Ele tenta acessar o modelo associado à queryset da view e obtém o nome do modelo (`model_name`) e o app label (`app_label`).
   - Em seguida, chama o método privado `__get_action_sufix` para obter o sufixo da ação baseado no método HTTP.
   - O codename é construído no formato `'{app_label}.{action}_{model_name}'`.

4. **Método Privado `__get_action_sufix`**:
   - Este método privado mapeia os métodos HTTP para os sufixos de ação correspondentes (`view`, `add`, `change`, `delete`).
   - Retorna o sufixo apropriado com base no método HTTP.

#### Utilização na View

Para utilizar essa permissão global nas suas views, basta adicionar a classe `GlobalDefaultPermission` à lista de `permission_classes` das views.

```python
# apps/genres/views.py

from rest_framework import generics
from apps.genres.models import Genre
from apps.genres.serializers import GenreSerializer
from core.permissions import GlobalDefaultPermission

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (GlobalDefaultPermission,)

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (GlobalDefaultPermission,)
```

#### Vantagens da Classe Global de Permissões

1. **Centralização da Lógica**:
   - A lógica de permissão é centralizada em uma única classe, facilitando a manutenção e o gerenciamento de permissões.

2. **Reutilização**:
   - A classe de permissão pode ser reutilizada em várias views, evitando duplicação de código.

3. **Flexibilidade**:
   - A implementação pode ser facilmente ajustada para suportar diferentes modelos e métodos HTTP.

4. **Manutenção Simplificada**:
   - Alterações na lógica de permissão precisam ser feitas apenas na classe global, propagando as mudanças automaticamente para todas as views que a utilizam.
