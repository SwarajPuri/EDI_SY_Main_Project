
# file contains combined algorithms
from Combined.DES.des  import main , main2
from Combined.StegaPy.encode import enimage
from Combined.StegaPy.decode import deimage
from Combined.Audio_Steganography_Ultrasonic_Embedded.Main_Ultrasonic import sound_encrypt , sound_decrypt

plaintext = str()
key = str()
ciphertext = str()
isPaddingRequired = str()
file_name = str()
imgname = str()

def pro_encrypt():
    global plaintext
    global key
    global ciphertext
    global isPaddingRequired
    global file_name
    global imgname
    """Card_Number-2318_1345_5678_4971_Expiry_Date-09/23Name_on_Card-Prateek_Puranik_CVV-273"""

    plaintext = input("Enter the message to be encrypted : ")
    key = input("Enter a key of 8 length (64-bits) (characters or numbers only) : ")  # password

    #="In exchange for power, maybe I've lost something that is essential to being human."
    #key="baldcape"
    print("\n........Encryption Start........ \n")
    print("DES Encryption ..........",end="\n")
    ciphertext , isPaddingRequired = main(plaintext, key)
    print()
    #print(ciphertext,isPaddingRequired)

    print("Image Encryption ..........",end="\n")
    imgname=input("Enter name for encrypted image: ")
    imgname+='.png'
    enimage(plaintext,imgname)
    print()

    print("Audio Encryption ..........",end="\n")
    #file_name=sound_encrypt(plaintext)

    print("\n........Encryption Complete........\n")
    while(1):
        if(""
           ""==input()):
            break


def image_encrypt(plaintext,imgname):
    #imgname should be name of select file for encyption
    #decrypt filename

    Dfilename=imgname.split('.')[0]+'encrypted.png'
    enimage(plaintext,imgname,Dfilename)
    return Dfilename


def image_decrypt(Dfilename):
    return deimage(Dfilename)



def pro_decrypt():
    print("........Decryption Start........ \n")
    print("DES Decryption ..........",end="\n")
    while(1):
        key_de=input("Enter Key for decryption: ")
        if(key_de==key):
            break
        else :
            print("!!!Wrong Key!!!")


    main2(key,ciphertext,isPaddingRequired)
    print()
    print("Image Decryption ..........",end="\n")
    deimage(imgname)
    print()
    print("Audio Decryption ..........",end="\n")
    sound_decrypt(file_name)

    print("\n........Decryption Complete........ \n")

def main1():
    #pro_encrypt()
    #pro_decrypt()
    image_encrypt('hello world','img2.jfif')

#main1()

