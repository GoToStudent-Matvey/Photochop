from PIL import Image
from photofilters import *
print ('Приветствую вас в фоторедакторе Photochop')
while True:
    print ('Фильтры: 1:Grey, 2:Twocolors, 3:Fourcolors, 4:Retro, 5:Mirror, 6:Noise, 7:Sepia, 8:Bloodimage')
    choose=input('Выберите фильтр и картинку: ')
    choose=choose.split(' ')
    img=Image.open(choose[0])
    for i in choose:
            if i=='1':
                img=Grey(img)
            if i=='2':
                img=Twocolor(img)
            if i=='3':
                img=Four_colors(img)
            if i=='5':
                img=Mirror(img)
            if i=='6':
                img=Noise(img)
            if i=='4':
                img=Retro(img)
            if i=='8':
                img=Blood_image(img)
            if i=='7':
                img=Sepia(img)
    img.show()
    if input('\nСохранить? (y/n): ')=='y':
        img.save(input('Укажите путь: '))
    if input('Хотите отредактировать ещё один файл? (y/n)')=='n':
        exit()
    

