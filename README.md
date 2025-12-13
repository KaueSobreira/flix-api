# 🎬 Flix-API

API REST desenvolvida em Django para gerenciamento de gêneros de filmes e séries. Projeto criado com fins educacionais para aprendizado de Django REST Framework.

## 📋 Sobre o Projeto

O **Flix-API** é uma API REST simples desenvolvida utilizando Django e Django REST Framework. O projeto foi criado com o objetivo de estudar e praticar os conceitos fundamentais de desenvolvimento de APIs REST, incluindo operações CRUD (Create, Read, Update, Delete) e serialização de dados.

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

### Gêneros (Genres)

#### Listar todos os gêneros / Criar novo gênero
- **GET** `/genres/` - Lista todos os gêneros cadastrados
- **POST** `/genres/` - Cria um novo gênero

**Exemplo de requisição POST:**
```json
{
  "name": "Ação"
}
```

#### Obter, atualizar ou deletar um gênero específico
- **GET** `/genres/<id>/` - Retorna um gênero específico
- **PUT** `/genres/<id>/` - Atualiza um gênero específico
- **DELETE** `/genres/<id>/` - Deleta um gênero específico

### Admin
- **GET** `/admin/` - Interface administrativa do Django

## 🧪 Exemplos de Uso

### Listar todos os gêneros
```bash
curl http://127.0.0.1:8000/genres/
```

### Criar um novo gênero
```bash
curl -X POST http://127.0.0.1:8000/genres/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Comédia"}'
```

### Obter um gênero específico
```bash
curl http://127.0.0.1:8000/genres/1/
```

### Atualizar um gênero
```bash
curl -X PUT http://127.0.0.1:8000/genres/1/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Ação e Aventura"}'
```

### Deletar um gênero
```bash
curl -X DELETE http://127.0.0.1:8000/genres/1/
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
│   └── ...
├── db.sqlite3           # Banco de dados SQLite
├── manage.py            # Script de gerenciamento do Django
└── requeriments.txt     # Dependências do projeto
```

## 🎯 Funcionalidades

- ✅ CRUD completo de gêneros
- ✅ API RESTful seguindo as melhores práticas
- ✅ Serialização de dados com Django REST Framework
- ✅ Interface administrativa do Django
- ✅ Banco de dados SQLite

## 📝 Modelo de Dados

### Genre
- `id` (Integer, Primary Key, Auto)
- `name` (CharField, max_length=200)

## 🎓 Objetivos de Aprendizado

Este projeto foi desenvolvido com o objetivo de:

- Aprender os fundamentos do Django REST Framework
- Praticar a criação de APIs REST
- Entender serialização de dados
- Implementar operações CRUD
- Trabalhar com views genéricas do DRF
- Compreender a estrutura de projetos Django

## 📄 Licença

Este projeto foi criado apenas para fins educacionais e de aprendizado.

## 👤 Autor
Kaue Sobreira Lucena
Desenvolvido como projeto de estudos.

---

**Nota:** Este é um projeto educacional. Para uso em produção, considere adicionar autenticação, validações mais robustas, testes automatizados e outras melhorias de segurança e performance.

