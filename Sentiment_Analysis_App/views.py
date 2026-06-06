from django.shortcuts import render

def home(request):
    sentiment = None
    text = ""

    if request.method == "POST":
        text = request.POST.get("text")

        # Your sentiment analysis code here
        sentiment = "Positive"  # Example

    return render(request, "index.html", {
        "sentiment": sentiment,
        "text": text
    })