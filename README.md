Este projeto é baseado no projeto ensinado no curso Django Master, que abrange a criação de aplicações completas utilizando Django e Django Rest Framework (DRF). O projeto exemplifica boas práticas no desenvolvimento web com Django, integrando autenticação, autorização, CRUD, e muito mais.

## Requisitos

1. **Variáveis de Ambiente**:
   - O projeto utiliza variáveis de ambiente para configuração. É necessário criar um arquivo `.env` baseado no `envexample` fornecido.
   
2. **Dependências**:
   - Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`.

## Configuração do Ambiente

### 1. Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

### 2. Criar e Ativar um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate   # No Windows, use `venv\Scripts\activate`
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

- Crie um arquivo `.env` na raiz do projeto.
- Copie o conteúdo do arquivo `envexample` para o arquivo `.env`.
- Ajuste as configurações conforme necessário, como informações do banco de dados, chaves secretas, etc.

### 5. Criar o Projeto Django

- Navegue até o diretório raiz do projeto e execute o comando abaixo para criar um novo projeto Django:

```bash
django-admin startproject config .
```

### 6. Aplicar Migrações

- Após criar o projeto Django, aplique as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```

### 7. Criar um Superusuário

- Crie um superusuário para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

### 8. Iniciar o Servidor de Desenvolvimento

- Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

## Estrutura do Projeto

- O projeto segue uma estrutura organizada para facilitar a manutenção e expansão.

```
<ROOT_PROJECT>
├── apps
│   ├── actors
│   ├── genres
│   ├── movies
│   └── ...
├── core
│   ├── permissions.py
│   └── ...
├── requirements.txt
├── envexample
├── .env
└── manage.py
```

## Principais Funcionalidades

- **Autenticação JWT**: Implementação de autenticação segura utilizando JWT.
- **CRUD Completo**: Funcionalidades de Create, Read, Update e Delete implementadas em diferentes módulos.
- **Permissões Personalizadas**: Controle de acesso detalhado utilizando classes de permissão personalizadas.
- **Serialização e Validações**: Utilização de serializers do DRF para validação e transformação de dados.

## Notas Finais

Este projeto serve como uma base sólida para desenvolvimento de aplicações web completas com Django e Django Rest Framework. Sinta-se à vontade para expandir e modificar conforme suas necessidades. Para dúvidas ou mais informações, consulte a documentação oficial do Django e do Django Rest Framework.