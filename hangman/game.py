import random
from .exceptions import *


class GuessAttempt(object):
    pass


class GuessWord(object):
    
    def __init__(self, answer):
        self.answer = answer
        
    def perform_attempt(self):
        pass


class HangmanGame(object):
    WORD_LIST = ['rmotr', 'python', 'awesome']
    
    def __init__(self, word_list=WORD_LIST, number_of_guesses=5):
        self.number_of_guesses = number_of_guesses
        self.remaining_misses = number_of_guesses
        self.previous_guesses = []
        self.word = GuessWord(self.select_random_word(word_list))
    
    def guess(self, letter):
        pass
        
    @classmethod    
    def select_random_word(cls, word_list):
        try:
            return random.choice(word_list)
        except:
            raise InvalidListOfWordsException
        
        
