from gtts import gTTS
save_directory="/home/shinjan/Desktop/Code/Python/text to speech/"
text="I am Shinjan"
translate=gTTS(text)
save_file_name=input("Enter a File Name=")
speech_save=translate.save(f"{save_directory}{save_file_name}.mp3")

