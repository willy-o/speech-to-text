import whisper

model = whisper.load_model("base")

result = model.transcribe("test.mp3")
file = open("test.txt", "w", encoding="utf-8")
file.write(result["text"])
# print(result["text"])
