import random
name = input("Введи имя\n")
print(f"Пользователь {name}\n")


def smeshivalka(slovo):
    slovodlasmeshivania=[]
    for i in slovo:
        if i != "\n":
            slovodlasmeshivania.append(i)
    random.shuffle(slovodlasmeshivania)
    return sobiralka(slovodlasmeshivania)


def sobiralka(smeshanoeslovo):
    slovokpokazu=""
    for i in smeshanoeslovo:
        slovokpokazu+=i
    return slovokpokazu

def bezperenosa(slovo):
    if slovo[-1]=="\n":
        return slovo[:len(slovo)-1]
    else:
        return slovo
otvetov=0
with open("words.txt", "r", encoding="utf-8") as f1:
    for stroka in f1:
        print(f"Угадай слово {smeshivalka(stroka)}")
        otvet=input()
        if bezperenosa(stroka.lower())==otvet.lower():
            print("Верно!")
            otvetov+=1
        else:
            print(f"Не верно, правильный ответ {stroka}")


with open("history.txt","a",encoding="utf-8") as f2:
    f2.write(f"{name} набрал {otvetov}!\n")

