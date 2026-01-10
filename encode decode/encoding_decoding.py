#encode and decode
# abcd
# shift by 3 -> abcd=cdef

alpha = [
      'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',' '
    ] #z is at last index u cannot shift further -> use % to get remainder and print the letter

def encoding_decoding(text,shift_amt,operation):
    cipher_text=""
    # if decode then  -shift_amt ,if encode   +shift_amt
    if operation=="decode":
      shift_amt *=-1 
        
    for letter in text:
        if letter not in alpha:
           cipher_text += letter
        else:
           shifted_position = alpha.index(letter)+shift_amt # decode => +(-shift_mt)
           shifted_position %=len(alpha) #  eg:z=25 ->27%25 = 2 ->prints c
           cipher_text += alpha[shifted_position]
    
    print(f"{operation }: {cipher_text}")


choice="yes"   
while choice=="yes":
   operation=input("enter encode for encoding and decode for decoding : ").lower()
   text=input("enter text : ")
   shift_amt=int(input("enter shift amt : "))

   encoding_decoding(text,shift_amt,operation)
   

   choice=input("if u want to try again enter yes  else no : ").lower()
