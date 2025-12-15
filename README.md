# 🎬 Flix-API

API REST desenvolvida em Django para gerenciamento completo de filmes, incluindo gêneros, atores, filmes e avaliações. Projeto criado com fins educacionais para aprendizado de Django REST Framework.

## 📋 Sobre o Projeto

O **Flix-API** é uma API REST completa desenvolvida utilizando Django e Django REST Framework. O projeto foi criado com o objetivo de estudar e praticar os conceitos fundamentais de desenvolvimento de APIs REST, incluindo operações CRUD (Create, Read, Update, Delete), serialização de dados, relacionamentos entre modelos e validações.

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Django 6.0** - Framework web Python
- **Django REST Framework 3.16.1** - Framework para construção de APIs REST
- **SQLite** - Banco de dados relacional

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

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

5. Execute as migrações do banco de dados:
```bash
python manage.py migrate
```

6. (Opcional) Crie um superusuário para acessar o admin:
```bash
python manage.py createsuperuser
```

7. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`

## 📚 Endpoints da API

Todos os endpoints estão disponíveis sob o prefixo `/api/v1/`

### Gêneros (Genres)

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

### Admin
- **GET** `/admin/` - Interface administrativa do Django

## 🧪 Exemplos de Uso

### Gêneros

#### Listar todos os gêneros
```bash
curl http://127.0.0.1:8000/api/v1/genres/
```

#### Criar um novo gênero
```bash
curl -X POST http://127.0.0.1:8000/api/v1/genres/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Comédia"}'
```

#### Obter um gênero específico
```bash
curl http://127.0.0.1:8000/api/v1/genres/1/
```

### Atores

#### Criar um novo ator
```bash
curl -X POST http://127.0.0.1:8000/api/v1/actors/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Tom Hanks", "birthday": "1956-07-09", "nationality": "USA"}'
```

#### Listar todos os atores
```bash
curl http://127.0.0.1:8000/api/v1/actors/
```

### Filmes

#### Criar um novo filme
```bash
curl -X POST http://127.0.0.1:8000/api/v1/movies/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Forrest Gump", "genre": 1, "release_date": "1994-07-06", "actors": [1], "resume": "A história de um homem simples..."}'
```

#### Listar todos os filmes
```bash
curl http://127.0.0.1:8000/api/v1/movies/
```

### Avaliações

#### Criar uma nova avaliação
```bash
curl -X POST http://127.0.0.1:8000/api/v1/reviews/ \
  -H "Content-Type: application/json" \
  -d '{"movie": 1, "stars": 5, "comment": "Filme incrível!"}'
```

#### Listar todas as avaliações
```bash
curl http://127.0.0.1:8000/api/v1/reviews/
```

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
├── db.sqlite3           # Banco de dados SQLite
├── manage.py            # Script de gerenciamento do Django
└── requeriments.txt     # Dependências do projeto
```

## 🎯 Funcionalidades

- ✅ CRUD completo de gêneros
- ✅ CRUD completo de atores
- ✅ CRUD completo de filmes
- ✅ CRUD completo de avaliações
- ✅ Relacionamentos entre modelos (ForeignKey e ManyToMany)
- ✅ Validações de dados (estrelas de 0 a 5)
- ✅ API RESTful seguindo as melhores práticas
- ✅ Serialização de dados com Django REST Framework
- ✅ Interface administrativa do Django
- ✅ Banco de dados SQLite

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

## 📄 Licença

Este projeto foi criado apenas para fins educacionais e de aprendizado.

## 👤 Autor
Kaue Sobreira Lucena
Desenvolvido como projeto de estudos.

---

**Nota:** Este é um projeto educacional. Para uso em produção, considere adicionar autenticação, validações mais robustas, testes automatizados e outras melhorias de segurança e performance.

