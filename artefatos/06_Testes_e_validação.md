### Fluxo de Autenticação

1. **Registro:** O usuário fornece um nome de usuário, email e senha. A senha é criptografada usando um algoritmo de hash seguro (ex: bcrypt) antes de ser armazenada no banco de dados.  Um email de confirmação pode ser enviado para verificar o endereço de email.

2. **Login:** O usuário fornece seu nome de usuário ou email e senha. O sistema recupera a senha hasheada do banco de dados e compara com o hash da senha fornecida pelo usuário. Se os hashes corresponderem, a autenticação é bem-sucedida.

3. **Geração de Token JWT (JSON Web Token):** Após a autenticação bem-sucedida, um token JWT é gerado. Este token contém informações sobre o usuário, como ID e privilégios, e é assinado com uma chave secreta.

4. **Autenticação subsequente:** Em solicitações subsequentes, o usuário inclui o token JWT no cabeçalho da requisição (ex: `Authorization: Bearer <token>`). O backend valida o token, verificando sua assinatura e expiração. Se o token for válido, o usuário é autenticado.

5. **Recuperação de Senha:** O usuário fornece seu email. Se o email existir no banco de dados, um link de redefinição de senha é enviado para o email. Este link leva o usuário a uma página onde ele pode definir uma nova senha.

### Tecnologias/Bibliotecas

* **Python:** Linguagem de programação principal do backend.
* **Flask/Django:** Frameworks web Python para construir a API RESTful.
* **PyJWT:** Biblioteca Python para gerar e verificar tokens JWT.
* **bcrypt:** Biblioteca Python para hashing de senhas.
* **SQLAlchemy/ORM:** Para interação com o banco de dados.  (Escolha um ORM dependendo do framework escolhido)
* **Banco de dados:** PostgreSQL ou MySQL (recomendado por sua segurança e estabilidade).


### Considerações de Segurança

* **Hashing de senhas:** Utilizar um algoritmo de hash unidirecional forte e resistente a ataques de força bruta, como bcrypt.  Nunca armazenar senhas em texto plano.
* **Validação de entrada:** Validar todas as entradas do usuário para prevenir injeções de SQL e outros ataques.
* **Proteção contra CSRF (Cross-Site Request Forgery):** Implementar medidas de proteção CSRF, como tokens CSRF.
* **Controle de acesso baseado em funções (RBAC):** Implementar RBAC para controlar o acesso a recursos com base nos privilégios do usuário.
* **Limitação de tentativas de login:** Implementar um mecanismo de limitação de tentativas de login para prevenir ataques de força bruta.
* **HTTPS:** Utilizar HTTPS para todas as comunicações entre o cliente e o servidor.
* **Segurança do banco de dados:** Implementar medidas de segurança no banco de dados, como controle de acesso e auditoria.
* **Atualização regular de bibliotecas:** Manter todas as bibliotecas e dependências atualizadas para corrigir vulnerabilidades de segurança.
* **Tratamento de erros:** Implementar tratamento de erros robusto para prevenir a exposição de informações sensíveis.
* **Teste de segurança:** Realizar testes de segurança regulares para identificar e corrigir vulnerabilidades.


<br>
<hr>
<br>

### 🧠 Instruções para o Agente de Desenvolvimento

**📝 Prompt Complementar:**
Este documento descreve o fluxo de autenticação e as considerações de segurança para o MVP.  A próxima fase de desenvolvimento deve focar na validação do fluxo de autenticação com usuários reais, coletando feedback e dados de uso para identificar problemas de usabilidade e segurança antes de implementar recursos mais complexos.  O objetivo é validar a funcionalidade central de autenticação do MVP e iterar com base nos dados obtidos.


**👍 Instruções Positivas:**
Teste o fluxo de registro e login com um grupo representativo de usuários reais.  Documente todos os problemas encontrados, incluindo erros, mensagens de erro, e dificuldades de usabilidade.  Colete feedback qualitativo através de entrevistas ou questionários, focando na clareza das instruções, na facilidade de uso e na percepção de segurança.  Utilize os dados coletados para refinar a interface do usuário e ajustar o fluxo de autenticação para melhorar a experiência do usuário e a segurança.  Priorize a detecção de erros críticos de segurança, como vulnerabilidades de injeção de SQL ou vulnerabilidades XSS.  Implemente monitoramento básico para acompanhar o sucesso/falha do login e o número de tentativas.  Após os testes, gere um relatório detalhado com os resultados, incluindo as melhorias sugeridas.

**👎 Instruções Negativas:**
Não implemente testes automatizados exaustivos ou cobertura completa de código neste estágio MVP.  Evite investir tempo em recursos de segurança avançados (como autenticação multifator ou auditoria completa) que não sejam essenciais para a funcionalidade básica.  Não se preocupe com a otimização de desempenho ou escalabilidade neste momento.  Evite a implementação de recursos não essenciais relacionados à autenticação (ex: login social) para manter o escopo do MVP.  Não perca tempo em integrações com ferramentas de monitoramento e logging complexas; um monitoramento básico para acompanhar o sucesso/falha do login é suficiente.  Não se preocupe com a internacionalização do sistema neste momento.
