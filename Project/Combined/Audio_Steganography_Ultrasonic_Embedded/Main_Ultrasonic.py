from Combined.Audio_Steganography_Ultrasonic_Embedded.Ultrasound_Encryption import ultrasonic_encrypt
from Combined.Audio_Steganography_Ultrasonic_Embedded.encrypt import encrypt
from Combined.Audio_Steganography_Ultrasonic_Embedded.decrypt import decrypt


def sound_encrypt(plaintext,audiofile):
    ultrasonic_encrypt(plaintext)
    return encrypt(audiofile)


def sound_decrypt(file_name):
    return decrypt(file_name)

#sound_encrypt("klmkjlkj")
#sound_decrypt()


