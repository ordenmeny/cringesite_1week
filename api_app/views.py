from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .generate_joke import TOKEN, FOLDER_ID, run


class ListJokes(APIView):
    def get(self, request):
        jokes = JokeModel.objects.all()
        serializer = JokeSerializer(jokes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class JokeCreateAPIView(APIView):
    # Генерация шутки по POST-запросу.
    # В качестве ответа приходит сгенерированная шутка, id шутки в БД

    def post(self, request, *args, **kwargs):
        topic_input = str(request.data["topic_input"])  # request
        run_res = run(TOKEN, FOLDER_ID, topic_input)
        gpt_response_text = str(run_res["result"]["alternatives"][0]["message"]["text"])  # ответ

        joke_data = {
            "topic_input": topic_input,
            "text_joke": gpt_response_text,
        }

        serializer = JokeSerializer(data=joke_data)

        if serializer.is_valid():
            joke = serializer.save()
            return Response(
                {
                    "id": joke.pk,  # Номер pk созданной записи
                    "topic_input": joke.topic_input,
                    "text_joke": joke.text_joke,
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JokeRetrieveAPIView(RetrieveDestroyAPIView):
    # 1) GET: Получение шутки по id
    # 2) DELETE: Удаление шутки
    queryset = JokeModel.objects.all()
    serializer_class = JokeSerializer
    permission_classes = ()
