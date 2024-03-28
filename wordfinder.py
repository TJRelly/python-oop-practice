"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    def __init__(self, file):
        self.file = file
        self.words = self.parse(self.file)
      
    def __repr__(self):
        return f"Wordfinder(file = {self.file})"  
        
    def print_random_word(self):
        """Prints random line from text file"""
        rand_word = choice(self.words).strip()
        # print(rand_word)
        return(rand_word)
        
    def parse(self, file):
        words = open(file, "r")
        wordList = list(words)
        words.close()
        return wordList
    
        
# wf = WordFinder("words.txt")
# print(wf)
# wf.print_random_word()
# wf.print_random_word()
# wf.print_random_word()

class SpecialWordFinder(WordFinder):
    """Special word finder that excludes blank spaces and comments
    
    >>> swf = SpecialWordFinder("special.txt")
    
    >>> swf.print_random_word() in ["kale", "parsnips", "apple", "mango"]
    True
    
    >>> swf.print_random_word() in ["kale", "parsnips", "apple", "mango"]
    True
    
    >>> swf.print_random_word() in ["# Fruits", "# Veggies", ""]
    False
    
    """
    
    def __repr__(self):
        return f"SpecialWordfinder(file = {self.file})" 
    
    def parse(self, file):
        words = open(file, "r")
        wordList = [word for word in words if not word.startswith("#") and word.strip()]
        words.close()
        return wordList
        
     
# swf = SpecialWordFinder("special.txt")
# print(swf)
# print(swf.words)
# swf.print_random_word()
# swf.print_random_word()
# swf.print_random_word()