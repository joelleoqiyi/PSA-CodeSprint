from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1-hd",
    voice="nova",
    input="Hi!!!!!!!!!!!!!!! I'm so excited to meet you!!!!!!!!!!! How have you been? I love working with you so much, I have great plans for the future!!!!!!!!!!!!!",
)

response.stream_to_file("output.mp3")