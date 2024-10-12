### ModelSerializer e Validações no Django Rest Framework

O `ModelSerializer` no Django Rest Framework (DRF) oferece uma maneira simples de converter automaticamente os dados de um modelo Django em formatos que podem ser serializados (como JSON). Ele gera os campos com base no modelo e permite definir validações personalizadas para garantir que os dados atendam a critérios específicos.

No exemplo abaixo, temos um serializer para o modelo `Movie`, que inclui validações personalizadas em dois campos: `release_date` e `resume`.

```python
from rest_framework import serializers
from apps.movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve ser maior do que 200 caracteres.')
        return value
```

#### 1. **Definição de ModelSerializer**

No código acima, `MovieSerializer` é um **ModelSerializer**, o que significa que ele gera automaticamente todos os campos do modelo `Movie`. A linha `fields = '__all__'` especifica que todos os campos do modelo serão incluídos no serializer.

Essa abordagem economiza tempo ao não precisar declarar cada campo manualmente, permitindo que a estrutura do modelo seja diretamente refletida na API.

#### 2. **Validações Customizadas**

Embora o `ModelSerializer` forneça validações automáticas com base nos tipos de campo do modelo (por exemplo, garantir que um campo inteiro seja de fato um número inteiro), você pode definir **validações personalizadas** para necessidades específicas.

##### 2.1. `validate_<field_name>`: Validação para `release_date`

A função `validate_release_date` é uma validação personalizada para o campo `release_date`. Esta função é chamada automaticamente quando o campo `release_date` é submetido para validação.

- **Lógica**: A função verifica se o ano da data de lançamento do filme é anterior a 1990. Caso seja, uma exceção `serializers.ValidationError` é lançada com uma mensagem personalizada.
  
```python
def validate_release_date(self, value):
    if value.year < 1990:
        raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
    return value
```

- **Exemplo**: Se um filme lançado em 1985 for enviado, a API retornará um erro com a mensagem `"A data de lançamento não pode ser anterior a 1990."`

##### 2.2. `validate_<field_name>`: Validação para `resume`

A função `validate_resume` é usada para garantir que o resumo do filme não exceda um limite de caracteres.

- **Lógica**: Esta função valida se o comprimento do texto no campo `resume` não é maior do que 200 caracteres. Caso ultrapasse esse limite, um erro de validação é levantado.
  
```python
def validate_resume(self, value):
    if len(value) > 200:
        raise serializers.ValidationError('Resumo não deve ser maior do que 200 caracteres.')
    return value
```

- **Exemplo**: Se o resumo do filme enviado contiver 250 caracteres, a API retornará o erro `"Resumo não deve ser maior do que 200 caracteres."`

#### 3. **Como Funciona a Validação?**

Ao submeter dados para a API (por exemplo, ao criar ou atualizar um filme), o DRF chama automaticamente as funções de validação:

- Cada campo é validado usando as validações nativas (por exemplo, tipos de dados).
- Para campos que possuem métodos `validate_<field_name>`, as funções de validação personalizada são executadas.

Se um dos métodos de validação levantar uma exceção, o processo de serialização falha e o usuário recebe uma resposta detalhando os erros.

#### 4. **Vantagens da Validação no Serializer**

- **Centralização da Lógica**: A validação de dados está centralizada no serializer, facilitando a manutenção e a leitura do código.
- **Mensagens de Erro Personalizadas**: Você pode fornecer mensagens de erro específicas e úteis para os usuários, aumentando a clareza.
- **Prevenção de Dados Inválidos**: Garante que os dados enviados para a API atendam aos critérios esperados antes de serem processados ou salvos no banco de dados.
