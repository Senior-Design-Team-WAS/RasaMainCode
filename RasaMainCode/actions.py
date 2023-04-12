
import json

from typing import Any, Dict, List, Text

from rasa_sdk import Action ,Tracker
from rasa_sdk.executor import CollectingDispatcher



class EnToZh:
    def __init__(self, data_file):
        with open(data_file,encoding="utf-8") as fd:
            self.data = json.load(fd)

    def __call__(self, key):
        return self.data.get(key, key)


class MyKnowledgeBaseAction(Action):
    def name(self) -> Text:
        return "action_response_query"

        

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: List[Dict[Text, Any]],
    ) -> None:
        self.en_to_zh = EnToZh("en_to_zh.json")
        print("asd")
        dispatcher.utter_message(text="123")