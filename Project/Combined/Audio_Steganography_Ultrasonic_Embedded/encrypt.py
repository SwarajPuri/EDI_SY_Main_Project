# We will use wave package available in native Python installation to read and write .wav audio file
import wave
def encrypt(audiofile):
    """# read wave audio file"""

    file1 = str(audiofile)

    song = wave.open(file1,mode='rb')
    print(song)
    us=wave.open("song_embedded_ultrasonic.wav",mode='rb')
    #song is a object
    #print("song :", song)
    # Read frames and convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    frame_bytes_us = bytearray(list(us.readframes(song.getnframes())))

    #print(type(frame_bytes))
    #l=list(frame_bytes)
    #print(l)
    #print(bytearray(l))
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

    while(len(frame_bytes_us)>len(frame_bytes)):
        frame_bytes+=frame_bytes


    for i in range(0,len(frame_bytes_us)):
        frame_bytes[2*i]=frame_bytes_us[i]


    frame_modified = bytes(frame_bytes)
    #print("Enter sound file name: ",end="")
    #file_name = input()
    file_name = audiofile.split('.')[0]+'encrypted'+'.wav'
    #file_name = audiofile.splt('.')[0] + 'encrypted' + '.wav'
    #print(song.getparams())
    """# Write bytes to a new wave audio file"""
    with wave.open(file_name, 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()
    return file_name