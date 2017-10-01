import unittest
import random 

"""
Functions are taken from palindromes.py and modified to operate outside of the Flask framework. 
For adding palindromes, pseudo-time is created using random number generation so that we can simulate palindromes being initialised at times that are at a reasonable distance from eachother. The time limit condition uses 
a value of 100 instead of 600 but follows the same logic.

"""

def is_palindrome(my_string):
    if type(my_string)!=str: #Taken from line 19 in palindromes.py, where it results in a bad request. Here it returns None for the purpose of testing.
        return None  
    lowercase_chars = ''.join(char for char in my_string if char.isalnum()).lower()
    if lowercase_chars==lowercase_chars[::-1]:
        return True
    else: 
        return False    
    
def add_palindrome(palindrome_content,index):
    if is_palindrome(palindrome_content)==True: 
        new_palindrome = {
            "content": palindrome_content,
            "pseudo_time": index * random.randint(1,5)
        }
        palindromes.append(new_palindrome)

def get_palindromes(palindromes):
    pseudo_current_time = 120; #Statistically, this value for current_time is guaranteed to return >10 palindromes with the condition written below. Pseudo_time lies in a range of 1 and 135, and should exceed current_time by 20 starting from the fourth element. There are 27 elements in total.
    recent_palindromes = [palindrome for palindrome in palindromes if pseudo_current_time-palindrome["pseudo_time"]<=100]
    palindromes_to_print = [];
    for palindrome in recent_palindromes: 
        palindromes_to_print.append(palindrome["content"])
    most_recent_index = len(palindromes_to_print)-1
    return palindromes_to_print[most_recent_index:most_recent_index-10:-1]

#palindrome examples taken from: http://www.palindromelist.net
yes_palindrome = [
"A tin mug for a jar of gum, Nita.",
"A Toyota! Race fast, safe car! A Toyota!",
"A Toyota’s a Toyota.",
"Able was I ere I saw Elba.",
"Acrobats stab orca.",
"Aerate pet area.",
"Ah, Satan sees Natasha!",
"Aibohphobia", 
"Air an aria",
"Flee to me, remote elf.",
"Oh, cameras are macho.",
"Olson is in Oslo.",
"On a clover, if alive, erupts a vast, pure evil; a fire volcano.",
"Oozy rat in a sanitary zoo.",
"Smart rams.",
"So Ida, adios.",
"So many dynamos!",
"So, cat tacos!",
"Solo gigolos.",
"Stressed desserts",
"Stressed was I ere I saw desserts.",
"Won kiosk. So, I know.",
"Won tons? Not now.",
"Won’t I panic in a pit now?",
"Won’t it now?",
"Won’t lovers revolt now?",
"He won snow, eh?",
"a1221a"
]

not_palindrome = [
"Hi I'm not a palindrome",
"I'm not one either",
"Only if we could be palindromes",
"1800-Not a palindrome"
"A quick brown fox",
"jumps over the lazy dog",
"A quicker brown fox",
"leaps over the lazier dog",
"13 is my favourite number",
"!!Cool"
]

other_data_types = [23,[11,22,44],["Hi",4,2],99,None,19.81]

palindromes = [];

class palindrome_Check(unittest.TestCase):
    
    def test_is_palindrome(self):
        for p in yes_palindrome: 
            self.assertTrue(is_palindrome(p))
        for np in not_palindrome: 
            self.assertFalse(is_palindrome(np))
        for o in other_data_types: 
            self.assertIsNone(is_palindrome(o))
            
    def test_add_palindrome(self):
        for index in range(len(yes_palindrome)):
            add_palindrome(yes_palindrome[index],index)
        self.assertEqual(type(palindromes),list)
        self.assertEqual(len(yes_palindrome),len(palindromes))
        for p in palindromes: 
            self.assertEqual(type(p),dict)

    def test_get_palindrome(self):
        sample = get_palindromes(palindromes); 
        self.assertEqual(len(sample),10)
        self.assertEqual(type(sample),list)

if __name__ == '__main__':
    unittest.main()
