# O que é JWT (JSON Web Token)?

**JWT (JSON Web Token)** é um padrão para a autenticação segura e troca de informações entre partes através de tokens. Ele é amplamente utilizado para autenticação de usuários em aplicações web e APIs. Em vez de armazenar informações de sessão no servidor, o JWT armazena essas informações no próprio token, que é enviado pelo cliente em cada requisição.

O JWT é composto por três partes principais, separadas por pontos (`.`), que são **codificadas em Base64** e **não criptografadas** por padrão, mas podem ser assinadas ou criptografadas para garantir a segurança e a integridade dos dados.

### Anatomia de um JWT

Um JWT completo tem a seguinte estrutura:

```
xxxxx.yyyyy.zzzzz
```

Ele é dividido em três partes distintas:

1. **Header (Cabeçalho)**:
    - O cabeçalho contém metadados sobre o token, como o algoritmo de assinatura e o tipo de token. Ele é representado em um formato JSON e codificado em Base64.
    
    Exemplo:
    ```json
    {
      "alg": "HS256",
      "typ": "JWT"
    }
    ```
    O campo `"alg"` especifica o algoritmo de assinatura usado, como **HS256** (HMAC com SHA-256). O campo `"typ"` indica que este é um token do tipo JWT.

2. **Payload (Corpo)**:
    - O payload contém as **informações que são transmitidas** no token, conhecidas como **claims**. As claims podem ser informações de autenticação do usuário, permissões, identificadores, etc. Assim como o cabeçalho, o payload também é um JSON e é codificado em Base64.
    
    Exemplo:
    ```json
    {
      "sub": "1234567890",
      "name": "John Doe",
      "iat": 1516239022
    }
    ```
    No exemplo acima:
    - `"sub"` é o ID do assunto ou usuário (subject).
    - `"name"` é o nome do usuário.
    - `"iat"` é o timestamp que indica o momento em que o token foi emitido (issued at).

    O **payload** não é criptografado, por isso, qualquer um que possua o token pode decodificá-lo e ler os dados. Por isso, é importante **não armazenar informações sensíveis** no payload do JWT.

3. **Signature (Assinatura)**:
    - A assinatura é utilizada para **verificar a integridade do token** e garantir que ele não foi alterado. Ela é gerada ao combinar o cabeçalho e o payload com uma chave secreta, utilizando o algoritmo de assinatura especificado no header. 
    
    A assinatura é gerada da seguinte maneira:
    
    ```
    HMACSHA256(
      base64UrlEncode(header) + "." + base64UrlEncode(payload),
      secret
    )
    ```
    O servidor, ao receber um JWT, verifica a assinatura recalculando-a com a chave secreta. Se a assinatura for válida, o token é considerado autêntico.

### Exemplos de Claims Comuns

Dentro do **payload**, alguns claims são comumente usados:

- `iss` (Issuer): Identifica quem emitiu o token.
- `sub` (Subject): Identifica o sujeito ou usuário ao qual o token se refere.
- `aud` (Audience): Define o público que pode usar o token.
- `exp` (Expiration Time): Indica quando o token expira.
- `nbf` (Not Before): Indica o momento a partir do qual o token é válido.
- `iat` (Issued At): Indica quando o token foi emitido.
- `jti` (JWT ID): É um identificador único para o token.

### Vantagens do JWT

- **Autocontido**: O JWT carrega todas as informações necessárias para autenticação no próprio token, o que permite que o servidor não precise de um estado adicional para gerenciar sessões.
- **Escalabilidade**: Como o token contém as informações do usuário, não é necessário armazenar dados de sessão no servidor, facilitando a escalabilidade em arquiteturas distribuídas.
- **Cross-Domain**: O JWT pode ser utilizado para autenticação entre diferentes domínios ou sistemas, já que ele é transmitido via HTTP, WebSockets, etc.

### Desvantagens do JWT

- **Tamanho do Token**: Como o token inclui o payload com informações, ele pode se tornar grande, especialmente se contiver muitos dados, impactando a performance em requisições.
- **Expiração**: Se o token não for invalidado corretamente (por exemplo, após logout), ele pode ser utilizado até expirar, o que pode ser um risco de segurança.
