"""
Shaan Khan
CNT4713: Assignment 2, Basic Python Programming

"""

class Assignment2:
    
    # Task1: Constructor
    def __init__(self, age):
        self.age = age
        
    # Task 2: Birth Year
    def tellBirthYear(self, currentYear: int):
        print("Your birth year is", (currentYear - self.age))

    # Task 3: List
    def listAnniversaries(self, n: int) -> list:
        result, k = [], n
        while k <= self.age :
            result.append(k)
            k+=n
        return result
    
    # Task 4: String Manipulation
    def modifyAge(self, n: int) -> str:
        s = ""
        s += str(self.age * n)

        r = self.age
        while r > 10:
            r = r // 10
        s += (str(r)) * n
        
        third = str(self.age ** n)
        s += third[::2]
        
        return s
    
    # Task 5: Loops and Conditional Statements
    def checkGoodString(self, string: str) -> bool:
        if not isinstance(string, str):
            return False        
        
        if len(string) < 9:
            return False
        if not string[0].islower():
            return False

        oneNum = False
        for letter in string:
            if letter.isnumeric():
                oneNum = True

        if oneNum == True:
            return True

        return False

    # Task 6: Socket
