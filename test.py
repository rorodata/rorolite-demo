"""Script to call the background-removal API with an image.

USAGE: python test.py static/bird.jpg
"""
import firefly
import sys
import shutil
import yaml
import base64

config = yaml.safe_load(open("rorolite.yml"))
host = config['host']
port = config['services'][0]['port']

api = firefly.Client("http://{}:{}".format(host, port))

default_image_url = "https://rorodata-tmp.s3.amazonaws.com/liomessi.jpg"

def main():
    try:
        image_url = sys.argv[1]
    except IndexError:
        image_url = default_image_url

    print("calling the background removal API...")
    response = api.predict(image={"url": image_url})

    image_bytes = base64.b64decode(response['data'])
    with open("output.png", "wb") as f:
        f.write(image_bytes)
        
    print("saved the output image in output.png")

if __name__ == '__main__':
    main()
