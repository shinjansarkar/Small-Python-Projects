from gtts import gTTS

text="I am Shinjan"
translate=gTTS(text)
save_file_name=input("Enter a File Name=")
speech_save=translate.save(f"{save_file_name}.mp3")

