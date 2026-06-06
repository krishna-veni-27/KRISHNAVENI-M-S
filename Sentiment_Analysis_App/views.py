from django.shortcuts import render
from textblob import TextBlob

def home(request):
    sentiment = None

    if request.method == "POST":
        text = request.POST.get("text")

        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

    return render(request, "index.html", {"sentiment": sentiment})