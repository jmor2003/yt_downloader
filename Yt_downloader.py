import yt_dlp
import ffmpeg

question = None
while question != "q":
    question = input("Please put in the link of the youtube video you want downloaded or put q to quit: ")
    if question == "q":
        break

    with yt_dlp.YoutubeDL() as ydl:
        try:
            ydl.download(question)
        except:
            print("An error has occured")
    
   
