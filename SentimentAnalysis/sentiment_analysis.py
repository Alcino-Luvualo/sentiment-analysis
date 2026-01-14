from textblob import TextBlob


def sentiment_analyzer(text_to_analyze):
    try:
        blob = TextBlob(text_to_analyze)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            label = "positive"
        elif polarity < -0.1:
            label = "negative"
        else:
            label = "neutral"

        return {"label": label, "score": round(polarity, 5)}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"label": None, "score": None}
