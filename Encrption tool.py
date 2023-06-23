#Cipher program
print("Welcome to this easy cipher tool used to secure your important messages enjoy")
alpabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
            'x','y','z',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
mode = int(input("Type 1 to encrypt or 0 to decrypt "))
text = input("Type your message:\n ").lower()
shift = int(input("Whats the number of shift used:\n"))
#the function encrypt was defined here
def encrypt(message , shift_num):
    cipher_text = ""
    for letters in message:
#In the line below the .index fuction coverts the amount
#of alphabet received into digits 
        current_position = alpabets.index(letters)
        new_position = current_position + shift_num
        new_letter = alpabets[new_position]
        cipher_text += new_letter 
    print(f"Your encryption key is {cipher_text}")

def decrypt(new_message , new_shift):
    new_cipher_text = ""
    for letters in new_message:
        current_position = alpabets.index(letters)
        new_position = current_position - new_shift
        new_letter = alpabets[new_position]
        new_cipher_text += new_letter 
    print(f"Your decryption  key is {new_cipher_text}")  
#This last lines give the instrutions on what path 
# the code should follow
if mode == 1:
    encrypt(message= text, shift_num= shift)
elif mode == 0:
    decrypt(new_message= text , new_shift= shift)  
else:
    print("You've entered an invaid number")
