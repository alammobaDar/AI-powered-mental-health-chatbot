from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from transformers import pipeline
from .serializers import ChatSerializer
# Create your views here.

class CustomJsonBrowsableAPI(BrowsableAPIRenderer):
    def get_default_renderer(self, view):
        return JSONRenderer()

emotions_detector =  pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def get_emotions(message):
    result = emotions_detector(message)
    print(result)
    return {"result": result}


@api_view(["GET","POST"])
@renderer_classes([CustomJsonBrowsableAPI, JSONRenderer])
def chat(request):
    if request.method == "POST":

        try:
            serializer = ChatSerializer(data=request.data)
            print("Parsed Data:", serializer)
        except Exception as e:
            return Response({"error": f"Failed to parse JSON: {str(e)}"}, status=400)

        if serializer.is_valid():
            message = serializer.validated_data["content"]
        if not message:
            return Response(serializer.errors)

        bot_response = get_emotions(message)
        return Response({"response": bot_response})
    return Response(
        {"content":"message"},
        # content_type="application/json"
    )

def chatpage_view(request):
    return render(request, 'chats/chatpage.html')