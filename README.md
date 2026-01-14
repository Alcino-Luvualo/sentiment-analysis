# 🎭 Sentiment Analysis with TextBlob

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.0+-green?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/TextBlob-NLP-orange?style=for-the-badge" alt="TextBlob">
  <img src="https://img.shields.io/badge/Pylint-10%2F10-brightgreen?style=for-the-badge" alt="Pylint Score">
  <img src="https://img.shields.io/badge/Tests-6%20Passing-success?style=for-the-badge" alt="Tests">
</p>

<p align="center">
  <b>Uma aplicação web moderna para análise de sentimentos usando Processamento de Linguagem Natural (NLP)</b>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-instalação">Instalação</a> •
  <a href="#-como-usar">Como Usar</a> •
  <a href="#-api">API</a> •
  <a href="#-como-funciona">Como Funciona</a>
</p>

---

## ✨ Features

| Feature | Descrição |
|---------|-----------|
| 🔍 **Análise de Sentimentos** | Classifica textos como Positivo, Negativo ou Neutro |
| 🌐 **Interface Web Moderna** | Design responsivo com gradientes e animações |
| 🚀 **API REST** | Endpoint simples para integração |
| 🧪 **Testes Automatizados** | Cobertura completa com unittest |
| 📊 **Pontuação de Polaridade** | Retorna score entre -1.0 e +1.0 |
| 🛡️ **Tratamento de Erros** | Validação robusta de entradas |
| 🇧🇷 **Suporte Português** | Resultados traduzidos para PT-BR |

---

## 🎬 Demo

### Interface Web

A aplicação possui uma interface moderna com design glassmorphism:

```
┌─────────────────────────────────────────────┐
│           🎭 Sentiment Analyzer             │
│      Análise de Sentimentos com TextBlob    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │ I love working with Python!        │    │
│  └─────────────────────────────────────┘    │
│                                             │
│         [🔍 Analisar Sentimento]            │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │ ✅ POSITIVO - Score: 0.5           │    │
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

### Exemplos de Análise

| Texto | Classificação | Score |
|-------|---------------|-------|
| "I love this product!" | 😊 POSITIVO | +0.50 |
| "This is terrible" | 😠 NEGATIVO | -0.80 |
| "The meeting is at 3pm" | 😐 NEUTRO | 0.00 |

---

## 📦 Instalação

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/alcino-luvualo/sentiment-analysis.git
cd sentiment-analysis
```

2. **Crie um ambiente virtual**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate   # Windows
```

3. **Instale as dependências**
```bash
pip install textblob flask pylint requests
```

4. **Baixe os corpora do TextBlob**
```bash
python -m textblob.download_corpora
```

5. **Execute a aplicação**
```bash
python server.py
```

6. **Acesse no navegador**
```
http://localhost:5000
```

> ⚠️ **Nota:** Se a porta 5000 estiver em uso (comum no macOS), use: `flask --app server run --port 5001`

---

## 🚀 Como Usar

### Via Interface Web

1. Abra o navegador em `http://localhost:5000`
2. Digite um texto no campo de entrada
3. Clique em **"Analisar Sentimento"**
4. Veja o resultado com a classificação e pontuação

### Via API

```bash
# Requisição GET
curl "http://localhost:5000/sentimentAnalyzer?textToAnalyze=I%20love%20Python"

# Resposta
O texto fornecido foi identificado como POSITIVO com uma pontuação de 0.5.
```

### Via Python

```python
from SentimentAnalysis import sentiment_analyzer

# Analisar um texto
result = sentiment_analyzer("I love working with Python")
print(result)
# {'label': 'SENT_POSITIVE', 'score': 0.5}

# Texto negativo
result = sentiment_analyzer("I hate bugs")
print(result)
# {'label': 'SENT_NEGATIVE', 'score': -0.8}
```

---

## 📡 API

### Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/` | Página principal (interface web) |
| `GET` | `/sentimentAnalyzer` | Analisa o sentimento de um texto |

### Parâmetros

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `textToAnalyze` | `string` | Texto a ser analisado |

### Resposta

```json
{
  "label": "SENT_POSITIVE | SENT_NEGATIVE | SENT_NEUTRAL",
  "score": -1.0 a 1.0
}
```

---

## 🧠 Como Funciona

### Arquitetura

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   Interface Web  │────▶│   Flask Server   │────▶│    TextBlob      │
│   (HTML/JS/CSS)  │     │   (server.py)    │     │  (NLP Engine)    │
└──────────────────┘     └──────────────────┘     └──────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
    Input do Usuário       Processa Request        Analisa Sentimento
```

### Algoritmo de Análise

O TextBlob usa um **classificador Naive Bayes** treinado com o corpus de críticas de filmes:

1. **Tokenização** - Quebra o texto em palavras
2. **Lookup Léxico** - Busca polaridade de cada palavra
3. **Média Ponderada** - Calcula polaridade final
4. **Classificação** - Aplica thresholds

```python
if polarity > 0.1:
    label = "SENT_POSITIVE"   # 😊
elif polarity < -0.1:
    label = "SENT_NEGATIVE"   # 😠
else:
    label = "SENT_NEUTRAL"    # 😐
```

### Escala de Polaridade

```
Negativo ◄─────────────────────────────────────────► Positivo
   -1.0        -0.5        0.0        +0.5        +1.0
    │           │           │           │           │
  Muito      Negativo    Neutro    Positivo     Muito
 Negativo                                      Positivo
```

---

## 📁 Estrutura do Projeto

```
sentiment-analysis/
├── 📂 SentimentAnalysis/           # Pacote Python
│   ├── __init__.py                 # Exporta sentiment_analyzer
│   └── sentiment_analysis.py       # Função de análise
├── 📂 templates/                   # Templates HTML
│   └── index.html                  # Interface web
├── 📂 static/                      # Arquivos estáticos
│   └── mywebscript.js              # JavaScript do frontend
├── 📂 venv/                        # Ambiente virtual
├── server.py                       # Servidor Flask
├── test_sentiment_analysis.py      # Testes unitários
├── .gitignore                      # Arquivos ignorados pelo Git
├── LICENSE                         # Licença do projeto
└── README.md                       # Este arquivo
```

---

## 🧪 Testes

### Executar Testes

```bash
python test_sentiment_analysis.py
```

### Resultado Esperado

```
......
----------------------------------------------------------------------
Ran 6 tests in 0.020s

OK
```

### Cobertura de Testes

| Teste | Descrição |
|-------|-----------|
| `test_positive_sentiment` | Verifica análise de texto positivo |
| `test_negative_sentiment` | Verifica análise de texto negativo |
| `test_neutral_sentiment` | Verifica análise de texto neutro |
| `test_empty_input` | Verifica tratamento de entrada vazia |
| `test_whitespace_input` | Verifica entrada apenas com espaços |
| `test_none_input` | Verifica entrada None |

---

## 📊 Qualidade de Código

### Pylint Score

```bash
pylint server.py
# Your code has been rated at 10.00/10

pylint SentimentAnalysis/sentiment_analysis.py
# Your code has been rated at 9.52/10
```

---

## 🔧 Tecnologias

| Tecnologia | Uso |
|------------|-----|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | Linguagem principal |
| ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white) | Framework web |
| ![TextBlob](https://img.shields.io/badge/-TextBlob-yellow) | Motor de NLP |
| ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white) | Estrutura da interface |
| ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?logo=css3&logoColor=white) | Estilização |
| ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black) | Interatividade |

---

## 🆚 Comparação: TextBlob vs Watson

| Aspecto | TextBlob | Watson NLU |
|---------|----------|------------|
| 💰 **Custo** | Gratuito | Pago |
| 🌐 **Internet** | Offline | Requer conexão |
| 🎯 **Precisão** | Média (Naive Bayes) | Alta (BERT/Transformers) |
| ⚡ **Velocidade** | Muito rápido | Mais lento (API) |
| 📦 **Instalação** | `pip install textblob` | SDK + API Key |
| 🔒 **Privacidade** | Local | Dados enviados à IBM |

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Alcino Luvualo**

[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github)](https://github.com/Alcino-Luvualo)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/alcino-luvualo)

---

## 🙏 Agradecimentos

- [TextBlob](https://textblob.readthedocs.io/) - Biblioteca de NLP
- [Flask](https://flask.palletsprojects.com/) - Micro framework web
- [NLTK](https://www.nltk.org/) - Natural Language Toolkit

---

<p align="center">
  Feito com ❤️ e ☕ | 2026
</p>
