# 🎬 Flix-API

API REST desenvolvida em Django para gerenciamento completo de filmes, incluindo gêneros, atores, filmes e avaliações. Projeto criado com fins educacionais para aprendizado de Django REST Framework.

## 📋 Sobre o Projeto

O **Flix-API** é uma API REST completa desenvolvida utilizando Django e Django REST Framework. O projeto foi criado com o objetivo de estudar e praticar os conceitos fundamentais de desenvolvimento de APIs REST, incluindo operações CRUD (Create, Read, Update, Delete), serialização de dados, relacionamentos entre modelos e validações.

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Django 6.0** - Framework web Python
- **Django REST Framework 3.16.1** - Framework para construção de APIs REST
- **Django REST Framework Simple JWT 5.5.1** - Autenticação JWT
- **DRF Spectacular 0.29.0** - Documentação automática da API (Swagger/OpenAPI)
- **Python-dotenv 1.2.1** - Gerenciamento de variáveis de ambiente
- **SQLite** - Banco de dados relacional

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (para clonar o repositório)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/flix-api.git
cd flix-api
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requeriments.txt
```

5. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione a seguinte variável:
   ```env
   SECRET_KEY=sua-chave-secreta-aqui
   ```
   - Você pode gerar uma chave secreta usando:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

6. Execute as migrações do banco de dados:
```bash
python manage.py migrate
```

7. Crie um superusuário para acessar o admin e obter permissões:
```bash
python manage.py createsuperuser
```

8. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`

## 📚 Endpoints da API

Todos os endpoints estão disponíveis sob o prefixo `/api/v1/`

**⚠️ IMPORTANTE:** Todos os endpoints (exceto autenticação e documentação) requerem autenticação JWT. Você precisa obter um token de acesso antes de fazer requisições.

### Autenticação (Authentication)

#### Obter token de acesso
- **POST** `/api/v1/authentication/token/` - Obtém um token de acesso e refresh token

**Exemplo de requisição:**
```json
{
  "username": "seu-usuario",
  "password": "sua-senha"
}
```

**Resposta:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Atualizar token de acesso
- **POST** `/api/v1/authentication/token/refresh/` - Atualiza o token de acesso usando o refresh token

**Exemplo de requisição:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Verificar token
- **POST** `/api/v1/authentication/token/verify/` - Verifica se um token é válido

**Exemplo de requisição:**
```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Como usar o token nas requisições:**
Adicione o header `Authorization` com o valor `Bearer <seu-token>`:
```bash
curl -H "Authorization: Bearer seu-token-aqui" http://127.0.0.1:8000/api/v1/genres/
```

### Documentação da API

#### Swagger UI
- **GET** `/api/v1/swagger/` - Interface interativa Swagger para testar a API

#### Schema OpenAPI
- **GET** `/api/v1/api/schema/` - Schema OpenAPI em formato JSON/YAML

### Gêneros (Genres)
**Requer autenticação JWT**

#### Listar todos os gêneros / Criar novo gênero
- **GET** `/api/v1/genres/` - Lista todos os gêneros cadastrados
- **POST** `/api/v1/genres/` - Cria um novo gênero

**Exemplo de requisição POST:**
```json
{
  "name": "Ação"
}
```

#### Obter, atualizar ou deletar um gênero específico
- **GET** `/api/v1/genres/<id>/` - Retorna um gênero específico
- **PUT** `/api/v1/genres/<id>/` - Atualiza um gênero específico
- **DELETE** `/api/v1/genres/<id>/` - Deleta um gênero específico

### Atores (Actors)
**Requer autenticação JWT**

#### Listar todos os atores / Criar novo ator
- **GET** `/api/v1/actors/` - Lista todos os atores cadastrados
- **POST** `/api/v1/actors/` - Cria um novo ator

**Exemplo de requisição POST:**
```json
{
  "name": "Leonardo DiCaprio",
  "birthday": "1974-11-11",
  "nationality": "USA"
}
```

**Opções de nacionalidade:** `USA`, `BRAZIL`, `ARG`

#### Obter, atualizar ou deletar um ator específico
- **GET** `/api/v1/actors/<id>/` - Retorna um ator específico
- **PUT** `/api/v1/actors/<id>/` - Atualiza um ator específico
- **DELETE** `/api/v1/actors/<id>/` - Deleta um ator específico

### Filmes (Movies)
**Requer autenticação JWT**

#### Listar todos os filmes / Criar novo filme
- **GET** `/api/v1/movies/` - Lista todos os filmes cadastrados
- **POST** `/api/v1/movies/` - Cria um novo filme

**Exemplo de requisição POST:**
```json
{
  "title": "Inception",
  "genre": 1,
  "release_date": "2010-07-16",
  "actors": [1, 2],
  "resume": "Um ladrão que invade os sonhos das pessoas..."
}
```

#### Obter, atualizar ou deletar um filme específico
- **GET** `/api/v1/movies/<id>/` - Retorna um filme específico
- **PUT** `/api/v1/movies/<id>/` - Atualiza um filme específico
- **DELETE** `/api/v1/movies/<id>/` - Deleta um filme específico

### Avaliações (Reviews)
**Requer autenticação JWT**

#### Listar todas as avaliações / Criar nova avaliação
- **GET** `/api/v1/reviews/` - Lista todas as avaliações cadastradas
- **POST** `/api/v1/reviews/` - Cria uma nova avaliação

**Exemplo de requisição POST:**
```json
{
  "movie": 1,
  "stars": 5,
  "comment": "Excelente filme! Muito bem dirigido."
}
```

**Validação:** O campo `stars` deve estar entre 0 e 5.

#### Obter, atualizar ou deletar uma avaliação específica
- **GET** `/api/v1/reviews/<id>/` - Retorna uma avaliação específica
- **PUT** `/api/v1/reviews/<id>/` - Atualiza uma avaliação específica
- **DELETE** `/api/v1/reviews/<id>/` - Deleta uma avaliação específica

### Grupos (Groups)
**Requer autenticação JWT**

#### Listar todos os grupos / Criar novo grupo
- **GET** `/api/v1/groups/` - Lista todos os grupos cadastrados
- **POST** `/api/v1/groups/` - Cria um novo grupo

**Exemplo de requisição POST:**
```json
{
  "name": "Administradores"
}
```

#### Obter, atualizar ou deletar um grupo específico
- **GET** `/api/v1/groups/<id>/` - Retorna um grupo específico
- **PUT** `/api/v1/groups/<id>/` - Atualiza um grupo específico
- **DELETE** `/api/v1/groups/<id>/` - Deleta um grupo específico

### Admin
- **GET** `/admin/` - Interface administrativa do Django

## 🧪 Exemplos de Uso

### Autenticação

#### Obter token de acesso
```bash
curl -X POST http://127.0.0.1:8000/api/v1/authentication/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "seu-usuario", "password": "sua-senha"}'
```

**Salve o token retornado para usar nas próximas requisições.**

#### Atualizar token de acesso
```bash
curl -X POST http://127.0.0.1:8000/api/v1/authentication/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "seu-refresh-token-aqui"}'
```

### Gêneros

#### Listar todos os gêneros
```bash
curl -H "Authorization: Bearer seu-token-aqui" \
  http://127.0.0.1:8000/api/v1/genres/
```

#### Criar um novo gênero
```bash
curl -X POST http://127.0.0.1:8000/api/v1/genres/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer seu-token-aqui" \
  -d '{"name": "Comédia"}'
```

#### Obter um gênero específico
```bash
curl -H "Authorization: Bearer seu-token-aqui" \
  http://127.0.0.1:8000/api/v1/genres/1/
```

### Atores

#### Criar um novo ator
```bash
curl -X POST http://127.0.0.1:8000/api/v1/actors/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer seu-token-aqui" \
  -d '{"name": "Tom Hanks", "birthday": "1956-07-09", "nationality": "USA"}'
```

#### Listar todos os atores
```bash
curl -H "Authorization: Bearer seu-token-aqui" \
  http://127.0.0.1:8000/api/v1/actors/
```

### Filmes

#### Criar um novo filme
```bash
curl -X POST http://127.0.0.1:8000/api/v1/movies/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer seu-token-aqui" \
  -d '{"title": "Forrest Gump", "genre": 1, "release_date": "1994-07-06", "actors": [1], "resume": "A história de um homem simples..."}'
```

#### Listar todos os filmes
```bash
curl -H "Authorization: Bearer seu-token-aqui" \
  http://127.0.0.1:8000/api/v1/movies/
```

### Avaliações

#### Criar uma nova avaliação
```bash
curl -X POST http://127.0.0.1:8000/api/v1/reviews/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer seu-token-aqui" \
  -d '{"movie": 1, "stars": 5, "comment": "Filme incrível!"}'
```

#### Listar todas as avaliações
```bash
curl -H "Authorization: Bearer seu-token-aqui" \
  http://127.0.0.1:8000/api/v1/reviews/
```

### Grupos

#### Listar todos os grupos
```bash
curl -H "Authorization: Bearer seu-token-aqui" \
  http://127.0.0.1:8000/api/v1/groups/
```

#### Criar um novo grupo
```bash
curl -X POST http://127.0.0.1:8000/api/v1/groups/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer seu-token-aqui" \
  -d '{"name": "Administradores"}'
```

### Documentação Swagger

#### Acessar a documentação interativa
Abra no navegador: `http://127.0.0.1:8000/api/v1/swagger/`

## 📁 Estrutura do Projeto

```
flix-api/
├── app/                  # Configurações principais do Django
│   ├── settings.py      # Configurações do projeto
│   ├── urls.py          # URLs principais
│   └── ...
├── genres/              # App de gêneros
│   ├── models.py        # Modelo Genre
│   ├── views.py         # Views da API
│   ├── serializers.py   # Serializers do DRF
│   ├── urls.py          # URLs do app
│   └── ...
├── actors/              # App de atores
│   ├── models.py        # Modelo Actor
│   ├── views.py         # Views da API
│   ├── serializers.py   # Serializers do DRF
│   ├── urls.py          # URLs do app
│   └── ...
├── movies/              # App de filmes
│   ├── models.py        # Modelo Movie
│   ├── views.py         # Views da API
│   ├── serializers.py   # Serializers do DRF
│   ├── urls.py          # URLs do app
│   └── ...
├── reviews/             # App de avaliações
│   ├── models.py        # Modelo Review
│   ├── views.py         # Views da API
│   ├── serializers.py   # Serializers do DRF
│   ├── urls.py          # URLs do app
│   └── ...
├── authentication/      # App de autenticação
│   ├── urls.py          # URLs de autenticação JWT
│   └── ...
├── docs/                # App de documentação
│   ├── urls.py          # URLs do Swagger/OpenAPI
│   └── ...
├── groups/              # App de grupos
│   ├── views.py         # Views da API
│   ├── serializers.py   # Serializers do DRF
│   ├── urls.py          # URLs do app
│   └── ...
├── app/                 # Configurações principais
│   ├── permissions.py   # Permissões customizadas
│   └── ...
├── db.sqlite3           # Banco de dados SQLite
├── manage.py            # Script de gerenciamento do Django
├── requeriments.txt     # Dependências do projeto
└── .env                 # Variáveis de ambiente (criar manualmente)
```

## 🎯 Funcionalidades

- ✅ CRUD completo de gêneros
- ✅ CRUD completo de atores
- ✅ CRUD completo de filmes
- ✅ CRUD completo de avaliações
- ✅ CRUD completo de grupos de usuários
- ✅ Autenticação JWT (JSON Web Tokens)
- ✅ Sistema de permissões baseado em grupos Django
- ✅ Documentação automática da API com Swagger/OpenAPI
- ✅ Relacionamentos entre modelos (ForeignKey e ManyToMany)
- ✅ Validações de dados (estrelas de 0 a 5)
- ✅ API RESTful seguindo as melhores práticas
- ✅ Serialização de dados com Django REST Framework
- ✅ Interface administrativa do Django
- ✅ Banco de dados SQLite
- ✅ Gerenciamento de variáveis de ambiente com python-dotenv
- ✅ Token blacklist para logout seguro

## 📝 Modelo de Dados

### Genre (Gênero)
- `id` (Integer, Primary Key, Auto)
- `name` (CharField, max_length=200)

### Actor (Ator)
- `id` (Integer, Primary Key, Auto)
- `name` (CharField, max_length=200)
- `birthday` (DateField, opcional)
- `nationality` (CharField, max_length=100, opcional)
  - Opções: `USA`, `BRAZIL`, `ARG`

### Movie (Filme)
- `id` (Integer, Primary Key, Auto)
- `title` (CharField, max_length=500)
- `genre` (ForeignKey para Genre)
- `release_date` (DateField, opcional)
- `actors` (ManyToMany para Actor)
- `resume` (TextField, opcional)

### Review (Avaliação)
- `id` (Integer, Primary Key, Auto)
- `movie` (ForeignKey para Movie)
- `stars` (IntegerField, validado entre 0 e 5)
- `comment` (TextField, opcional)

## 🔐 Autenticação e Permissões

### Autenticação JWT

A API utiliza autenticação baseada em JWT (JSON Web Tokens). Para acessar os endpoints protegidos:

1. Obtenha um token fazendo uma requisição POST para `/api/v1/authentication/token/` com suas credenciais
2. Use o token retornado no header `Authorization: Bearer <token>` em todas as requisições
3. O token de acesso expira em 4 horas (configurável)
4. Use o refresh token para obter um novo token de acesso quando necessário

### Sistema de Permissões

A API utiliza um sistema de permissões baseado nos grupos e permissões nativos do Django:

- Cada operação (GET, POST, PUT, DELETE) requer a permissão correspondente
- Permissões seguem o padrão: `<app>.<action>_<model>`
- Exemplos:
  - `genres.view_genre` - Para visualizar gêneros
  - `genres.add_genre` - Para criar gêneros
  - `genres.change_genre` - Para atualizar gêneros
  - `genres.delete_genre` - Para deletar gêneros

**Configurando permissões:**
1. Acesse o admin do Django (`/admin/`)
2. Crie grupos e atribua as permissões necessárias
3. Adicione usuários aos grupos apropriados

## 🎓 Objetivos de Aprendizado

Este projeto foi desenvolvido com o objetivo de:

- Aprender os fundamentos do Django REST Framework
- Praticar a criação de APIs REST
- Entender serialização de dados
- Implementar operações CRUD completas
- Trabalhar com views genéricas do DRF (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
- Compreender a estrutura de projetos Django
- Trabalhar com relacionamentos entre modelos (ForeignKey e ManyToMany)
- Implementar validações de dados
- Organizar URLs com prefixos e includes
- Implementar autenticação JWT
- Trabalhar com sistema de permissões customizadas
- Documentar APIs com Swagger/OpenAPI
- Gerenciar variáveis de ambiente de forma segura

## 📖 Documentação da API

A documentação interativa da API está disponível através do Swagger UI:

- **Swagger UI:** `http://127.0.0.1:8000/api/v1/swagger/`

A documentação inclui:
- Todos os endpoints disponíveis
- Parâmetros de requisição e resposta
- Esquemas de dados
- Possibilidade de testar endpoints diretamente na interface

## 🔧 Configurações Importantes

### Variáveis de Ambiente

O projeto utiliza variáveis de ambiente para configurações sensíveis. Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta-aqui
```

### Configurações JWT

As configurações de JWT podem ser ajustadas em `app/settings.py`:

- `ACCESS_TOKEN_LIFETIME`: Tempo de vida do token de acesso (padrão: 4 horas)
- `REFRESH_TOKEN_LIFETIME`: Tempo de vida do refresh token (padrão: 1 dia)
- `ROTATE_REFRESH_TOKENS`: Rotaciona refresh tokens a cada uso
- `BLACKLIST_AFTER_ROTATION`: Adiciona tokens antigos à blacklist

## 📄 Licença

Este projeto foi criado apenas para fins educacionais e de aprendizado.

## 👤 Autor
Kaue Sobreira Lucena
Desenvolvido como projeto de estudos.

---

**Nota:** Este é um projeto educacional. Para uso em produção, considere adicionar validações mais robustas, testes automatizados, rate limiting, CORS adequado, HTTPS e outras melhorias de segurança e performance.

