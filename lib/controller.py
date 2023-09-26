from decouple import config
import os
import openai
import requests


class Controller:
    def __init__(self):
        self.key = config("OPENAI_API_KEY")
        self.organization = "org-lxPTLC4axXuep5yp0iaq3KB8"

    def start(self):
        openai.organization = self.organization
        openai.api_key = self.key

    def ask_question(self, question):
        s = requests.Session()
        s.headers = {
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
        }
        resp = s.post(
            url="https://api.openai.com/v1/chat/completions",
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant named PyCli-GPT."},
                    {"role": "user", "content": question},
                ],
            }
        )
        
        return resp.json()