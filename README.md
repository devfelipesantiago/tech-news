# Tech News

Um projeto em Python com foco em **Web Scraping** e **Análise de Dados** de notícias de tecnologia. O projeto realiza a extração de dados da página de novidades do site [TecMundo](https://www.tecmundo.com.br/novidades), salva essas informações em um banco de dados MongoDB e disponibiliza uma interface interativa via linha de comando (CLI) para realizar consultas e análises sobre os dados extraídos.

## 🚀 Funcionalidades

- **Raspagem de Dados (Scraping):** Obtém as últimas notícias do TecMundo, extraindo detalhes como título, URL, data, autor, resumo, categorias, fontes, e quantidade de comentários/compartilhamentos.
- **Armazenamento:** Persiste todas as informações coletadas em um banco de dados **MongoDB**.
- **Motor de Busca:**
  - Buscar notícias por **título** (case insensitive).
  - Buscar notícias por **data** de publicação (formato YYYY-MM-DD).
  - Buscar notícias por **fonte**.
  - Buscar notícias por **categoria**.
- **Análises:**
  - Identificar as **Top 5 Notícias** mais populares, baseando-se no engajamento (comentários + compartilhamentos).
  - Identificar as **Top 5 Categorias** mais frequentes no banco de dados.
- **Menu Interativo (CLI):** Uma interface amigável no terminal para acionar a raspagem e interagir com o motor de busca sem precisar escrever código.

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** - Linguagem base do projeto.
- **[Requests](https://docs.python-requests.org/)** - Biblioteca para realizar requisições HTTP e capturar o HTML das páginas.
- **[Parsel](https://parsel.readthedocs.io/)** - Biblioteca para extrair dados do HTML utilizando seletores CSS e XPath.
- **[MongoDB](https://www.mongodb.com/)** - Banco de dados NoSQL orientado a documentos utilizado para armazenar as notícias.
- **[PyMongo](https://pymongo.readthedocs.io/)** - Driver do Python para se comunicar com o MongoDB.
- **[Pytest](https://docs.pytest.org/)** - Framework para execução de testes unitários.
- **[Flake8](https://flake8.pycqa.org/)** - Ferramenta de linter para garantir a qualidade e a formatação do código.

## ⚙️ Pré-requisitos

Para rodar este projeto localmente, certifique-se de ter os seguintes serviços e ferramentas instalados:
- **Python 3**
- **MongoDB** rodando na sua máquina (porta padrão `27017`) ou um cluster remoto configurado nas variáveis de ambiente.

## 🏃 Como executar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/devfelipesantiago/tech-news.git
   ```

2. **Entre no diretório do projeto:**
   ```bash
   cd tech-news
   ```

3. **Crie e ative um ambiente virtual (Recomendado):**
   ```bash
   python3 -m venv .venv
   
   # Linux / macOS:
   source .venv/bin/activate
   
   # Windows:
   .venv\Scripts\activate
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r dev-requirements.txt
   ```

5. **Garanta que o MongoDB está rodando:**
   Se estiver no Linux e usando systemd:
   ```bash
   sudo systemctl start mongod
   ```
   *(Caso utilize Windows/Mac ou Docker, inicie o serviço do MongoDB de acordo com o seu ambiente)*

6. **Execute o menu interativo:**
   O projeto já configura um atalho para execução do CLI. Basta rodar:
   ```bash
   tech-news-analyzer
   ```

## 🧪 Como rodar os testes

Com o ambiente virtual ativado e as dependências instaladas, você pode executar a suíte de testes usando o comando:

```bash
python3 -m pytest
```

Para encerrar a execução no primeiro erro encontrado, utilize a flag `-x`:
```bash
python3 -m pytest -x
```

Para verificar o padrão de estilo de código (linter):
```bash
python3 -m flake8
```

## 📝 Sobre o Projeto

Este projeto foi desenvolvido originalmente como parte das atividades práticas do módulo de **Ciência da Computação** do curso de Desenvolvimento Web da [Trybe](https://www.betrybe.com/). O foco principal deste exercício foi introduzir os conceitos de raspagem de dados (Web Scraping), manipulação de dados não-relacionais no MongoDB, e fixar a sintaxe e as boas práticas de programação em Python.
