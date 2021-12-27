# We will use wave package available in native Python installation to read and write .wav audio file
import wave
def ultrasonic_encrypt(plaintext):
    """# read wave audio file"""
    song = wave.open("21000.wav", mode='rb')
    #song is a object
    #print("song :", song)
    # Read frames and convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    """for i in range(len(frame_bytes)):
        if frame_bytes[i]>256:
            print("256>",i,frame_bytes[i])
            break
            """
    #print(frame_bytes)
    #TESTING
    """
    j=0
    for i in range(0,5644800):
        if(frame_bytes[i] != 0):
            print(i , "frame_bytes[]   :",frame_bytes[i])
    
            j=j+1
            if(j==150):
                    break
     """

    """# The "secret" text message"""


    string=plaintext
    #string='Hello World!!!!'
    #print("Length of string input : ", (len(string)*8*8))


    """# Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters."""
    string = string + "###"
    #print("String : ", string)

    while (len(frame_bytes) < len((string)*8*8)):
        frame_bytes=frame_bytes + frame_bytes

    """# Convert text to bit array"""
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
    #print("bit of alphabet A :", bin(ord('A')).lstrip('0b').rjust(8,'0'))
    #print(''.join([bin(ord('A')).lstrip('0b').rjust(8,'0')]))
    #print(list(map(int, ''.join([bin(ord('A')).lstrip('0b').rjust(8,'0')]))))
    #print(''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string]))



    """"# Replace LSB of each byte of the audio data by one bit from the text bit array """
    for i, bit in enumerate(bits):
        #print("bit",bit)
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    """# Get the modified bytes"""
    frame_modified = bytes(frame_bytes)

    #print("len is",len(frame_modified))
    """# Write bytes to a new wave audio file"""
    with wave.open('song_embedded_ultrasonic.wav', 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()