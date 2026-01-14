# 🎭 Sentiment Analysis with TextBlob

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.0+-green?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/TextBlob-NLP-orange?style=for-the-badge" alt="TextBlob">
  <img src="https://img.shields.io/badge/Pylint-10%2F10-brightgreen?style=for-the-badge" alt="Pylint Score">
  <img src="https://img.shields.io/badge/Tests-6%20Passing-success?style=for-the-badge" alt="Tests">
</p>

<p align="center">
  <b>A modern web application for sentiment analysis using Natural Language Processing (NLP)</b>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-api">API</a> •
  <a href="#-how-it-works">How It Works</a>
</p>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Sentiment Analysis** | Classifies text as Positive, Negative, or Neutral |
| 🌐 **Modern Web Interface** | Responsive design with gradients and animations |
| 🚀 **REST API** | Simple endpoint for integration |
| 🧪 **Automated Tests** | Full coverage with unittest |
| 📊 **Polarity Score** | Returns score between -1.0 and +1.0 |
| 🛡️ **Error Handling** | Robust input validation |
| 🇧🇷 **Portuguese Support** | Results translated to PT-BR |

---

## 🎬 Demo

### Web Interface

The application features a modern interface with glassmorphism design:

```
┌─────────────────────────────────────────────┐
│           🎭 Sentiment Analyzer             │
│     Sentiment Analysis using TextBlob       │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │ I love working with Python!        │    │
│  └─────────────────────────────────────┘    │
│                                             │
│         [🔍 Analyze Sentiment]              │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │ ✅ POSITIVE - Score: 0.5           │    │
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

### Analysis Examples

| Text | Classification | Score |
|------|----------------|-------|
| "I love this product!" | 😊 POSITIVE | +0.50 |
| "This is terrible" | 😠 NEGATIVE | -0.80 |
| "The meeting is at 3pm" | 😐 NEUTRAL | 0.00 |

---

## 📦 Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Step by Step

1. **Clone the repository**
```bash
git clone https://github.com/alcino-luvualo/sentiment-analysis.git
cd sentiment-analysis
```

2. **Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate   # Windows
```

3. **Install dependencies**
```bash
pip install textblob flask pylint requests
```

4. **Download TextBlob corpora**
```bash
python -m textblob.download_corpora
```

5. **Run the application**
```bash
python server.py
```

6. **Open in browser**
```
http://localhost:5000
```

> ⚠️ **Note:** If port 5000 is in use (common on macOS), use: `flask --app server run --port 5001`

---

## 🚀 Usage

### Via Web Interface

1. Open your browser at `http://localhost:5000`
2. Enter text in the input field
3. Click **"Analyze Sentiment"**
4. View the result with classification and score

### Via API

```bash
# GET Request
curl "http://localhost:5000/sentimentAnalyzer?textToAnalyze=I%20love%20Python"

# Response
The provided text was identified as POSITIVE with a score of 0.5.
```

### Via Python

```python
from SentimentAnalysis import sentiment_analyzer

# Analyze a text
result = sentiment_analyzer("I love working with Python")
print(result)
# {'label': 'SENT_POSITIVE', 'score': 0.5}

# Negative text
result = sentiment_analyzer("I hate bugs")
print(result)
# {'label': 'SENT_NEGATIVE', 'score': -0.8}
```

---

## 📡 API

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Home page (web interface) |
| `GET` | `/sentimentAnalyzer` | Analyzes the sentiment of a text |

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `textToAnalyze` | `string` | Text to be analyzed |

### Response

```json
{
  "label": "SENT_POSITIVE | SENT_NEGATIVE | SENT_NEUTRAL",
  "score": -1.0 to 1.0
}
```

---

## 🧠 How It Works

### Architecture

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   Web Interface  │────▶│   Flask Server   │────▶│    TextBlob      │
│   (HTML/JS/CSS)  │     │   (server.py)    │     │  (NLP Engine)    │
└──────────────────┘     └──────────────────┘     └──────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
    User Input            Process Request         Analyze Sentiment
```

### Analysis Algorithm

TextBlob uses a **Naive Bayes classifier** trained with the movie reviews corpus:

1. **Tokenization** - Breaks the text into words
2. **Lexicon Lookup** - Looks up polarity of each word
3. **Weighted Average** - Calculates final polarity
4. **Classification** - Applies thresholds

```python
if polarity > 0.1:
    label = "SENT_POSITIVE"   # 😊
elif polarity < -0.1:
    label = "SENT_NEGATIVE"   # 😠
else:
    label = "SENT_NEUTRAL"    # 😐
```

### Polarity Scale

```
Negative ◄─────────────────────────────────────────► Positive
   -1.0        -0.5        0.0        +0.5        +1.0
    │           │           │           │           │
  Very       Negative    Neutral    Positive      Very
 Negative                                       Positive
```

---

## 📁 Project Structure

```
sentiment-analysis/
├── 📂 SentimentAnalysis/           # Python package
│   ├── __init__.py                 # Exports sentiment_analyzer
│   └── sentiment_analysis.py       # Analysis function
├── 📂 templates/                   # HTML templates
│   └── index.html                  # Web interface
├── 📂 static/                      # Static files
│   └── mywebscript.js              # Frontend JavaScript
├── 📂 venv/                        # Virtual environment
├── server.py                       # Flask server
├── test_sentiment_analysis.py      # Unit tests
├── .gitignore                      # Git ignored files
├── LICENSE                         # Project license
└── README.md                       # This file
```

---

## 🧪 Tests

### Run Tests

```bash
python test_sentiment_analysis.py
```

### Expected Result

```
......
----------------------------------------------------------------------
Ran 6 tests in 0.020s

OK
```

### Test Coverage

| Test | Description |
|------|-------------|
| `test_positive_sentiment` | Verifies positive text analysis |
| `test_negative_sentiment` | Verifies negative text analysis |
| `test_neutral_sentiment` | Verifies neutral text analysis |
| `test_empty_input` | Verifies empty input handling |
| `test_whitespace_input` | Verifies whitespace-only input |
| `test_none_input` | Verifies None input handling |

---

## 📊 Code Quality

### Pylint Score

```bash
pylint server.py
# Your code has been rated at 10.00/10

pylint SentimentAnalysis/sentiment_analysis.py
# Your code has been rated at 9.52/10
```

---

## 🔧 Technologies

| Technology | Usage |
|------------|-------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | Main language |
| ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white) | Web framework |
| ![TextBlob](https://img.shields.io/badge/-TextBlob-yellow) | NLP engine |
| ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white) | Interface structure |
| ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?logo=css3&logoColor=white) | Styling |
| ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black) | Interactivity |

---

## 🆚 Comparison: TextBlob vs Watson

| Aspect | TextBlob | Watson NLU |
|--------|----------|------------|
| 💰 **Cost** | Free | Paid |
| 🌐 **Internet** | Offline | Requires connection |
| 🎯 **Accuracy** | Medium (Naive Bayes) | High (BERT/Transformers) |
| ⚡ **Speed** | Very fast | Slower (API) |
| 📦 **Installation** | `pip install textblob` | SDK + API Key |
| 🔒 **Privacy** | Local | Data sent to IBM |

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Alcino Luvualo**

[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github)](https://github.com/Alcino-Luvualo)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/alcino-luvualo)

---

## 🙏 Acknowledgments

- [TextBlob](https://textblob.readthedocs.io/) - NLP Library
- [Flask](https://flask.palletsprojects.com/) - Micro web framework
- [NLTK](https://www.nltk.org/) - Natural Language Toolkit

---

<p align="center">
  Made with ❤️ and ☕ | 2026
</p>
