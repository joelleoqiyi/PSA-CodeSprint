import requests
from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a struggling mark zuckerberg",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

image_response = requests.get(image_url)
if image_response.status_code == 200:
    with open('image_01.png', 'wb') as file:
        file.write(image_response.content)
        print("Image saved successfully!")
else:
    print(f"Failed to download image: {image_response.status_code}")