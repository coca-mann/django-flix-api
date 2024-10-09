# Choices no Campo CharField no Django

No Django, o uso de **choices** em um campo como o `CharField` permite que você restrinja os valores que podem ser inseridos em um campo de texto para um conjunto pré-definido de opções. Esse recurso é útil quando você deseja garantir que os dados salvos no banco estejam dentro de um conjunto específico de valores, como no caso de nacionalidades, categorias de produtos, ou tipos de usuário.

### Exemplo com `NATIONALITY_CHOICES`:

No exemplo abaixo, um modelo `Actor` foi criado com um campo `nationality` do tipo `CharField`, onde as opções possíveis de nacionalidade são definidas por uma constante chamada `NATIONALITY_CHOICES`.

#### Código:

```python
from django.db import models

# Definição das opções de nacionalidade
NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('FRANCE', 'França'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,  # Definindo as opções possíveis
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
```

### Explicando as Choices:

1. **Definindo as Opções**:
   - As opções para o campo `nationality` são definidas como uma tupla de tuplas chamada `NATIONALITY_CHOICES`.
   - Cada elemento da tupla externa representa uma opção e é composto por dois valores:
     - O primeiro valor é o que será armazenado no banco de dados (`USA`, `BRAZIL`, `FRANCE`).
     - O segundo valor é a descrição legível que será exibida no formulário para o usuário (`Estados Unidos`, `Brasil`, `França`).

2. **Utilizando no Model**:
   - O campo `nationality` é um `CharField`, mas com a adição do argumento `choices=NATIONALITY_CHOICES`, você limita as opções de entrada do campo para apenas os valores definidos na constante.
   - O argumento `max_length=100` define o tamanho máximo do campo no banco de dados, e `blank=True, null=True` permite que o campo possa ficar em branco ou ser nulo.

### Como Funciona no Django:

- Quando você define um campo com o argumento `choices`, o Django automaticamente gera um campo de seleção (dropdown) no formulário administrativo ou em formulários gerados automaticamente.
- O valor armazenado no banco será sempre o primeiro elemento de cada tupla (`USA`, `BRAZIL`, `FRANCE`), enquanto o usuário verá o segundo valor legível no formulário (`Estados Unidos`, `Brasil`, `França`).

### Exemplo no Formulário:

No formulário de cadastro de um ator no Django Admin, o campo `nationality` será exibido como um dropdown, onde o usuário pode escolher entre "Estados Unidos", "Brasil", ou "França". Ao salvar, o valor armazenado no banco de dados será o código associado, como `USA` para "Estados Unidos".

### Vantagens do Uso de Choices:

- **Validação Automática**: O Django garante que apenas os valores presentes nas `choices` possam ser salvos no banco de dados.
- **Legibilidade**: A separação entre o valor armazenado e a descrição exibida facilita o uso de valores mais curtos e eficientes no banco, ao mesmo tempo em que proporciona uma interface amigável para os usuários.
- **Facilidade de Implementação**: Usar `choices` é uma maneira simples e eficiente de lidar com opções predefinidas em um formulário ou modelo, sem a necessidade de criar tabelas extras ou relacionamentos.
