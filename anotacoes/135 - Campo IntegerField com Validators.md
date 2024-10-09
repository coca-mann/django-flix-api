# Campo IntegerField com Validators no Django

Os **validators** no Django são funções que garantem que os dados inseridos em um campo atendam a determinadas regras de validação. Isso é útil para assegurar a integridade dos dados no banco e para fornecer feedback ao usuário quando o valor inserido não está dentro dos parâmetros esperados.

No código abaixo, o campo `stars` do modelo `Review` usa dois validators (`MinValueValidator` e `MaxValueValidator`) para garantir que o número de estrelas atribuído a uma avaliação esteja entre 0 e 5.

### Exemplo de Código:

```python
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas.')
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.movie}'
```

### Explicando o Código:

- **ForeignKey**: O campo `movie` é uma chave estrangeira que relaciona a avaliação (`Review`) com o filme (`Movie`). O parâmetro `related_name='reviews'` permite acessar todas as avaliações de um filme através do atributo `reviews`.
- **IntegerField com Validators**: O campo `stars` é um `IntegerField`, que armazena o número de estrelas da avaliação. Para garantir que o valor esteja entre 0 e 5, utilizamos dois validators:
  - `MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas.')`: Garante que o valor mínimo seja 0. Se o valor for menor, a mensagem de erro personalizada será exibida.
  - `MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas.')`: Garante que o valor máximo seja 5, também com uma mensagem de erro personalizada.
- **Comment**: O campo `comment` é um campo de texto (`TextField`), opcional, que pode conter comentários adicionais sobre a avaliação.
- **__str__ Method**: O método `__str__` retorna a representação textual da instância, que neste caso é o título do filme relacionado.

### Outros Exemplos de Validators:

- **DateTimeField**: Você pode aplicar validators para garantir que uma data seja válida ou esteja dentro de um intervalo específico.
  
  ```python
  from django.core.validators import MinValueValidator
  from django.utils import timezone
  
  class Event(models.Model):
      event_date = models.DateTimeField(
          validators=[MinValueValidator(timezone.now, 'A data do evento não pode ser no passado.')]
      )
  ```

  - Aqui, `MinValueValidator` garante que a data do evento não seja anterior à data atual.

- **CharField**: O `CharField` pode ter um validador que limite o tamanho mínimo ou máximo do texto.

  ```python
  from django.core.validators import MinLengthValidator

  class User(models.Model):
      username = models.CharField(
          max_length=50,
          validators=[MinLengthValidator(5, 'O nome de usuário deve ter pelo menos 5 caracteres.')]
      )
  ```

  - `MinLengthValidator` garante que o nome de usuário tenha pelo menos 5 caracteres.

### Retorno do `__str__` em Chaves Estrangeiras:

No modelo `Review`, o método `__str__` retorna o título do filme relacionado. Isso é possível porque o campo `movie` é uma chave estrangeira que aponta para o modelo `Movie`. Quando você utiliza `f'{self.movie}'`, o Django automaticamente chama o método `__str__` do modelo `Movie`, que geralmente retorna o nome ou título do filme.
