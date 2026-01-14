/**
 * Script para executar análise de sentimentos via requisição ao servidor.
 */

function runSentimentAnalysis() {
    // Obter o texto do campo de entrada
    const textInput = document.getElementById('textInput');
    const textToAnalyze = textInput.value;
    const resultDiv = document.getElementById('result');

    // Verificar se o texto está vazio
    if (textToAnalyze.trim() === '') {
        alert('Por favor, digite um texto para analisar!');
        return;
    }

    // Fazer requisição GET ao servidor
    const url = `/sentimentAnalyzer?textToAnalyze=${encodeURIComponent(textToAnalyze)}`;

    fetch(url)
        .then(response => response.text())
        .then(data => {
            // Exibir o resultado
            resultDiv.innerHTML = data;
            resultDiv.style.display = 'block';

            // Adicionar classe baseada no resultado
            resultDiv.classList.remove('positive', 'negative', 'neutral');
            if (data.includes('POSITIVO')) {
                resultDiv.classList.add('positive');
            } else if (data.includes('NEGATIVO')) {
                resultDiv.classList.add('negative');
            } else if (data.includes('NEUTRO')) {
                resultDiv.classList.add('neutral');
            }
        })
        .catch(error => {
            resultDiv.innerHTML = 'Erro ao analisar o sentimento: ' + error;
            resultDiv.style.display = 'block';
        });
}

// Permitir análise ao pressionar Ctrl+Enter
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('textInput').addEventListener('keypress', function(event) {
        if (event.key === 'Enter' && event.ctrlKey) {
            runSentimentAnalysis();
        }
    });
});
