import json
newslovar={}
def load_questions(file):
    with open(file, mode="r", encoding="utf-8") as f1:
        for stroka in f1:
            global newslovar
            newslovar = json.loads(stroka)
def risuempole():
    global newslovar
    a=newslovar
    for tema, cena in a.items():
        print(tema.ljust(15), end=" ")
        for key_iz_cena in cena:
            if cena[key_iz_cena]["asked"] == False:
                print("\t\t"+key_iz_cena, end= " ")
            else:
                print("\t""xxx", end=" ")
        print()

def parse_input():
    kategory=input("Введи категорию\n")
    price=input("Введи цену вопроса\n")
    return [kategory, price]

def show_question(selected):
    global newslovar
    a= newslovar
    if selected[0] in a and selected[1] in a[selected[0]]:

        print(a[selected[0]][selected[1]]['question'])
        a[selected[0]][selected[1]]["asked"]=True
    else:
        print("Нет такой рубрики/цены вопроса")

    otvet=input("Введите ответ\n")
    if otvet == a[selected[0]][selected[1]]["answer"]:
        print("Молодец")
    else:
        print("Не молодец")


def pokasz_staty(spisok_voprosov):
    itogoballov=0
    kol_vo_voprosov=0
    for item in spisok_voprosov:
        if item.balls>0:
            itogoballov+=item.balls
            kol_vo_voprosov+=1
    print(f"Вот и все!\nОтвечено верно {kol_vo_voprosov} из {len(spisok_voprosov)}\nНабрано баллов: {itogoballov}")

