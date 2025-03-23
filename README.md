# 🔐 Sistema de Autenticação com CPF em Django

Sistema web com autenticação de usuários via CPF, desenvolvido com Django e PostgreSQL. Conta com cadastro de usuários, recuperação de senha e uma interface responsiva com Bootstrap 5.

## ✨ Funcionalidades

- Login com CPF para usuários comuns
- Login com username para superusuário
- Cadastro com validação de nome, CPF, e-mail, senha e username
- Recuperação de senha por e-mail
- Painel restrito pós-login
- Interface moderna com Bootstrap

## 🧰 Tecnologias Utilizadas

- Python 3.12
- Django 5.1
- PostgreSQL
- Bootstrap 5

## ⚙️ Como rodar o projeto

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

# 2. Crie e ative o ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Realize as migrações
python manage.py migrate

# 5. Crie um superusuário
python manage.py createsuperuser

# 6. Inicie o servidor
python manage.py runserver
```

## 🗃️ Estrutura de Pastas

```
.
├── contas/                 # App responsável pela autenticação
├── setup/                  # Configurações principais do projeto
├── templates/              # Templates HTML com Bootstrap
│   ├── base.html
│   └── contas/
│       ├── login.html
│       ├── cadastro.html
│       └── ...
├── manage.py
└── requirements.txt
```

## 📌 Observações

- O login é feito via CPF para usuários comuns.
- Superusuários continuam utilizando o campo `username`.
- E-mails de recuperação são exibidos no terminal (modo desenvolvimento).

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
