# _________________________________________________________________________________________________
#
# ***Please Note*** The dictionary file will not open unless it is in Python's active directory
# _________________________________________________________________________________________________

# Opening the dictionary file.
DictionaryFile = open("words.txt")

# Creating an empty list to store the dictionary in, as well as an empty dictionary to act as the original list.
Words = []
OriginalWords = []

# Creating a list to store the letters of the alphabet, as well as a list to store the corresponding value of each letter.
Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
 
# Writing the content of the dictionary file to the list and removing the string "\n" from the end of each element.
for Line in DictionaryFile:
    New_Line = Line.replace("\n" , "")
    Words.append(New_Line)
    OriginalWords = Words

DictionaryFile.close

# Main function. First returns the Words list to the OriginalWords list, and then asks for user input and converts the string to lowercase. Then passes the inputted word to the Find_Word search algorithm.
def Main():

    global Words
    global OriginalWords

    Words = OriginalWords
    print("_______________________________________________________\n")
    Inputted_Word = input("Please enter the word you would like to search for.\n\n")
    try:
        Inputted_Word = str(Inputted_Word)
        if Inputted_Word == "":
            Code = 1
            Error(Code)
    except ValueError:
        Code = 1
        Error(Code)

    Inputted_Word = Inputted_Word.lower()
    Find_Word(Inputted_Word)

# Function that tells the user there is an error, and calls the Main function so the user can search again.
def Error(Code):
    if Code == 1:
        print("_______________________________________________________\n")
        print("Error: Invalid input.\nEnsure you enter a word only including the letters of the English alphabet.")
    elif Code == 2:
        print("_______________________________________________________\n")
        print("Error: The word you have entered was not found.\nIf you think you are seeing this in error, please ensure you have typed the word correctly.")
    Main()

# The main search algorithm.
def Find_Word(User_Word):

    global Words
    global OriginalWords

    User_Word_Length = len(User_Word)                           # Getting the legnth of the user inputted word

    Start = 0                                                   # Setting the start position as the start of the list
    Position = 0                                                # Setting the position / index of the current letter to be checked in the words. Starts at 0 so the first letter is checked first.

    while True:                                                 # While loop that handles the search. Infinite, but will always be broken out of.

        End = len(Words)                                        # Setting the end position as the length (end) of the list
        #print("Length of List:", End)                          # For debugging purposes.
        if End == 3 or End == 2:                                # Sets the middle value as index 0 if the list is 2 or 3 elements long.
            Middle = 0
        elif End == 0:                                          # If the list is empty, the word is not present in the Words list, and it will call Error with the code 2 which prompts the user of this.
            Code = 2
            Error(Code)
        else:
            Middle = ((End - Start)/2)                          # If the list has more than 3 elements, the middle index of the list is calculated.
            Middle = Middle.__round__()
        Middle_Word = Words[Middle]                             # The middle word is found and the length of this word is stored in a variable.
        Middle_Word_Length = len(Middle_Word)

        if User_Word == Middle_Word:                            # If the middle word is the user's word, the index of the word is passed to the Found function.
            Index = OriginalWords.index(Middle_Word)
            Found(Index)

        if Position < User_Word_Length:                         # If the index of the current position being checked is smaller than the legnth of the user's word, then Position is used as the index for the current letter being checked in the user's word.
            User_Letter = User_Word[Position]
        else:
            User_Letter = User_Word[-1]                         # Otherwise, if the user's word is longer than the Position being checked, the current letter being checked in User_Word will be the final letter / character.
        if Position < Middle_Word_Length:                       # The same check is then carried out for the Middle_Word.
            Middle_Letter = Middle_Word[Position]
        else:
            Middle_Letter = Middle_Word[-1]

        if User_Letter in Alphabet:                             # If the current letter being checked in User_Word is part of the alphabet, it will find the index of that letter in the Alphabet list and use this as an index to get the letter's position in the alphabet from Values.
            Index = Alphabet.index(User_Letter)
            User_Value = Values[Index]
        else:                                                   # Error handling: if the current letter being checked is not part of the alphabet, it will call Error and notify the user that their input was invalid.
            Code = 1
            Error(Code)
        Index = Alphabet.index(Middle_Letter)                   # Grabs the value of the letter currently being checked in the Middle_Word too.
        Middle_Value = Values[Index]

        '''print("TICK VARIABLES")                              # Printing variables for debugging purposes.
        print("User word: ", User_Word)
        print("User letter: ", User_Letter)
        print("User letter value: ", User_Value)
        print("Checking position: ", Position)
        print("Middle word: ", Middle_Word)
        print("Middle letter: ", Middle_Letter)
        print("Middle letter value: ", Middle_Value)
        print("Start index: ", Start)
        print("Middle word index: ", Words.index(Middle_Word))
        print("End index: ", End)
        print("Current list:", Words)
        print("_______________________________________________________")
        print("TICK RESULTS")'''


        '''if Middle_Word in User_Word:                                     # Seperate if statements instead of using OR for debugging purposes.
            # Keep 2nd half
            New_Start = (Words.index(Middle_Word)) + 1
            Words2 = Words[New_Start:]
            Words = Words2 
            Position = 0
            #print("Middle word PART OF User word")
        elif User_Word in Middle_Word:
            # Keep 1st half
            New_End = Words.index(Middle_Word)
            Start = 0
            Words2 = Words[0:New_End]
            Words = Words2
            Position = 0
            #print("User word PART OF Middle word")'''


        if Middle_Value > User_Value or User_Word in Middle_Word:           # If the value of the current letter being checked in the Middle_Word is bigger than that of the User_Word, OR if the User_Word is in / part of the Middle_Word, the 1st half of the list is kept.
            # Keep 1st half
            New_End = Words.index(Middle_Word)                              # The new endpoint for the list becomes the index of the Middle_Word.
            Start = 0                                                       # The start is set to index 0.
            Words2 = Words[0:New_End]                                       # Words2 is created to temporarily store the new spliced list. This goes from the start of the Words list to the New_End point.
            Words = Words2                                                  # Setting words to the new spliced list.
            Position = 0                                                    # The position of the letter being checked is set back to 0.
            #print("Middle > User")                                         # For debugging purposes.
        elif Middle_Value < User_Value or Middle_Word in User_Word:         # If the value of the current letter being checked in the Middle_Word is smaller than that of the User_Word, OR if the Middle_Word is in / part of the User_Word, the 2nd half of the list is kept.
            # Keep 2nd half
            New_Start = (Words.index(Middle_Word)) + 1                      # The new starting point of the list is set as the element after the Middle_Word.
            Words2 = Words[New_Start:]                                      # The temporary Words2 list splices Words from the New_Start position to the end of the list.
            Words = Words2                                                  
            Position = 0
            #print("Middle < User")
        elif Middle_Value == User_Value:                                    # If the current letters being checked in the Middle_Word and User_Word match, one is added to the Position variable, so that the next letter in the words will be checked / compared.
            Position = Position + 1 
            #print("Middle = User")

        '''print("Start index: ", Start)                                    # Printing variables for debugging purposes.
        #print("Middle word index: ", Words.index(Middle_Word))
        print("End index: ", End)
        print("Current list:", Words)
        print("_______________________________________________________")'''
        

# Found function called when the word is successfully found. Passed the index of the word found. Outputs the index in the list as well as the actual line position in the words.txt file to the user.
def Found(Index):

    global OriginalWords

    Line = Index + 1                                                                                        
    print("..___________________________________________________..\n")
    print("'",OriginalWords[Index],"'", "found, index is:", Index, "\nLine number in words.txt:", Line)            
    Main()

# Runs the Main function.
Main()
