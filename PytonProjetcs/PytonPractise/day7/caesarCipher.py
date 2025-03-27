# List of letters with the alphabet
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

from art import logo

#end = "" is used to print the output in the same line/igonra los saltos de linea y escribe en la misma linea

def caesar(originalText,shifts,encodeOrDecode):
    outputText = ""
    for letter in originalText:
        
        if encodeOrDecode == "decode":
            shifts = -shifts        
        
        if letter in alphabet:
            index = alphabet.index(letter)
            index = (index + shifts) % 26
            outputText+=alphabet[index]
        else:
            outputText+=letter
    print(f"The {encodeOrDecode}d is: ",outputText)


print(logo)
        
# finish = input("Do you want to run the program? yes or no: ")
finish="yes"
while finish == "yes":
    encodeOrDecode = input("Enter encode or decode: ")
    while encodeOrDecode != "encode" and encodeOrDecode !="decode":
        print("Invalid input")
        encodeOrDecode = input("Enter encode or decode: ")
    originalText = input("Enter the text: ")
    shifts = int(input("Enter the number of shifts: ")) 
    caesar(originalText,shifts,encodeOrDecode)
    finish = input("Do you want to continue? yes or no: ")

if not finish != "yes":
    print("Goodbye!")
    