from PIL import Image
from random import randint
def Twocolor(img):
    pixels=img.load()
    for i in range(img.width):
        Ready(img.width,i,'Twocolors')
        for j in range(img.height):
            r, g, b=pixels[i, j]
            middle=(r+g+b)//3
            if middle>32:
                r=255
                g=255
                b=255
            else:
                r=0
                g=0
                b=0
            pixels[i, j] = r, g, b
    return img
def add_color(color, add):
    if color+add>255:
        n=255
    elif color+add<0:
        n=0
    else:
        n=color+add
    return n
def Ready(width, i, name):
    g=i/width*100
    if g%10==0:
        print(name, 'Выполнено', int(g),'%')
def Mirror(img):
    a=0
    b=0
    c=img.width//2
    d=img.height
    pos=a,b,c,d
    twin=img.crop(pos)
    twin=twin.transpose(Image.FLIP_LEFT_RIGHT)
    e=img.width//2
    f=0
    g=img.width
    i=img.height
    img.paste(twin, (e,f,g,i))
    return img
def Grey(img):
    pixels=img.load()
    for i in range(img.width):
        Ready(img.width,i,'Grey')
        for j in range(img.height):
            r, g, b=pixels[i, j]
            middle=(r+g+b)//3
            r=middle
            b=middle
            g=middle
            pixels[i, j] = r, g, b
    return img
def Noise(img):
    pixels=img.load()    
    for i in range(img.width):
        Ready(img.width,i,'Noise')
        for j in range(img.height):
            z=randint(-100,100)
            r, g, b=pixels[i, j]
            r=add_color (r,z)
            g=add_color (g,z)
            b=add_color (b,z)
            pixels[i, j] = r, g, b
    return img
def Four_colors(img):
    z=150
    pixels=img.load()
    for i in range(img.width):
        Ready(img.width,i,'Fourcolors')
        for j in range(img.height):
            r, g, b=pixels[i, j]
            if i>img.width//2:
                if j>img.height//2:
                    r=add_color(r,z)
                else:
                    b=add_color(b,z)
                    g=add_color(g,z)
            else:
                if j>img.height//2:
                    g=add_color(g,z)
                else:
                    r=add_color(r,z)
                    b=add_color(b,z)
            pixels[i, j] = r, g, b
    return img
def Retro(img):
    pixels=img.load()
    for i in range(img.width):
        Ready(img.width,i,'Retro')
        for j in range(img.height):
            z=randint(-100,100)
            r, g, b=pixels[i, j]
            r=add_color(r,z)
            g=add_color(g,z)
            b=add_color(b,z)
            r=add_color(r,80)
            g=add_color(g,80)
            pixels[i, j] = r, g, b

    return img
def Blood_image(img):
    pixels=img.load()
    for i in range(img.width):
        Ready(img.width,i,'Bloodimage')
        for j in range(img.height):
            r, g, b=pixels[i, j]
            r=add_color(r,100)
            g=0
            b=0
            pixels[i, j] = r, g, b
    return img
def Sepia(img):
    pixels=img.load()
    for i in range(img.width):
        Ready(img.width,i,'Sepia')
        for j in range(img.height):
            r, g, b=pixels[i, j]
            r=112
            g=66
            b=20
            pixels[i, j]=r,g,b
    return img
