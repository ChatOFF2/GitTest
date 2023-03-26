import allfunction

class Question:
    def __init__(self, text_voprosa, slojnost, vernii_variant,balls=0, vopros_zadan = False, otvet = None, ):
        self.text_voprosa=text_voprosa
        self.slojnost=slojnost
        self.vernii_variant=vernii_variant
        self.balls=balls
        self.vopros_zadan=vopros_zadan
        self.otvet=otvet

    def get_point(self):
        self.balls=self.slojnost*10
        return self.balls

    def is_correct(self, otvet):
        self.otvet=otvet
        if self.otvet==self.vernii_variant:
            return True
        else:
            return False

    def build_question(self):
        return str(f"Вопрос: {self.text_voprosa}\nСложность {self.slojnost}/5")

    def positive_feedback(self):
        return str(f"Ответ правильный, получено {self.balls} баллов")

    def negative_feedback(self):
        return str(f"Ответ не верный, верный ответ {self.vernii_variant}!")

