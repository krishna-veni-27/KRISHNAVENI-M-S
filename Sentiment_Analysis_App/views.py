from django.shortcuts import render
from textblob import TextBlob

def home(request):
    sentiment = None
    text = ""

    if request.method == "POST":
        text = request.POST.get("text")

        analysis = TextBlob(text)

        if analysis.sentiment.polarity > 0:
            sentiment = "Positive"
        elif analysis.sentiment.polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

    return render(request, "index.html", {
        "sentiment": sentiment,
        "text": text
    })