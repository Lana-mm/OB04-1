
class Weapon:
    def attack(self):
        return "Боец атакует с помощью неопределенного оружия!"


class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом!"


class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука!"


class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self):
        self.health -= 1
        return self.health <= 0


class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} сменил оружие на {type(weapon).__name__}!")

    def attack(self, monster: Monster):
        print(self.weapon.attack())
        if monster.take_damage():
            print("Монстр побежден!")
        else:
            print("Монстр еще в бою!")


def main():
    # Создаем бойца и монстра
    fighter = Fighter("Герой", Sword())
    monster = Monster(3)

    # Бой с мечом
    print("Боец выбирает меч.")
    fighter.attack(monster)

    # Бой с луком
    fighter.change_weapon(Bow())
    print("\nБоец выбирает лук.")
    fighter.attack(monster)
    fighter.attack(monster)
    fighter.attack(monster)

if __name__ == "__main__":
    main()
