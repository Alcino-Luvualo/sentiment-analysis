"""
Módulo de análise de sentimentos usando TextBlob.

Este módulo fornece funções para analisar o sentimento de textos,
classificando-os como positivo, negativo ou neutro.
"""

from textblob import TextBlob


def sentiment_analyzer(text_to_analyse):
    """
    Analisa o sentimento de um texto usando TextBlob.
    Retorna None para ambos label e score em caso de erro.

    Args:
        text_to_analyse (str): Texto a ser analisado

    Returns:
        dict: Dicionário com 'label' e 'score', ou None em caso de erro
    """
    try:
        # Validar entrada
        if not text_to_analyse or not isinstance(text_to_analyse, str):
            return {
                "label": None,
                "score": None
            }

        # Remover espaços em branco
        text_to_analyse = text_to_analyse.strip()

        if not text_to_analyse:
            return {
                "label": None,
                "score": None
            }

        # Criar análise com TextBlob
        blob = TextBlob(text_to_analyse)
        polarity = blob.sentiment.polarity  # Valor entre -1 e 1

        # Validar resultado
        if polarity is None:
            return {
                "label": None,
                "score": None
            }

        # Classificar em POSITIVO, NEGATIVO ou NEUTRO
        if polarity > 0.1:
            label = "SENT_POSITIVE"
        elif polarity < -0.1:
            label = "SENT_NEGATIVE"
        else:
            label = "SENT_NEUTRAL"

        # Retornar resultado formatado
        return {
            "label": label,
            "score": round(polarity, 5)
        }

    except Exception as e:
        print(f"Erro ao analisar sentimento: {e}")
        return {
            "label": None,
            "score": None
        }
