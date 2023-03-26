import json
import random
import allfunction
from MyClasses import Question



questionsfromJSON=[]
with open("package.json", "r") as f1:
    questionsfromJSON = json.load(f1)


questions=[]
for vopros in questionsfromJSON:
    exemplarvoprosa = Question(vopros["q"],int(vopros["d"]),vopros["a"])
    questions.append(exemplarvoprosa)

YASOBERU=[]
schetchikvoprosov=0
while schetchikvoprosov < len(questions):
    voprosNOW=random.choice(questions)
    if voprosNOW.vopros_zadan == False:
        print(voprosNOW.build_question())
        voprosNOW.vopros_zadan = True
        otver=input()
        if voprosNOW.is_correct(otver):
            YASOBERU.append(voprosNOW.get_point())
            print(voprosNOW.positive_feedback())

        else:
            print(voprosNOW.negative_feedback())


        schetchikvoprosov+=1



allfunction.pokasz_staty(questions)