from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline
# Create your views here.

emotions_detector =  pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def get_emotions(message):
    result = emotions_detector(message)
    print(result)
    return {"result": "testing"}

@api_view(["GET","POST"])
def chat(request):
    if request.method == "POST":
        print("Content-Type:", request.content_type)  # Debugging
        print("Raw Body:", request.body)  # Debugging
        print("Headers:", request.headers)  # Debugging
        print("POST", request.POST)
        try:
            data = request.data
            print("Parsed Data:", data)
        except Exception as e:
            return Response({"error": f"Failed to parse JSON: {str(e)}"}, status=400)

        message = data.get("content", "")
        if not message:
            return Response({"error": "Content cannot be empty"}, status=400)

        bot_response = get_emotions(message)
        return Response({"response": bot_response})
        # user_message = "I am happy"
        # bot_response = get_emotions(user_message)
        # return Response({"response": bot_response})
    return Response({"response":"test"})