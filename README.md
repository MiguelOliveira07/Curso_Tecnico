# Curso Técnico: estudos e projetos

Repositório com os exercícios, trabalhos e anotações que desenvolvi durante o **curso técnico em Informática** no Senac. Ele reúne a minha evolução em programação, de `Hello World` até aplicações que consomem APIs, raspam dados da web e gravam em banco de dados.

> Nem tudo aqui é um projeto polido: parte dos arquivos são exercícios de aula e rascunhos, mantidos para mostrar o caminho de aprendizado.

## O que você encontra aqui

| Pasta / arquivo | Conteúdo |
| --- | --- |
| `Básico/Python/Exercicios` | Listas de exercícios em notebooks: estrutura sequencial, condicional, repetição (`for` e `while`), strings, listas, dicionários e funções |
| `orientacao_objs` | Programação orientada a objetos: classes, encapsulamento, herança, composição e agregação |
| `SQL` e `Básico/Python/SQL` | CRUD com SQLite e Python, validação de dados de entrada e atividades de SQL |
| `Banco de dados` | Diagramas de modelagem (draw.io), plano de projeto de um app de agenda de monitoria e exemplos de SQL com Python |
| `API` | Consumo de APIs públicas com `requests` e aplicações web em Streamlit |
| `Básico/Python/Tkinter` | Aplicações desktop com Tkinter e CustomTkinter |
| `Básico/Python/Trabalhos_completos` | Trabalhos concluídos: raspagem de dados, calculadora e app de dados de países |
| `Básico/js_inicio` | Primeiros passos em JavaScript: eventos, manipulação do DOM e calculadora |
| `Básico/xampp` | Testes em PHP: `GET` e `POST`, variáveis e validação com regex |
| `GIT - commands.txt` | Resumo dos comandos de Git que usei no curso |

## Projetos em destaque

**Previsão do tempo** (`API/trabalho_api_01.py`)
App web em Streamlit que recebe o nome de uma cidade, consulta a BrasilAPI (CPTEC) e mostra condição, data e temperaturas mínima e máxima, com tratamento de erro para cidades não encontradas.

**Mundo em Dados** (`API/Trabalho_api_crieApp`)
App em Streamlit que traduz o nome do país, consulta a API Ninjas e a REST Countries e exibe população, PIB, moeda, expectativa de vida e a bandeira do país, com formatação dos valores.

**Busca de CEP** (`Básico/Python/Tkinter/api_cep_formatado.py`)
Aplicação desktop em CustomTkinter que valida o CEP, consulta a ViaCEP, mostra o endereço e permite copiar e limpar os dados.

**Taxa de juros por país** (`Básico/Python/Tkinter/atv_api_juros`)
Aplicação desktop que consulta a taxa de juros de um país na API Ninjas, com leitura da chave em arquivo `secrets.toml` e função preparada para empacotamento em executável.

**Raspagem de dados** (`Básico/Python/Trabalhos_completos/trabalho_raspagem_online`)
Seis scripts com `requests` e BeautifulSoup que coletam nomes e preços de categorias do Mercado Livre (carros novos e usados, eletrodomésticos, jogos, peças de PC e roupas).

**Caçador de Palavras** (`Básico/Python/Exercicios/trabalho_streamlit.py`)
App em Streamlit que raspa os links do Hacker News e gera uma nuvem de palavras.

**CRUD com SQLite** (`SQL/Crud`)
Cadastro de pessoas em SQLite com consultas parametrizadas, campo `UNIQUE` para o RA e funções de validação de nome, RA, data de nascimento e curso.

**Calculadora** (`Básico/js_inicio/calculadora` e `Básico/Python/Tkinter`)
A mesma ideia implementada em duas tecnologias: HTML, CSS e JavaScript no navegador, e Tkinter no desktop.

## Tecnologias

- **Linguagens:** Python, JavaScript, PHP, SQL, HTML e CSS
- **Bibliotecas Python:** `requests`, BeautifulSoup, Streamlit, pandas, matplotlib, WordCloud, Tkinter, CustomTkinter
- **Banco de dados:** SQLite
- **APIs públicas:** ViaCEP, BrasilAPI, API Ninjas, REST Countries e IBGE
- **Ferramentas:** Git e GitHub, Jupyter Notebook, draw.io, XAMPP

## Como executar

### Pré-requisitos

- Python 3.10 ou superior
- Git

### Instalação

```bash
git clone https://github.com/SEU_USUARIO/Curso_Tecnico.git
cd Curso_Tecnico
python -m venv venv
```

Ative o ambiente virtual (`venv\Scripts\activate` no Windows, `source venv/bin/activate` no Linux e macOS) e instale as dependências usadas pelos projetos:

```bash
pip install streamlit requests beautifulsoup4 pandas translate wordcloud matplotlib customtkinter toml
```

### Executando

```bash
# Previsão do tempo (não precisa de chave de API)
streamlit run API/trabalho_api_01.py

# Busca de CEP (aplicação desktop)
python "Básico/Python/Tkinter/api_cep_formatado.py"
```

### Projetos que usam chave de API

O **Mundo em Dados** e o app de **taxa de juros** usam a API Ninjas. O repositório não inclui chaves: crie a sua conta gratuita em [api-ninjas.com](https://api-ninjas.com) e salve a chave em um arquivo local.

Para o Mundo em Dados, crie `API/Trabalho_api_crieApp/.streamlit/secrets.toml`:

```toml
API_KEY = "sua_chave_aqui"
```

Para o app de juros, crie `Básico/Python/Tkinter/atv_api_juros/secrets.toml`:

```toml
[Api]
Api-Key = "sua_chave_aqui"
```

> Nunca envie o `secrets.toml` ao GitHub. Ele já está listado no `.gitignore`.

## Aprendizados

- Evolução de scripts simples para aplicações com interface gráfica e web.
- Consumo de APIs REST, leitura de JSON e tratamento de erros de requisição.
- Raspagem de dados com `requests` e BeautifulSoup.
- Persistência de dados em SQLite com consultas parametrizadas.
- Organização de código com funções e classes (POO).
- Fluxo básico de Git: `add`, `commit`, branches, `pull --rebase` e `push`.

## Licença

Distribuído sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE).

## Contato

- GitHub: https://github.com/MiguelOliveira07
- LinkedIn: www.linkedin.com/in/miguel-oliveria
