import subprocess
import sys
import os

def convert(filename_mp3, filename_wav):
    cd = os.getcwd()
    if not filename_wav: 
        filename_wav =  ".".join(filename_mp3.split(".")[0:-1]) + ".wav"
    if "/" not in filename_wav: cd + "/" + filename_wav
    if "/" not in filename_mp3: cd + "/" + filename_mp3
    
    subprocess.run(["mpg321", "-w", filename_wav, filename_mp3])

if __name__ == "__main__":
    filename_mp3 = sys.argv[1]
    filename_wav = None
    try:
        filename_wav = sys.argv[2]
    except IndexError:
        print("Target filename is not provided. Using the same name.")
        
    convert(filename_mp3, filename_wav)
    exit(0)