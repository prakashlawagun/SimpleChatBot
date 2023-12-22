from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckBalance(Action):

    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        account_number = tracker.get_slot("account_number")
        name = tracker.get_slot("name")

        if account_number and name:
            # Simulating database with account details
            account_details = {
                                "123456":{"name":"Krishna","balance":1000}
                               }

            if account_number in account_details:
                balance = account_details[account_number]["balance"]
                dispatcher.utter_message(f"Dear {name}, your {account_number} has a balance of Rs. {balance}")
            else:
                dispatcher.utter_message("Sorry, I couldn't find your account details.")
        else:
            dispatcher.utter_message("Sorry, I couldn't retrieve your account details. Please provide both account number and name.")

        return []

class ActionTransactionHistory(Action):

    def name(self) -> Text:
        return "action_transaction_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        account_number = tracker.get_slot("account_number")
        name = tracker.get_slot("name")

        # Simulating database with account details
        account_details = {
            "123456": {"name": "Krishna", "balance": 1000, "transactions": ["Deposit 500", "Withdraw 500"]}
        }

        if account_number in account_details:
            transactions = account_details[account_number]["transactions"]
            transaction_history_text = "\n".join(transactions)
            dispatcher.utter_message(f"Transaction History for {name} ({account_number}):\n{transaction_history_text}")
        else:
            dispatcher.utter_message("Sorry, I couldn't find your account details.")

        return []



