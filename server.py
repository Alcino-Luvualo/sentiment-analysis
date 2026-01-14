"""
Módulo servidor para análise de sentimentos.

Este módulo implementa um servidor Flask que fornece uma interface web
para análise de sentimentos usando TextBlob.
"""

from flask import Flask, render_template, request
from SentimentAnalysis import sentiment_analyzer

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')


@app.route('/')
def render_index_page():
    """Renderiza a página principal (index.html)."""
    return render_template('index.html')


@app.route('/sentimentAnalyzer')
def sent_analyzer():
    """
    Processa a requisição GET e retorna a análise de sentimento.

    Espera receber um parâmetro 'textToAnalyze' na URL.

    Returns:
        str: Mensagem com resultado da análise ou erro
    """
    text_to_analyze = request.args.get('textToAnalyze', '')

    if not text_to_analyze or text_to_analyze.strip() == '':
        return "Por favor, digite um texto para analisar!"

    result = sentiment_analyzer(text_to_analyze)

    if result['label'] is None:
        return "Entrada inválida! Tente novamente."

    label = result['label']
    score = result['score']

    label_translation = {
        "SENT_POSITIVE": "POSITIVO",
        "SENT_NEGATIVE": "NEGATIVO",
        "SENT_NEUTRAL": "NEUTRO"
    }

    label_pt = label_translation.get(label, label)

    return f"O texto fornecido foi identificado como {label_pt} com uma pontuação de {score}."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
