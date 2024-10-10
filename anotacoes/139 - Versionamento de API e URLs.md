# Versionamento de API e Estrutura de URLs no Django

Versionar uma API é uma prática importante para manter a compatibilidade ao longo do tempo, permitindo que diferentes versões da API coexistam sem interrupções para os clientes. No Django, uma maneira comum de implementar o versionamento é por meio das rotas (`urls`), organizando-as para refletir diferentes versões da API.

### Reestruturação de URLs

Neste exemplo, movemos as rotas (`urls`) de cada aplicação do projeto Django para dentro dos respectivos apps. Isso torna o gerenciamento mais modular e escalável, especialmente em projetos grandes. Além disso, o versionamento é adicionado às rotas principais da API no arquivo `urls.py` da pasta core do projeto.

### Código de Exemplo:

#### Arquivo `urls.py` na pasta Core do Projeto:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.genres.urls')),  # Versionamento da API v1 para o app genres
]
```

- **path('api/v1/', include('apps.genres.urls'))**: Aqui, estamos utilizando a função `include` para incluir as URLs do app `genres` dentro de um caminho de versão da API (`api/v1/`). Isso significa que as rotas do app estarão acessíveis dentro da estrutura da API versionada.

#### Arquivo `urls.py` na pasta do app (`apps/genres/urls.py`):

```python
from django.urls import path
from .views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]
```

Neste arquivo, as URLs específicas do app `genres` estão sendo declaradas:

- **GenreCreateListView**: Rota para listar e criar gêneros (`genres/`).
- **GenreRetrieveUpdateDestroyView**: Rota para recuperar, atualizar ou deletar um gênero específico com base no seu `id` (`genres/<int:pk>`).

### Vantagens do Versionamento de API e Estrutura Modular:

1. **Organização Modular**: Mover as rotas para dentro de cada app torna o projeto mais organizado e permite que cada app tenha controle sobre suas próprias rotas.
  
2. **Facilidade de Atualizações**: Ao versionar a API, podemos criar novas versões sem afetar os clientes que estão utilizando versões antigas. Exemplo:
   - `api/v1/genres/`: Rota da versão 1 da API.
   - `api/v2/genres/`: Rota da versão 2 da API, que pode ter mudanças no comportamento ou na estrutura de resposta.

3. **Escalabilidade**: Com a estrutura modular e o versionamento, fica mais fácil manter e escalar o projeto, adicionando novas versões da API e novos apps de forma independente.
