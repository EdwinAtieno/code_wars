class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name,age,tracks,score):
        self.name= name
        self.age = age
        self.track = tracks
        self.score= score

    def change_name(self):


        return self.name
    def change_age(self):
        pass
    def add_track(self):
        pass
    def get_score(self):
        pass



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
"""Assignments 
1.  Download the Starter Project here. You can follow the steps outlined in the guidelines.

2.  Open “main.py”, and complete the function “find_anagrams”. It should accept two strings, and determine if they are anagrams. You can read more about anagrams here.

3.  Your function should return True  if they are anagrams, else  False.
String Manipulation in Python - PythonForBeginners.com

Python Lists and List Manipulation | by Michael Galarnyk | Towards Data Science 

Anagrams 

Read the Guidelines first here: Guidelines

1.  Download the Starter Project here. You can follow the steps outlined in the guidelines.

2.  Open “main.py”, and complete the function “read_file_content”. It should accept a filename as an argument and read the text contained in that file. It should return a string.

3.  Complete the function “count_words”. It uses “read_file_content” to read the text contained in “story.txt”. It should return a dictionary whose keys are unique words, and their values the count of those words in the text e.g {“as”:10, “would”:5}.

 

Resources:

How to Read a Text file In Python Effectively

Python Functions

Read the Guidelines first here: Guidelines
 

1.  Download the Starter Project here. You can follow the steps outlined in the guidelines.

2.  Open “main.py”. You’ll find the skeleton of the class Student. Student class should have the following attributes:

 Name: A string, should be initialized when creating an instance of Student
 Age: An integer, should be initialized when creating an instance of Student
Tracks: A list of strings, should be initialized when creating an instance of Student. Feel free to pick any values as tracks.
 Score: A float, should be initialized when creating an instance of Student.    
3.  Create the following methods for class “Student”:

change_name: Change students name, should accept a new name as an argument.
Change_age: Change students' age, should accept a new age as an argument. Should ensure age remains an integer.
Add_track: Add a new item to students tracks, should accept a new track as an argument.
get_score: Return student’s score.
 

Resources:

Python Classes and Objects - GeeksforGeeks

Python's Instance, Class, and Static Methods Demystified
"""