class Znak:
    def __init__(self, name, surname, znak, day, mounth, year):
        self.name = name
        self.surname = surname
        self.znak = znak
        self.birthday = [day, mounth, year]
    def __repr__(self):
        return "{0.surname} {0.name} {0.znak} {0.birthday[0]}.{0.birthday[1]}.{0.birthday[2]} ".format(self)

def foundznak(list):
    print("Введите людей с каким знаком хотите найти ")
    znakfound =checkstr()
    count=0
    for i in range(8):
        if znakfound == list[i].znak:
            print("С таким знаком зодиака найден человек: ", list[i].name, list[i].surname, list[i].birthday)
            count+=1
    if count==0:
        print("Человек с таким знаком зодиака не найден")



def checkint():
    while True:
        try:
           x = int(input())
           return x
        except ValueError:
            print("Введены некорректные данные")

def checkstr():
    while True:
        x=input()
        if  x and x.strip():
            return x
        else:
            print("Введены некорректные данные")

def sortclass(list1):
    for i in range(8):
        for j in range(8):
            if list1[i].birthday[2] < list1[j].birthday[2]:
                list1[i], list1[j] = list1[j], list1[i]
            elif list1[i].birthday[2] == list1[j].birthday[2]:
                if list1[i].birthday[1] < list1[j].birthday[1]:
                    list1[i], list1[j] = list1[j], list1[i]
                elif list1[i].birthday[1] == list1[j].birthday[1]:
                    if list1[i].birthday[0] < list1[j].birthday[0]:
                        list1[i], list1[j] = list1[j], list1[i]




def classJUSTdoit():
    list1 = list()
    for i in range(8):
        print("Введите данные человека № ",i+1)
        print("Имя: ")
        name = checkstr()
        print("Фамилия: ")
        surname = checkstr()
        print("Знак зодиака: ")
        znak = checkstr()
        print("День рождения: ")
        day = checkint()
        print("Месяц рождения: ")
        mounth = checkint()
        print("Год рождения: ")
        year = checkint()
        person = Znak(name, surname, znak, day, mounth, year)
        list1.append(person)
    sortclass(list1)
    print(list1)
    foundznak(list1)

def main():
    classJUSTdoit()

if __name__ == '__main__':
    main()
