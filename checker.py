from wand.image import Image
from wand.display import display
import time
import os
# from wand.display import display
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import base64

from wand.api import library
from ctypes import c_void_p, c_size_t
import base64
from io import BytesIO


def send_notification(title,img):
    print("notifikace")
    return
    url = 'https://www.pushsafer.com/api'
    post_fields = { 
        "t" : title,
        "m" : "https://www.etoro.com/people/aimstrader/portfolio",
        "s" : 10,
        "v" : 3,
        "i" : 1,
        "c" : "",
        "d" : "a",
        "u" : "https://www.etoro.com/people/aimstrader/portfolio",
        "ut" : "",
        "pr" : "2",
        "p" : img,
        "k" : "zGpXkVtbxElxZLPAasd4"
        }

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)


def screenshot():
    # cmd = "firefox -screenshot https://www.etoro.com/people/aimstrader/portfolio "
    os.system("import -window 0x3c00001 -crop 400x400+240+400 ./screenshot.png")


def are_images_same(img1,img2):
    img = Image(filename=img1)
    im = Image(filename=img2)
    # return os.path.getsize(img1) == os.path.getsize(img2)


    comparison = img.compare(im, metric='root_mean_square')[1]
    print(str(comparison))
    if comparison == 0:
        return True
    return False

if __name__ == "__main__":
    # display = Display(visible=0, size=(1800, 1600))
    # display.start()
    sendimg =  base64.b64encode(open("screenshot.png", "rb").read()).decode('UTF-8')
    sendimg = "data:image/png;base64," + sendimg
    while True:
        try:
            time.sleep(20)
            os.system("cp screenshot.png before_screenshot.png")
            print("loop")
            try:
                screenshot()
            except Exception as e:
                print(e)
                send_notification("ETORO-screenshot",sendimg) # TODO musi byt alert i pri navraceni,
                continue
            if not are_images_same("before_screenshot.png", "screenshot.png"):
                sendimg =  base64.b64encode(open("screenshot.png", "rb").read()).decode('UTF-8')
                sendimg = "data:image/png;base64," + sendimg
                send_notification("ETORO-ZMENA",sendimg) # TODO musi byt alert i pri navraceni,


        except Exception as e:
            send_notification("ETORO - crash",sendimg) # TODO musi byt alert i pri navraceni,
            print(e)
