# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import requests

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        time_zone = tracker.get_slot("time_zone")
        res = requests.get("http://worldtimeapi.org/api/timezone/{}.json".format(time_zone))
        current_datetime = res.json()["datetime"]
        dispatcher.utter_message(text="Datetime en {}: {}".format(time_zone, current_datetime))
        return []
