from random import randint

dict = {}
with open("Users.txt") as file:
    for line in file:
        key, *value = line.split()
        dict[key] = value

with open('Users.txt', 'r') as Users:
    lines = Users.readlines()
    id = len(lines)+ 1

def register(login,password, id):
    try:
        with open("Users.txt", "a+") as file:
            file.seek(0)
            file.write(f"{login} {id} {password} 100 10 0 0 50 1 0")
            file.write("\n")
            print("Успешная регистрация")
    except:
        print("Ошибка")


def logins():
    try:
        global login, password
        profile = dict.get(login)
        for k, v in dict.items():
            if login == k and password == profile[1]:
                return print("Успешный логин")
        print("Неправильный логин или пароль")
        print("------------------------")
        print("Введите логин")
        login = input().lower()
        print("------------------------")
        print("Введите пароль")
        password = input().lower()
        print("------------------------")
        return logins()
    except:
        print("Ошибка : 404")
        return logins()



print("1)Регистрация")
print("2)Войти")
choise = int(input("Выберите действие: "))
if choise == 1:
    print("------------------------")
    print("Введите логин")
    login = input().lower()
    print("------------------------")
    print("Введите пароль")
    password = input().lower()
    print("------------------------")
    register(login,password, id)
if choise == 2:
    print("------------------------")
    print("Введите логин")
    login = input().lower()
    print("------------------------")
    print("Введите пароль")
    password = input().lower()
    print("------------------------")
    logins()

dict = {}
with open("Users.txt") as file:
    for line in file:
        key, *value = line.split()
        dict[key] = value


class Player:
    hpmax = int(dict.get(login)[2])
    hp = hpmax
    damage = int(dict.get(login)[3])
    money = int(dict.get(login)[4])
    xp = int(dict.get(login)[5])
    xpmax = int(dict.get(login)[6])
    lvl = int(dict.get(login)[7])
    respect = int(dict.get(login)[8])


p = Player()


class Goblin:
    hp = randint(30, 50)
    damage = randint(3, 10)
    name = "Goblin"
    xp = randint(10, 30)
    cooldown = 0


g = Goblin()


class TreasureSandyBeach:
    money = randint(5, 20)
    name = "Ценная ракушка"


s = TreasureSandyBeach()


class TreasureForestofThieves:
    money = randint(10, 50)
    name = "Сундук"


t = TreasureForestofThieves()


class Upgrade:
    power = 1
    hp = 2
    PowerLvl = 0
    HealthLvl = 0


u = Upgrade()


class Magic:
    lvlmagic = 0
    damagemagic = 0


m = Magic()


class Weapon:
    gun1_dmg = 5
    gun1_cost = 25
    gun1_buying = 0
    gun2_dmg = 10
    gun2_cost = 75
    gun2_buying = 0
    gun3_dmg = 15
    gun3_cost = 250
    gun3_buying = 0
    stick1_dmg = 10
    stick1_cost = 100
    stick1_buying = 0
    stick2_dmg = 20
    stick2_cost = 250
    stick2_buying = 0
    stick3_dmg = 50
    stick3_cost = 750
    stick3_buying = 0
    armor1_hp = 15
    armor1_cost = 50
    armor1_buying = 0
    armor2_hp = 30
    armor2_cost = 200
    armor2_buying = 0
    armor3_hp = 50
    armor3_cost = 500
    armor3_buying = 0
    armor4_hp = 100
    armor4_cost = 1500
    armor4_buying = 0


w = Weapon()

class arena:
    opponent = randint(1,2)
    boss = randint(1,10)
    ohp = randint(10,50)
    odmg = randint(5,25)
    bhp = randint(50,200)
    bdmg = randint(25,50)
    blucky = randint(1,10)
    cooldown = 0
    rand = randint(1,3)

ar = arena()


def menu(p):
    while True:
        print("------------------------")
        print(f"{login},Вы дома!")
        print("------------------------")
        print("1) Пойти на охоту")
        print("2) Посмотреть статистику")
        print("3) Отправиться на поиски сокровища")
        print("4) Пойти в город Альбром")
        print("5) Сохранить и выйти")
        try:
            a = int(input("Введите действие: "))

            if a == 1:
                menu_fight(p)
            if a == 2:
                menu_stats(p)
            if a == 3:
                menu_treasure(t)
            if a == 4:
                menu_city()
            if a == 5:
                menu_save()
            if a == 1827:
                p.lvl += 999
                p.money += 999
        except NameError:
            print("Введите действие: ")
        except SyntaxError:
            print("Введите действие: ")

def menu_save():
    with open('Users.txt', 'r') as Users:
        lines = Users.readlines()
    lines.insert(int(dict.get(login)[0]), f'{login} {id} {password} {p.hpmax} {p.damage} {p.money} {p.xp} {p.xpmax} {p.lvl} {p.respect}\n')
    del lines[int(dict.get(login)[0])-1]
    with open('Users.txt', 'w') as Users:
        Users.writelines(lines)

def menu_stats(p):
    print("Твоя статистика")
    print("------------------------")
    print(f"Уровень: {p.lvl}, Опыт {p.xp}/{p.xpmax}, Уважение: {p.respect}")
    print("------------------------")
    print("Навыки: ")
    print(f"Сила: {u.PowerLvl}")
    print(f"Живучесть: {u.HealthLvl}")
    print(f"Магия: {m.lvlmagic}")
    print("------------------------")
    print(f"hp: {p.hp}")
    print(f"physical damage: {p.damage}")
    print(f"Magic damage: {m.damagemagic}")
    print("------------------------")
    print(f"money: {p.money}")
    print("------------------------")
    input("Нажмите Enter")


def menu_treasure(t):
    print("------------------------")
    print("В какое место вы желаете пойти искать сокровища?")
    print("1) Лес варваров")
    print("2) Песчаный пляж")
    a = int(input("Сделайте свой выбор: "))
    print("------------------------")
    if a == 1:
        p.money += t.money
        print(f"Вы нашли: {t.name}, с {t.money} монет, и вы забираете себе их")
    if a == 2:
        p.money += s.money
        print(f"Вы нашли: {s.name}, и смогли продать её за {s.money} монет")
    t.money = randint(10, 50)
    t.name = "Сундук"
    s.money = randint(5, 20)
    s.name = "Драгоценная ракушка"
    input("Нажмите Enter")

def menu_city():
    n = 0
    print("------------------------")
    print("Город Альбром")
    print("------------------------")
    print("1) Зайти в магическую библиотеку")
    print("2) Пойти на арену")
    print("3) Заглянуть в оружейную лавку")
    print("4) Вернуться домой")
    a = int(input("Куда соизволите пройти: "))
    if a == 1:
        print("------------------------")
        if p.lvl < 2:
            print("Чтобы познать магию нужно быть 2 уровня!")
        elif p.lvl >= 2:
            print(f"1) Читать книги про магию. Вы владаете магией на {m.lvlmagic} уровне")
            b = int(input("Выберите действие: "))
            if b == 1:
                print("------------------------")
                p.lvl -= 1
                m.lvlmagic += 1
                m.damagemagic += randint(1, 7)
                print(f"Вы прочитали книгу и увеличили магический урон, теперь он равен {m.damagemagic}")
        menu_city()
    if a == 2:
        print("------------------------")
        print("Арена")
        f = 0
        while f == 0:
            print("------------------------")
            print("1) Напасть на противника")
            print("2) Уйти с арены")
            b = int(input("Что сделаете: "))
            if b == 1:
                ar.boss = randint(1,10)
                ar.opponent = randint(1,2)
                if ar.boss < 9:
                    print("------------------------")
                    ar.ohp = randint(10,50)
                    ar.odmg = randint(5,25)
                    ar.rand = randint(1,3)
                    while ar.ohp > 0 and p.hp > 0:
                        if ar.rand == 1 and ar.cooldown == 0:
                            print(f"Вы напали на Мечника у него {ar.ohp} хп и {ar.odmg} урона")
                        if ar.rand == 2 and ar.cooldown == 0:
                            print(f"Вы напали на Копейщика у него {ar.ohp} хп и {ar.odmg} урона")
                        if ar.rand == 3 and ar.cooldown == 0:
                            print(f"Вы напали на Разбойника у него {ar.ohp} хп и {ar.odmg} урона")
                        print("------------------------")
                        if ar.rand == 1:
                            print("1) Ударить Мечника мечом")
                        if ar.rand == 2:
                            print("1) Ударить Копейщика мечом")
                        if ar.rand == 3:
                            print("1) Ударить Разбойника мечом")
                        print("2) Выпить зелье регенерации.")
                        bplan = int(input("Что сделаете: "))
                        ar.cooldown += 1

                        if bplan == 1:
                            ar.ohp -= p.damage
                            print("------------------------")
                            if ar.ohp < 0:
                                ar.ohp = 0
                            if ar.rand == 1:
                                print(f"Вы ударили Мечника, у него осталось: {ar.ohp} хп")
                            if ar.rand == 2:
                                print(f"Вы ударили Копейщика, у него осталось: {ar.ohp} хп")
                            if ar.rand == 3:
                                print(f"Вы ударили Разбойника, у него осталось: {ar.ohp} хп")
                            p.hp -= ar.odmg
                            if ar.rand == 1:
                                print(f"Мечник ударил вас, у вас осталось {p.hp} хп")
                            if ar.rand == 2:
                                print(f"Копейщик ударил вас, у вас осталось {p.hp} хп")
                            if ar.rand == 3:
                                print(f"Разбойник ударил вас, у вас осталось {p.hp} хп")

                        if bplan == 2:
                            p.hp += randint(1, 7)
                            if p.hp > p.hpmax:
                                p.hp = p.hpmax
                            print(f"У тебя {p.hp}, здоровья")

                        if p.hp <= 0:
                            print("Вы мертвы")
                            print("------------------------")
                            print("...Game Over...")
                            menu_stats(p)

                        if ar.ohp <= 0:
                            if ar.opponent == 1:
                                p.damage += u.power
                                u.PowerLvl += 1
                                ar.cooldown = 0
                                print("------------------------")
                                print(f"Вы победили его, и прокачали навык: Сила. Теперь его уровень: {u.PowerLvl}")


                            if ar.opponent == 2:
                                p.hpmax += u.hp
                                u.HealthLvl += 1
                                ar.cooldown = 0
                                print("------------------------")
                                print(f"Вы победили его, и прокачали навык: Живучесть. Теперь его уровень: {u.HealthLvl}")
                            print("------------------------")
                            print("Вы покинули арену")
                            menu_city()

                if ar.boss > 8:
                    print("------------------------")
                    ar.bhp = randint(50,200)
                    ar.bdmg = randint(25,50)
                    print(f"Кажется вы напали на крутого противника (Паладин)... У него {ar.bhp} хп и {ar.bdmg} урона")
                    print("------------------------")
                    print("1) Атаковать его!")
                    print("2) Сбежать с позором...")
                    print("------------------------")
                    f = int(input("Что сделаете: "))
                    if f == 1:
                        while ar.bhp > 0 and p.hp > 0:
                            if ar.cooldown == 0:
                                print("------------------------")
                                print(f"Вы решаетесь атаковать Паладина и бросаетесь в бой! У него: {ar.bhp} хп, {ar.bdmg} урона.  Вас стали уважать чуть больше.")
                                p.respect += 1
                            print("------------------------")
                            print("1) Ударить Паладина противника мечом ")
                            print("2) Выпить зелье регенерации.")
                            ar.cooldown += 1
                            bplan = int(input("Что сделаете: "))

                            if bplan == 1:
                                ar.bhp -= p.damage
                                print(f"Вы ударили Паладина, у него осталось: {ar.bhp} хп")
                                p.hp -= ar.bdmg
                                print(f"Паладин ударил вас, у вас осталось {p.hp} хп")

                            if bplan == 2:
                                p.hp += randint(1, 7)
                                if p.hp > p.hpmax:
                                    p.hp = p.hpmax
                                print(f"У тебя {p.hp}, здоровья")

                            if p.hp <= 0:
                                print("Вы мертвы")
                                print("------------------------")
                                print("...Game Over...")
                                menu_stats(p)

                            if ar.bhp <= 0:
                                ar.bhp = 0
                                if ar.opponent == 1:
                                    p.damage += u.power*5
                                    u.PowerLvl += 1
                                    ar.cooldown = 0
                                    print(f"Вы победили его, и прокачали навык: Сила. Теперь его уровень: {u.PowerLvl}")

                                if ar.opponent == 2:
                                    p.hpmax += u.hp*5
                                    u.HealthLvl += 1
                                    ar.cooldown = 0
                                    print(f"Вы победили его, и прокачали навык: Живучесть. Теперь его уровень: {u.HealthLvl}")
                                print("------------------------")
                                print("Вы покинули арену")
                                menu_city()
                    if f == 2:
                        ar.blucky = randint(1,10)
                        if ar.blucky > 8:
                            print("-----------------------")
                            print("Увидев такого крутого противника, вы не задумываясь побежали от него подальше, но на выходе с арены вас поджидали его дружки, они отняли у вас деньги")
                            p.money = 0
                            print("С позором вы уходите с арены...")
                            print("-----------------------")
                            print("Вы покинули арену")
                            print("-----------------------")
                        if ar.blucky < 9:
                            print("Тот час как вы увидели своего противника, бросились прочь от него.")
                            print("-----------------------")
                            print("Вы покинули арену")
                            menu_city()
            if b == 2:
                print("------------------------")
                print("Вы покинули арену")
                menu_city()




    if a == 3:
        n = 0
        d = 0
        while d == 0:
            print("------------------------")
            r = randint(1,3)
            if n == 0:
                if r == 1:
                    print("Вы заходите в лавку и видите, как продавец ругается на покупателя")
                if r == 2:
                    print("Заходя в лавку, вы случайно задеваеете красавицу в доспехах, она вам подмигивает и вы начинаете рассматривать товары")
                if r == 3:
                    print("Только вы захотели отпереть дверь, но какой-то человек с другой стороны её толкнул и выбежал, вслед за ним выбежал продавец и прокричал: Ах, ты вор! После этого вы благополучно заходите в лавку")
                print("------------------------")
                n += 1
            print("1) Мечи")
            print("2) Посохи")
            print("3) Доспехи")
            print("4) Выйти из лавки")
            b = int(input("Выберите товар: "))
            if b == 1:
                print("------------------------")
                if w.gun1_buying == 0:
                    print("1) Железный меч")
                elif w.gun1_buying == 1:
                    print("1) У вас куплен железный меч")
                if w.gun2_buying == 0 :
                    print("2) Аклахидовый меч")
                elif w.gun2_buying == 1:
                    print("У вас куплен аклахидовый меч")
                if w.gun3_buying == 0:
                    print("3) Рассекающий пространство меч")
                elif w.gun3_buying == 1:
                    print("3) У вас куплен рассекающий пространство меч")
                c = int(input("Выберите меч: "))
                if c == 1 and w.gun1_buying < 1:
                    if p.money >= w.gun1_cost:
                        print("------------------------")
                        print(f"Вы успешно приобрели Железный меч, ваш физический урон увеличен на {w.gun1_dmg} урона ")
                        p.damage += w.gun1_dmg
                        w.gun1_buying += 1
                        p.money -= w.gun1_cost
                    elif p.money < w.gun1_cost:
                        r = w.gun1_cost - p.money
                        print("------------------------")
                        print(f"У вас не хватает {r} монет")
                if c == 2 and w.gun2_buying < 1:
                    if p.money >= w.gun2_cost:
                        print("------------------------")
                        print(f"Вы успешно приобрели аклахидовый меч, ваш физический урон увеличен на {w.gun2_dmg} урона ")
                        p.damage += w.gun2_dmg
                        w.gun2_buying += 1
                        p.money -= w.gun2_cost
                    elif p.money < w.gun2_cost:
                        r = w.gun2_cost - p.money
                        print("------------------------")
                        print(f"У вас не хватает {r} монет")
                if c == 3 and w.gun3_buying < 1:
                    if p.money >= w.gun3_cost:
                        print("------------------------")
                        print(f"Вы успешно приобрели рассекающий пространство меч, ваш физический урон увеличен на {w.gun3_dmg} урона ")
                        p.damage += w.gun3_dmg
                        w.gun3_buying += 1
                        p.money -= w.gun3_cost
                    elif p.money < w.gun3_cost:
                        r = w.gun3_cost - p.money
                        print("------------------------")
                        print(f"У вас не хватает {r} монет")

            if b == 2:
                print("------------------------")
                if w.stick1_buying == 0:
                    print("1) Деревянный посох")
                if w.stick1_buying == 1:
                    print("1) У вас куплен деревянный посох")
                if w.stick2_buying == 0:
                    print("2) Азамантовый посох")
                if w.stick2_buying == 1:
                    print("2) у вас куплен азамантовый посох")
                if w.stick3_buying == 0:
                    print("3) Мистический посох")
                if w.stick3_buying == 1:
                    print("У вас куплен мистический посох")
                c = int(input("Выберите посох: "))
                if c == 1 and w.stick1_buying < 1:
                    if p.money >= w.stick1_cost:
                        print("------------------------")
                        print(f"Вы успешно приобрели Деревянный посох, ваш магический урон увеличен на {w.stick1_dmg} урона ")
                        m.damagemagic += w.stick1_dmg
                        w.stick1_buying += 1
                        p.money -= w.stick1_cost
                    elif p.money < w.gun1_cost:
                        r = w.gun1_cost - p.money
                        print("------------------------")
                        print(f"У вас не хватает {r} монет")
                if c == 2 and w.stick2_buying < 1:
                    if p.money >= w.stick2_cost:
                        print("------------------------")
                        print(f"Вы успешно приобрели Азамантовый посох, ваш магический урон увеличен на {w.stick2_dmg} урона ")
                        m.damagemagic += w.stick2_dmg
                        w.stick2_buying += 1
                        p.money -= w.stick2_cost
                    elif p.money < w.gun2_cost:
                        r = w.gun2_cost - p.money
                        print("------------------------")
                        print(f"У вас не хватает {r} монет")
                if c == 3 and w.stick3_buying < 1:
                    if p.money >= w.stick3_cost:
                        print("------------------------")
                        print(f"Вы успешно приобрели Мистический посох, ваш магический урон увеличен на {w.stick3_dmg} урона ")
                        m.damagemagic += w.stick3_dmg
                        w.stick3_buying += 1
                        p.money -= w.stick3_cost
                    elif p.money < w.gun3_cost:
                        r = w.gun3_cost - p.money
                        print("------------------------")
                        print(f"У вас не хватает {r} монет")
            if b == 3:
                print("------------------------")
                if w.armor1_buying == 0:
                    print("1) Кольчужные доспехи")
                if w.armor1_buying == 1:
                    print("1) У вас куплены кольчужные доспехи")
                if w.armor2_buying == 0:
                    print("2) Железные доспехи")
                if w.armor2_buying == 1:
                    print("2) У вас куплены железные доспехи")
                if w.armor3_buying == 0:
                    print("3) Аклахидовые доспехи")
                if w.armor3_buying == 1:
                    print("3) У вас куплены аклахидовые доспехи")
                if w.armor4_buying == 0:
                    print("4) Легендарные доспехи")
                if w.armor4_buying == 1:
                    print("4) У вас куплены легендарные доспехи")
                c = int(input("Выберите доспехи: "))
                if c == 1 and w.armor1_buying < 1:
                    if p.money >= w.armor1_cost:
                        print("------------------------")
                        print(f"Вы успешно приобрели Кольчужные доспехи, ваше здоровье увеличено на {w.armor1_hp} хп ")
                        p.hpmax += w.armor1_hp
                        if p.hp < p.hpmax:
                            p.hp = p.hpmax
                        w.armor1_buying += 1
                        p.money -= w.armor1_cost
                    if p.money < w.armor1_cost:
                        r = w.armor1_cost - p.money
                        print("------------------------")
                        print(f"У вас не хватает {r} монет")
                if c == 2 and w.armor2_buying < 1:
                    if p.money >= w.armor2_cost:
                        print("------------------------")
                        print(f"Вы успешно приобрели Железные доспехи, ваше здоровье увеличено на {w.armor2_hp} хп ")
                        p.hpmax += w.armor2_hp
                        if p.hp < p.hpmax:
                            p.hp = p.hpmax
                        w.armor2_buying += 1
                        p.money -= w.armor2_cost
                    if p.money < w.armor2_cost:
                        r = w.armor2_cost - p.money
                        print("------------------------")
                        print(f"У вас не хватает {r} монет")
                if c == 3 and w.armor3_buying < 1:
                    if p.money >= w.armor3_cost:
                        print("------------------------")
                        print(f"Вы успешно приобрели Аклахидовые доспехи, ваше здоровье увеличено на {w.armor3_hp} хп ")
                        p.hpmax += w.armor3_hp
                        if p.hp < p.hpmax:
                            p.hp = p.hpmax
                        w.armor3_buying += 1
                        p.money -= w.armor3_cost
                    if p.money < w.armor3_cost:
                        r = w.armor3_cost - p.money
                        print("------------------------")
                        print(f"У вас не хватает {r} монет")
                if c == 4 and w.armor4_buying < 1:
                    if p.money >= w.armor4_cost:
                        print("------------------------")
                        print(f"Вы успешно приобрели Легендарные доспехи, ваше здоровье увеличено на {w.armor4_hp} хп ")
                        p.hpmax += w.armor4_hp
                        if p.hp < p.hpmax:
                            p.hp = p.hpmax
                        w.armor4_buying += 1
                        p.money -= w.armor4_cost
                    if p.money < w.armor4_cost:
                        r = w.armor4_cost - p.money
                        print("------------------------")
                        print(f"У вас не хватает {r} монет")
            if b == 4:
                print("------------------------")
                print("Вы вышли из лавки")
                menu_city()

    if a == 4:
        menu(p)


def menu_fight(p):
    if g.hp <= 0:
        g.hp = randint(30, 50)
        g.damage = randint(3, 10)
        g.xp = randint(10, 30)
        g.cooldown = 0
    while g.hp > 0:
        print("------------------------")
        if g.cooldown == 0:
            print(f"У вас hp: {p.hp} damage: {p.damage}")
            print(f"Вы напали на врага {g.name}. У врага хп: {g.hp} damage: {g.damage}")
        print("------------------------")
        print(f"1) Ударить {g.name} мечом ")
        print("2) Выпить зелье регенерации")
        g.cooldown += 1
        if m.damagemagic > 0:
            print("3) Стрельнуть Файерболом")
        print("------------------------")
        a = int(input("Введите действие: "))
        print("------------------------")

        if a == 1:
            g.hp -= p.damage
            print(f"Вы ударили противника {g.name} , у него осталось: {g.hp} хп")
            p.hp -= g.damage
            print(f"{g.name} ударил вас, у вас осталось {p.hp} хп")

        if a == 2:
            p.hp += randint(1, 7)
            if p.hp > p.hpmax:
                p.hp = p.hpmax
            print(f"У тебя {p.hp}, здоровья")

        if a == 3 and m.damagemagic > 0:
            g.hp -= m.damagemagic
            print(f"Вы стрельнули файерболом в {g.name}, у него осталось {g.hp} хп")
            p.hp -= g.damage
            print(f"{g.name} ударил вас, у вас осталось {p.hp} хп")

        if p.hp < 0:
            print("Вы мертвы")

        if g.hp < 0:
            print(f"Вы убили {g.name}, и получили {g.xp} опыта")
            p.xp += g.xp
            if p.xp >= p.xpmax:
                p.lvl += 1
                p.xp -= p.xpmax


menu(p)