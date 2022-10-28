
import random
import string

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks',"laptop","bottle","paper","medals"]
lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( ) ..👻 
               |          |
               |         / \ \
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               |        
               |       
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }
used_letters = []
         

def check_input(word):
    alphabet = set(string.ascii_uppercase)
    
    if word not in alphabet:
        guess = input("Sorry not a valid word. Go again :").upper()
        check_input(guess)
  
    
            
# def pick_word(list):
#     word = random.choice(list)
#     while "-" or " " not in word:
#         word = random.choice(list)
#     return word
    
    
# word = pick_word(words)
word = random.choice(words)
word = word.upper()
def hide(word):
    hidden_word = []
    for i in word :
        if i not in used_letters:
            hidden_word.append("-")
        elif i in used_letters:
            hidden_word.append(i.upper())
            
    return hidden_word

lives = 7
hidden = hide(word)

temp = True
while lives>0:
    
    print("Word : "," ".join(hidden))
    print("you have used :"," ".join(used_letters))
    
    guess = input("You have {} lives .Guess a letter :".format(lives)).upper()

    if guess not in used_letters:
        if guess in word:
            used_letters.append(guess.upper())
        elif guess not in word:
            print("letter is not in word ")
            used_letters.append(guess.upper())
            lives -= 1
            print(lives_visual_dict[lives])
    elif guess in used_letters:
        print("Sorry you have already guessed this letter")
    hidden = hide(word)
    if "-" not in hidden:
        temp = False
        break                         
    
if temp == False :
    print("Congrats, You Won !! ^_^")
else :
    print("You lost (._.`) .The word was {}".format(word))
    
    
    

   
