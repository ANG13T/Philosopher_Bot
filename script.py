import re
import random
from responses import negative_responses, exit_commands, random_questions, ask_for_questions,user_questions

class PhilosopherBot:
    def __init__(self):
        pass
    def greet(self):
        self.name = input("Well there, what is you name \n >")
        user_question = input(f'Welcome, {self.name}, to the school of Athens! Do you have ny questions \n >')
        if (user_question in negative_responses) or (user_question in exit_commands):
            print("Farewell, my friend.")
            return
        self.talk() 

    def exit_functionality(self, user_input):
        for command in exit_commands:
            if command in user_input:
                print("Farewell, my friend.")
                return True

    def talk(self):
        user_reply = input("You can ask me about anything you please /n>")

        while not self.exit_functionality(user_reply):
            self.match_reply(user_reply)
            ask_question = random.choice(ask_for_questions)
            user_reply = input(ask_question)
        
    def match_reply(self, user_reply):
        for intent, regex in user_questions.items():
            found_match = re.match(regex, user_reply)
            
            if found_match:
                if intent == "describe_place_intent" or intent == "describe_place_intent2":
                     print(self.describe())
                elif intent ==  "answer_name_intent":
                    print(self.give_name())  
                elif intent == "who_are_you_intent":
                    print(self.give_name())
                elif intent == "life_intent":
                     print(self.life_intent())
                elif intent == "nature_intent":
                    print(self.nature_intent())
                elif intent == "stoic_intent":
                    print(self.stoic_intent())
                elif intent == "friend_intent":
                    print(self.friend_intent())
            else:
                print(self.no_match_intent())

    def describe(self):
        print("describe method")
        responses = ("My planet is a utopia of diverse organisms and species.",  "I am from Opidipus, the capital of the Wayward Galaxies. ")
        return random.choice(responses)

    def give_name(self):
        print("give_name method")
        responses = ("My planet is a utopia of diverse organisms and species.",  "I am from Opidipus, the capital of the Wayward Galaxies. ")
        return random.choice(responses)

    def life_intent(self):
        print("life_intent method")
        responses = ("My planet is a utopia of diverse organisms and species.",  "I am from Opidipus, the capital of the Wayward Galaxies. ")
        return random.choice(responses)

    def nature_intent(self):
        print("nature_intent method")
        responses = ("My planet is a utopia of diverse organisms and species.",  "I am from Opidipus, the capital of the Wayward Galaxies. ")
        return random.choice(responses)

    def stoic_intent(self):
        print("stoic_intent method")
        responses = ("My planet is a utopia of diverse organisms and species.",  "I am from Opidipus, the capital of the Wayward Galaxies. ")
        return random.choice(responses)

    def friend_intent(self):
        print("friend_intent method")
        responses = ("My planet is a utopia of diverse organisms and species.",  "I am from Opidipus, the capital of the Wayward Galaxies. ")
        return random.choice(responses)

    def no_match_intent(self):
        print("no_match_intent method")
        responses = ("Please tell me more.", "Tell me more!", "Why do you say that?", "Why?", "I see. Can you elaborate?")
        return random.choices(responses)

bot = PhilosopherBot()
bot.greet()