import random
from .exceptions import *


class GuessAttempt(object):
    
    def __init__(self, character, hit=None, miss=None):
        self.character = character
        self.hit = hit
        self.miss = miss
        if hit == True and miss == True:
            raise InvalidGuessAttempt
    
    def is_hit(self):
        return self.hit == True
    
    def is_miss(self):
        return self.miss == True


class GuessWord(object):
    
    def __init__(self, answer):
        if not answer:
            raise InvalidWordException
        self.answer = answer
        self.masked = len(answer) * '*'
        
        
    def perform_attempt(self, character):
        if len(character) > 1:
            raise InvalidGuessedLetterException
        


class HangmanGame(object):
    WORD_LIST = ['rmotr', 'python', 'awesome']
    
    def __init__(self, word_list=WORD_LIST, number_of_guesses=5):
        self.number_of_guesses = number_of_guesses
        self.remaining_misses = number_of_guesses
        self.previous_guesses = []
        self.word = GuessWord(self.select_random_word(word_list))
    
    def guess(self, character):
        pass
        
        
    @classmethod    
    def select_random_word(cls, word_list):
        try:
            return random.choice(word_list)
        except:
            raise InvalidListOfWordsException
        
        
