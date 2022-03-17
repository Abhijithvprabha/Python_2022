alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encode = ""

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_word, shift_amount):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text_word' forwards in the alphabet by the shift amount and print the encrypted text_word.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text_word is mjqqt"
  encoded_message = ""
  for letter in text_word:
    for position in range(26):
     if letter == alphabet[position]:
      new_position = position + shift
      new_letter = alphabet[new_position]
      encoded_message += new_letter
  print(encoded_message)
      
      

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
encrypt(text,shift)
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 