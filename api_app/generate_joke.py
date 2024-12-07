import requests

URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
TOKEN = "token"
FOLDER_ID = "folder_id"


def run(iam_token, folder_id, user_text):
    # Собираем запрос
    data = {}
    # Указываем тип модели
    data["modelUri"] = f"gpt://{folder_id}/yandexgpt/latest"
    # Настраиваем опции
    data["completionOptions"] = {"temperature": 0.8, "maxTokens": 1000}
    # Указываем контекст для модели
    data["messages"] = [
        {
            "role": "system",
            "text": "Нужно придумать кринжовую шутку. На вход поступает тема шутки."
        },

        {
            "role": "user",
            "text": f"{user_text}"
        },
    ]

    # Отправляем запрос
    response = requests.post(
        URL,
        headers={
            "Accept": "application/json",
            "Authorization": f"Api-Key {TOKEN}"
        },
        json=data,
    ).json()

    return response


