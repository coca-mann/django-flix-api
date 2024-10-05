# Criar Apps e Mover para Dentro de uma Pasta no Django

Organizar seus aplicativos em uma pasta específica é uma prática comum que pode ajudar a manter a estrutura do projeto Django limpa e organizada. Um exemplo dessa organização é mover todos os apps criados para dentro de uma pasta chamada `apps`. A seguir, explico como realizar esse procedimento e garantir que o app continue funcional e totalmente integrado ao projeto.

## Passos para Criar e Mover um App para a Pasta `apps`

1. **Criar o App**:
   Crie seu app Django normalmente utilizando o comando:
   ```bash
   python manage.py startapp nome_do_app
   ```
   Isso vai gerar a estrutura padrão do app no diretório atual.

2. **Mover o App para a Pasta `apps`**:
   Após a criação do app, mova a pasta gerada (por exemplo, `nome_do_app`) para dentro de uma pasta chamada `apps`. Se a pasta `apps` não existir, crie-a na raiz do seu projeto:
   ```bash
   mkdir apps
   ```
   Agora mova o app para dentro dela:
   ```bash
   mv nome_do_app apps/
   ```

3. **Atualizar o `INSTALLED_APPS`**:
   No arquivo `settings.py`, você precisa atualizar a lista de `INSTALLED_APPS` para refletir o novo caminho do app. Substitua a referência original:
   ```python
   'nome_do_app',
   ```
   por:
   ```python
   'apps.nome_do_app',
   ```

4. **Ajustar o Arquivo `apps.py`**:
   No arquivo `apps/nome_do_app/apps.py`, você deve ajustar o caminho do app. O campo `name` na classe `AppConfig` precisa refletir a nova localização:
   ```python
   class NomeDoAppConfig(AppConfig):
       default_auto_field = 'django.db.models.BigAutoField'
       name = 'apps.nome_do_app'
   ```

5. **Usar em Outros Arquivos**:
   Sempre que precisar importar algo do seu app, lembre-se de utilizar o novo caminho. Por exemplo, se for importar um modelo ou uma view, use o caminho `apps.nome_do_app`:
   ```python
   from apps.nome_do_app.models import ModeloExemplo
   from apps.nome_do_app.views import ViewExemplo
   ```

## Benefícios da Organização

Organizar seus apps dentro de uma pasta dedicada, como `apps`, melhora a escalabilidade do projeto, facilita a navegação em grandes códigos e segue boas práticas de arquitetura em Django. Dessa forma, seu projeto se mantém modular e bem estruturado, facilitando o gerenciamento conforme ele cresce.