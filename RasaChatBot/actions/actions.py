'''from typing import List, Any, Text, Dict

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSayName(Action):
    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        names = tracker.get_slot("namee")
        if not names:
            dispatcher.utter_message(text="sorry i don't know your name")
        else:
            dispatcher.utter_message(text=f"Your name is {names} , happy to know you!")
        return []'''
