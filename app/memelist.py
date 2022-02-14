import os

folder = 'D:\\TarhunBot\\memes\\'

oxy = 'D:\\TarhunBot\\oxxxymiron\\'

memes = os.listdir(folder)

MemesList = []

for file in memes:
    MemesList.append(os.path.join(folder+file))

oxxxy = os.listdir(oxy)

OxyList = []

for x in oxxxy:
        OxyList.append(os.path.join(oxy+x))

CheList = [
    "Нет, ты чел",
    "Чел, ты лох",
    "Нет, ты лох",
    "Ты чел",
    'Чел, ты чел',
    "Ты лох, чел",
    "Ты лох и чел"
]

