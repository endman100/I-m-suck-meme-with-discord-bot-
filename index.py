import discord
import random
import json
import os
import cv2
import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image
TOKEN = 'Njk3Nzk1NzU1NDM5ODE2NzM1.Xo8e_A.rNHqHGK_f0U9sDgenf2MsNNCvIs'
with open("loli.json", 'r') as f:
    datastore = json.load(f)
mylist = list(os.listdir("./GIF/"))
print(mylist)
client = discord.Client()

# 指定 TTF 字體檔
fontPath = "./font/TW-Sung-98_1.ttf"
# 載入字體
font = ImageFont.truetype(fontPath, 150)
def getText(strTemp):
    npArray = np.zeros((1000, 1000, 3), dtype="uint8")
    # 將 NumPy 陣列轉為 PIL 影像
    imgPil = Image.fromarray(npArray)
    # 在圖片上加入文字
    draw = ImageDraw.Draw(imgPil)
    text_width, text_height = draw.textsize(strTemp, font=font)
    npArray = np.zeros((text_height, text_width, 3), dtype="uint8")
    npArray[:,:,:] = 255
    imgPil = Image.fromarray(npArray)
    draw = ImageDraw.Draw(imgPil)
    draw.text((0, 0),  strTemp, font = font, fill = (0, 0, 0))

    npArray = np.array(imgPil)
    return npArray
def putText(img, textArray):
    textArray = cv2.resize(textArray, (720, int(textArray.shape[0]/(textArray.shape[1]/720))))
    targetArr = np.where((textArray<128))
    # print(textArray[targetArr])
    img[targetArr[0]+400,targetArr[1],targetArr[2]] = textArray[targetArr]
    return img

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello World!')
    elif message.content.startswith('!help'):
        await message.channel.send('''instruction list\n!hello\nrandom <int>\n!loli\n!1011\n!fonu\n''')
    elif message.content.startswith('!fonu'):
        await message.channel.send(file=discord.File('fonu.jpg'))
    elif message.content.startswith('雉雞'):
        await message.channel.send(file=discord.File("littlechicken/dead.jpg"))
    elif message.content.startswith('random'):
        def Unicode():
            val = random.randint(0x0000,0xffff)
            return chr(val)
        intTemp = int(message.content.split(" ")[-1])
        await message.channel.send("".join([Unicode() for i in range(intTemp)]))
    elif message.content.startswith('!loli'):
        await message.channel.send(datastore[random.randint(0, len(datastore)-1)])
    elif message.content.startswith('!1011'):
        await message.channel.send(file=discord.File("./GIF/"+mylist[random.randint(0, len(mylist)-1)]))
    elif message.content.startswith('!我就爛'):
        strTemp = message.content.split(" ")[-1]
        # print(strTemp)
        img = cv2.imread('iambad.png')
        textArray = getText(strTemp)
        img = putText(img, textArray)

        cv2.imwrite('temp.png', img)
        await message.channel.send(file=discord.File("temp.png"))
    # elif message.content.startswith('幹'):
    #     await message.channel.send("雞雞")
    else:
        try:
            print(str(float(message.content)))
            await message.channel.send(str(float(message.content)*2))
        except:
            pass
        # await message.channel.send(str(int(message.content)*2))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)