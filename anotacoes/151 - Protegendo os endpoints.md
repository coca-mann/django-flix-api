# Protegendo Endpoints com Permissões no Django Rest Framework

Ao desenvolver uma API, é crucial proteger determinados endpoints para garantir que apenas usuários autenticados ou com permissões adequadas possam acessá-los. No **Django Rest Framework (DRF)**, isso é feito através de **permission classes**, que determinam quem tem o direito de acessar cada view.

### Utilizando a Classe `IsAuthenticated`

A classe de permissão **`IsAuthenticated`** é uma das permissões padrão fornecidas pelo DRF. Ela restringe o acesso a apenas usuários autenticados, ou seja, usuários que tenham feito login e possuam um token de autenticação válido, como um token JWT. Se um usuário não estiver autenticado, ele receberá uma resposta de erro `401 Unauthorized`.

No exemplo abaixo, protegemos o endpoint de criação e listagem de atores (`ActorCreatListView`) para que somente usuários autenticados possam acessá-lo.

### Exemplo de Código

```python
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.actors.models import Actor
from apps.actors.serializers import ActorSerializer


class ActorCreatListView(generics.ListCreateAPIView):
    # Aplica a permissão de apenas usuários autenticados
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
```

Aqui está o que está acontecendo:

- **`permission_classes`**: Essa propriedade é usada para definir as classes de permissão aplicadas à view. No caso, estamos utilizando **`IsAuthenticated`**, que garante que apenas usuários autenticados possam acessar as operações de listagem e criação de atores.
  
- **Comportamento do DRF**: Quando um cliente faz uma requisição a esse endpoint (GET ou POST) sem estar autenticado, o DRF retornará automaticamente uma resposta **401 Unauthorized**. Se o cliente estiver autenticado, ele poderá acessar normalmente.

### Proteger Outros Endpoints

A classe **`IsAuthenticated`** pode ser usada em qualquer **View** ou **ViewSet**. Por exemplo, se você tiver uma view de atualização ou exclusão, pode aplicar a mesma lógica:

```python
from rest_framework.permissions import IsAuthenticated
from apps.actors.models import Actor
from apps.actors.serializers import ActorSerializer
from rest_framework import generics

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
```

#### Vantagens de Usar `IsAuthenticated`

1. **Segurança**: Garante que apenas usuários autenticados possam acessar e modificar os dados sensíveis da API.
2. **Facilidade de implementação**: O DRF fornece várias classes de permissão prontas para uso, como `IsAuthenticated`, o que facilita a proteção de endpoints.
3. **Escalabilidade**: Permite adicionar diferentes classes de permissões para diferentes endpoints de forma modular, de acordo com a necessidade do projeto.

Essa abordagem oferece uma camada de segurança para os endpoints da sua API, exigindo que os usuários façam login antes de interagir com a aplicação, aumentando a segurança e garantindo o controle adequado sobre quem pode acessar e modificar os dados.