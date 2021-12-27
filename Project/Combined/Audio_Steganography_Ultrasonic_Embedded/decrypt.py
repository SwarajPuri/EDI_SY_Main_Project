# Use wave package (native to Python) for reading the received audio file
import wave
def decrypt(file_name):
    decoded=''
    song = wave.open(file_name, mode='rb')
    # Convert audio to byte array

    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    frame_bytes = [frame_bytes[i] for i in range(0,len(frame_bytes),2)]


    # Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    #print(extracted)
    #print(len(extracted))
    #print(extracted[0:0+8])
    #print(int("".join(map(str,extracted[0:0+8])),2))  #int(str,2)
    #print(chr(80))

    # Convert byte array back to string
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    # Cut off at the filler characters
    decoded = string.split("###")[0]

    # Print the extracted text
    #print("Successfully decoded: "+decoded)

    song.close()

    return decoded