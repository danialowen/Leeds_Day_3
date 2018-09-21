# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:36:37 2018

@author: gydwo
"""

class Person:
    def __init__(self, money, happiness):
        self.money = money
        self.happiness = happiness
        
    def work(self):
        self.money = self.money + 10  
        self.happiness = self.happiness - 5
        # or: you could type self.happiness -= 5
        # as I work, money goes up and happiness goes down
        
    def consume(self):
        self.happiness += 7
        self.money -= 8
        #as we consume, happiness up 7 and money down 8
        
    def __repr__(self):
        return (f"A person with money = {self.money} "
                f" and happiness = {self.happiness}")
        
    def interact(self, other):
        """interact with other person; increase happiness for both"""
        self.happiness += 1
        other.happiness += 1
        
        

# this class now works
# make a person with 100 money and 10 happiness

dan = Person(100,10)

# type 'dan' and this is now a person. type 'dan.money' and will
# give answer of a 100
# name will not show in 'variables explorer'.
# click settings and uncheck 'exclude unsuported data types'


# now set 'dan' to work and we can now see how much money/happiness remains
# money 110, happiness = 5

dan.work()
print("dan's money", dan.money)
print(f"Dan: money = {dan.money}, "
      f"happiness = {dan.happiness}")

#now set to consume
# m = 102, h = 12
dan.consume()
print(f"Dan: money = {dan.money}, "
      f"happiness = {dan.happiness}")

# set other person and they both interact
# dan and rob's happiness go up by 1 each 
rob = Person(500,5)
rob.interact(dan)
print('After interaction:')
print(dan)
print(rob)






# Input/Output


#turn text to integer
result = 10
result_as_integer = int(result)


#create file 
my_file = open('hi.txt', 'w')
my_file.write('Oh Hello!')
my_file.close()


#read file
file_for_reading = open('hi.txt', 'r')
text_in_file = file_for_reading.read()
print(text_in_file)


#instead of 'file_for_reading...' line
# don't need to close file anymore bc when indent satops, python assumes
# it's closed

with open ('hi.txt', 'r') as file_for_reading:
    text_in_file = file_for_reading.read()
    print(text_in_file)
    
    
    
    
    
#create numerical file
#data_file = open('data_file.txt', 'w')
#data_file.write('100 5 ' 
#                '\n'
#                '200 10 '
#                '\n'
#                '400 15 '
#                '\n'
#                '300 10 ')
#data_file.close()

file_for_reading = open('data_file.txt', 'r')
agents_data = file_for_reading.read()
print(agents_data)


#read line by line
with open('data_file.txt', 'r') as file_for_reading:
    for line in file_for_reading:
        print('I read a line and it is: ', repr(line))
        
#split the words        
with open('data_file.txt', 'r') as file_for_reading:
    for line in file_for_reading:
        words = line.split()
        print('I read a line and it is: ', repr(words))
#construct persons
with open('data_file.txt', 'r') as file_for_reading:
    for line in file_for_reading:
        words = line.split()
        money = int(words[0])
        happiness = int(words[1])
        person = Person(money, happiness)
    print('I read a line and I created: ', person)
        
#create function
def read_person_from_file(filename):
    persons = []
    with open(filename, 'r') as file_for_reading:
        for line in file_for_reading:
            words = line.split()
            money = int(words[0])
            happiness = int(words[1])
            person = Person(money, happiness)
            persons.append(persons)
    return persons

#read file from data
person_list = read_persons_from_file('data_file.txt')
for person in person_list:
    person.work()
    
def write_persons_to_file(filename, persons):
    """save a list of Person to file so that it can be read by read_persons_from_file"""
    with open(filename, 'w') as file_for_writing:
        for person in persons:
            s = f'{person.money} {person.happiness}'
            file_for_writing.write(s)
            
write_persons_to_file('workieworkie.txt', person_list)

    
        