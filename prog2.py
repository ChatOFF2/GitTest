import json
import allfunction
questions={"Транспорт":
{"100": {"question": "plane", "answer": "самолет", "asked": False},
  "200": {"question": "train", "answer": "поезд", "asked": False},
  "300": {"question": "boarding", "answer": "доска", "asked": False}},
           "Животные":
{"100": {"question": "dog", "answer": "собака", "asked": False},
  "200": {"question": "shark", "answer": "акула", "asked": False},
  "300": {"question": "sparrow", "answer": "воробей", "asked": False}},
           "Пища":
{"100": {"question": "apple", "answer": "яблоко", "asked": False},
  "200": {"question": "berry", "answer": "ягода", "asked": False},
  "300": {"question": "venison", "answer": "оленина", "asked": False}}

}

with open("questions.json", mode="w", encoding="utf-8") as f1:
    json.dump(questions, f1)

allfunction.load_questions("questions.json")

a = 0
while a < 8:
    allfunction.risuempole()
    selected=allfunction.parse_input()
    allfunction.show_question(selected)
    a+=1
