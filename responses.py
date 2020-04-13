negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
ask_for_questions = ("Any more questions? \n >", "Such inate curiosity! Do you have any more of your questions? \n>", "Do you have another question /n>", "Any more of your wonderful observations or speculations /n>", "Care to ask another question? /n>")

random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

user_questions = {
    'describe_place_intent': r'.*\s*where am I.*',
    'describe_place_intent2': r'.*\s*this place.*',
    'answer_name_intent': r'your name.*',
    'who_are_you_intent': r'*\s*are you.*',
    'life_intent': r'*\s*meaning of life.*',
    'nature_intent': r'*\s*nature.*',
    'stoic_intent': r'*\s*stoicism.*',
    'friend_intent': r'*\s*friend.*'
}