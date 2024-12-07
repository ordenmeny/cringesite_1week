from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .generate_joke import TOKEN, FOLDER_ID, run


class JokeCreateAPIView(APIView):
    # Генерация шутки по GET-запросу.
    # В качестве ответа приходит сгенерированная шутка, id шутки в БД

    def get(self, request, *args, **kwargs):
        text = str(request.data["topic_input"])  # request
        run_res = run(TOKEN, FOLDER_ID, text)
        gpt_response_text = str(run_res["result"]["alternatives"][0]["message"]["text"])  # ответ

        new_model = JokeModel.objects.create(
            topic_input=request.data["topic_input"],
            text_joke=gpt_response_text
        )


        return Response(
            {
                'topic_input': request.data["topic_input"],
                'text_joke': gpt_response_text,
                'db_model': new_model.pk
            }
        )

    # def post(self, request, gpt_response_text):
        # new_model = JokeModel.objects.create(
        #     topic_input=request.data["topic_input"],
        #     text_joke=gpt_response_text
        # )

# class JokeDetailAPIView(RetrieveDestroyAPIView):
#     # 1) GET: Получение шутки по id
#     # 2) DELETE: Удаление шутки
#     queryset = JokeModel.objects.all()
#     serializer_class = JokeSerializer
