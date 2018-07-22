import random

class Probablity:

    """
        This module functions returns head or tail, rock or paper or scissors,
        dice or roll. It depends on what you want.
        Usage:
            dice_roll(int)
            head_tail()
            rock_paper_scissors()
    """


    def roll_dices(self,number_of_dices):
        faces = {
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
        }
        for i in range(number_of_dices):
            for  key,value in faces.items():
                if key == random.randint(0,6):
                    faces[key] = faces[key] + 1
        print("ZAR SAYISI:",number_of_dices)
        print("----ATILAN ZARLAR----")
        print("Toplam 1 gelme:",faces[1])
        print("Toplam 2 gelme:", faces[2])
        print("Toplam 3 gelme:", faces[3])
        print("Toplam 4 gelme:", faces[4])
        print("Toplam 5 gelme:", faces[5])
        print("Toplam 6 gelme:", faces[6])
        print("----ATILAN ZARLAR----")

    def head_or_tails(self):
        print("Yazı Tura:",random.choice(("Yazı","Tura")))

    def rock_paper_scissors(self):
        print("Taş Kağıt Makas:",random.choice(("Rock","Paper","Scissors")))