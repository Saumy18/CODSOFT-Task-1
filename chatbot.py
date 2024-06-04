import random
import re


class SupportBot:
    negative_res = ("no", "no indeed", "absolutely not", "naw", "not at all", "sorry","nae","no way")
    exit_commands = ("quit", "pause", "exit", "bye", "leave","vacate")

    def __init__(self):
        self.support_responses = {
            'ask_about_product': r'.*\s*product.*',
            'product_reviews': r'.*\s*product.*reviews.*',
            'about_returns': r'.*\s*return.*policy.*',
            'general_query': r'.*how.*help.*'
        }

    def greet(self):
        self.name = input('Hey! What is your name?\n')
        will_help = input(f'{self.name} Ask something? I shall be grateful to assist you with all my knowledge \n')
        if will_help in self.exit_commands:
            print("Bye! See you next time\n")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("see you in near future\n")
                return True
            return False

    def chat(self):
        reply = input("please tell me your problem\n").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == "ask_about_product":
                return self.ask_about_product()
            elif found_match and intent == "product_reviews":
                return self.taste_reviews()
            elif found_match and intent == "about_returns":
                return self.about_returns()
            elif found_match and intent == "general_query":
                return self.general_query()
        return self.no_intent_matched()

    def ask_about_product(self):
        responses = ("Our product is of high-quality and lightweight\n",
                     "Our Product never Dissapoints\n")
        return random.choice(responses)

    def taste_reviews(self):
        responses = "Our product's durability is amazing\n"
        return random.choice(responses)

    def about_returns(self):
        responses = ("Open products cannot be returned\n",
                     "If seal is broken, it cannot be returned\n")
        return random.choice(responses)

    def general_query(self):
        responses = ("How can I assist you next?\n",
                     "Is there anything I can help you with?\n")
        return random.choice(responses)

    def no_intent_matched(self):
        responses = ("You may find other information from our website\n",
                        )
        return random.choice(responses)


bot = SupportBot()
bot.greet()