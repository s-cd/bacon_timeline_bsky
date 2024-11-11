from atproto import Client
import time
client = Client()
client.login('username', 'password')

with open("text.txt", "r") as file:
    text = file.readlines()

i = 0
for t in text:
    filename = "pics/bacon" + str(i) +'.png'
    with open(filename, 'rb') as f:
        img_data = f.read()
    client.send_image(text=t.strip(), image=img_data, image_alt="bacon")
    print(t.strip())
    i += 1
    time.sleep(10)
