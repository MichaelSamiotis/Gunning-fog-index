#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ommited_paragraphs(x):
    if x[-1] != '.':
        return True
    
def words_validation(var):
    if words(var) < 95 or words(var) > 105:
        return True

def sentences(y):
    full_stop = 0
    for word in y:
        if '.' in word:
            full_stop += 1
    return full_stop
    
def words(z):
    words = len(z.split())
    return words
    
def complex_words(passage):
#for each word in the list count how many words have more or 3 syllables
    words_syllables = 0
    for word in passage.split():
        syllables = 0
        for s in word.lower():
            if (s=='a' or s=='e' or s=='i' or s=='o' or s=='u'):
                syllables = syllables + 1
        if syllables >= 3:
            words_syllables += 1
        else:
            continue
    return words_syllables

#Asking from the user the passage to be evaluated
passage = input('Select a passage (such as one or more full paragraphs) of around 100 words: ')

#Checking if there are ommited paragraphs or the number of words is not sufficient
while ommited_paragraphs(passage) or words_validation(passage):

    if ommited_paragraphs(passage) == True:
        passage = input('The last sentence doesn\'t end with a full stop.\
 One or more sentences might have been ommited.\
 Select a new passage (such as one or more full paragraphs) of around 100 words: ')

    if words_validation(passage):
        passage = print('The number of words in the text seems to be insufficient.\
 Your input is',words(passage),'words.')
        input('Select a new passage (such as one or more full paragraphs) of around 100 words: ')

#Calculation of the fog index
import math
fog_index = math.floor(0.4 * ((words(passage)/sentences(passage))+100*(complex_words(passage)/words(passage))))

print(fog_index) #This is for testing

#Fog index reading level by grade
if fog_index <= 6:
    print('The fog index result is',fog_index,'the text inserted requires the reading \
level of a United States Sixth grade.')
elif fog_index == 7:
    print('The fog index result is 7, the text inserted requires the reading \
level of a United States Seventh grade.')
elif fog_index == 8:
    print('The fog index result is 8, the text inserted requires the reading \
level of a United States Eighth grade.')
elif fog_index == 9:
    print('The fog index result is 9, the text inserted requires the reading \
level of a United States High school freshman.')
elif fog_index == 10:
    print('The fog index result is 10, the text inserted requires the reading \
level of a United States High school sophomore.')
elif fog_index == 11:
    print('The fog index result is 11, the text inserted requires the reading \
level of a United States High school junior.')
elif fog_index == 12:
    print('The fog index result is 12, the text inserted requires the reading \
level of a United States High school senior.')
elif fog_index == 13:
    print('The fog index result is 13, the text inserted requires the reading \
level of a United States College freshman.')
elif fog_index == 14:
    print('The fog index result is 14, the text inserted requires the reading \
level of a United States College sophomore.')
elif fog_index == 15:
    print('The fog index result is 15, the text inserted requires the reading \
level of a United States College junior.')
elif fog_index == 16:
    print('The fog index result is 16, the text inserted requires the reading \
level of a United States College senior.')
elif fog_index >= 17:
    print('The fog index result is',fog_index,'the text inserted requires the reading \
level of a United States College graduate.')
          
#Handling the program exit
import sys
exit_program = input('Press any key to EXIT: ')
if exit_program:
    sys.exit()


# In[ ]:




