__author__ = 'kamil'

import sqlite3
from tabulate import tabulate


class Planet():
    def __init__(self, name, number, diameter, to_sun, moons):
        self.name = name
        self.number = number
        self.diameter = diameter
        self.to_sun = to_sun
        self.moons = moons

    @property
    def tb_dist(self):
        """distance to sun (in astronomical units) estimated by Titius- Bode"""
        if self.number < 5:
            dist = 0.4 + 0.3*2**(self.number-2)
        else:
            dist = 0.4 + 0.3*2**(self.number-1)
        return dist

    @property
    def conquer(self):
        self.__conquer = conquer

    @conquer.setter
    def conquer(self, st):
        dist = self.to_sun - earth.to_sun
        if dist == 0:
            print("Really?")
        elif abs(dist) < 10**9:
            self.__conquer = st
            print("YOU HAVE CONQUERED", self.name.upper())
        else:
            print("Sorry, it is too far for you")


def create_table():
    c = conn.cursor()
    c.execute("CREATE TABLE planets (name PRIMARY KEY, number, diameter, to_sun, moons)")
    conn.commit()


def save_planet(planet):
    purchases = [planet.name, planet.number, planet.diameter, planet.to_sun, planet.moons]
    c = conn.cursor()
    try:
        c.execute("INSERT INTO planets VALUES (?,?,?,?,?)", purchases)
        conn.commit()
    except sqlite3.IntegrityError:
        print("This planet is already in database")


def sort_and_print():
    c = conn.cursor()
    order = input("Which order do you choose:\n\t-number of moons (type: moons),\n\t-number\n\t-name\n~")
    if order == "moons":
        for i in c.execute("SELECT * FROM planets ORDER BY moons"):
            print(i[0], i[4])
    elif order == "number":
        for i in c.execute("SELECT * FROM planets ORDER BY number"):
            print(i[0], i[1])
    elif order == "name":
        for i in c.execute("SELECT * FROM planets ORDER BY name"):
            print(i[0])
    else:
        print("Wrong choice")


def compare():
    tab = [["Planet", "Real dist. [a.u.]", "T-B dist. [a.u.]"], ["--------", "-------------------", "----------------"]]
    for i in all_planets:
        tab.append([i.name, i.to_sun/earth.to_sun, round(i.tb_dist, 2)])
    print(tabulate(tab))


def conquer():
    choice = input("Which planet?\n~")
    for i in all_planets:
        if choice.lower() == i.name.lower():
            i.conquer = True


def main():
    dec = ""

    while dec != "4":
        print(""" Choose:
                  1. Sort and print.
                  2. Compare distances with Titius- Bode estimation.
                  3. Conquer.
                  4. EXIT.""")
        dec = input("~")

        if dec == "1":
            sort_and_print()
        elif dec == "2":
            compare()
        elif dec == "3":
            conquer()
        elif dec == "4":
            break

"""MAIN"""
earth = Planet("Earth", 3, 12756, 149597887, 1)
mercury = Planet("Mercury", 1, 4879, 57909170, 0)
venus = Planet("Venus", 2, 12104, 108208926, 0)
mars = Planet("Mars", 4, 6805, 227936637, 2)
jupiter = Planet("Jupiter", 5, 142984, 778412027, 67)
saturn = Planet("Saturn", 6, 120536, 1426725413, 62)
uranus = Planet("Uranus", 7, 51118, 2870972220, 27)
neptune = Planet("Neptune", 8, 49528, 4498252900, 14)

all_planets = [earth, mercury, venus, mars, jupiter, saturn, uranus, neptune]

conn = sqlite3.connect("base.db")

main()
