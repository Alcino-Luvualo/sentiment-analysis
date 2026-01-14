"""
Módulo de testes unitários para a função sentiment_analyzer.

Este módulo contém testes para verificar o correto funcionamento
da análise de sentimentos.
"""

import unittest
from SentimentAnalysis import sentiment_analyzer


class TestSentimentAnalyzer(unittest.TestCase):
    """Testes unitários para a função sentiment_analyzer."""

    def test_positive_sentiment(self):
        """Testa análise de sentimento positivo."""
        result = sentiment_analyzer("I love working with Python")
        self.assertEqual(result['label'], "SENT_POSITIVE")
        self.assertGreater(result['score'], 0.1)

    def test_negative_sentiment(self):
        """Testa análise de sentimento negativo."""
        result = sentiment_analyzer("I hate working with bugs")
        self.assertEqual(result['label'], "SENT_NEGATIVE")
        self.assertLess(result['score'], -0.1)

    def test_neutral_sentiment(self):
        """Testa análise de sentimento neutro."""
        result = sentiment_analyzer("This is a test")
        self.assertEqual(result['label'], "SENT_NEUTRAL")
        self.assertGreaterEqual(result['score'], -0.1)
        self.assertLessEqual(result['score'], 0.1)

    def test_empty_input(self):
        """Testa entrada vazia."""
        result = sentiment_analyzer("")
        self.assertIsNone(result['label'])
        self.assertIsNone(result['score'])

    def test_whitespace_input(self):
        """Testa entrada apenas com espaços em branco."""
        result = sentiment_analyzer("   ")
        self.assertIsNone(result['label'])
        self.assertIsNone(result['score'])

    def test_none_input(self):
        """Testa entrada None."""
        result = sentiment_analyzer(None)
        self.assertIsNone(result['label'])
        self.assertIsNone(result['score'])


if __name__ == '__main__':
    unittest.main()
