# Osztályok Létrehozása
# Bicikli absztrakt osztály létrehozása alap attribútumokkal (pl. típus, ár, állapot). (5 pont)
# Különböző típusú biciklik (pl. OrszágútiBicikli, HegyiBicikli) leszármaztatott osztályok létrehozása. (5 pont)
# Kölcsönző osztály létrehozása, amely több Bicikli objektumot tartalmaz,
# és saját attribútumokkal rendelkezik (pl. név). (10 pont)
# Kölcsönzés osztály létrehozása a biciklik kölcsönzésének kezelésére. (10 pont)

from abc import ABC, abstractmethod
from datetime import datetime

class Bicikli(ABC):
    def __init__(self, bicikli_id, marka, tipus, meret, fek, allapot="Szabad"):
        self.bicikli_id = bicikli_id
        self.marka = marka
        self.tipus = tipus
        self.meret = meret
        self.fek = fek
        self.allapot = allapot


    def __str__(self):
        return f"{self.tipus} {self.marka}, Méret: {self.meret}, Állapot: {self.allapot}"

    def foglalas_lemondasa(self):               #Kölcsönzések lemondásának lehetősége
        if self.allapot == "Foglalt":
            self.allapot = "Szabad"
            print(f"Foglalás lemondva: {self.marka}")
        else:
            print(f"Az adott bicikli nincs foglalva.")

class RoadBike(Bicikli):
    def __init__(self, bicikli_id, marka, meret, fek, allapot="Szabad"):
        super().__init__(bicikli_id, marka, "Road", meret, fek, allapot)

    def koltseg(self):
        return 3500

class TrekkingBike(Bicikli):
    def __init__(self, bicikli_id, marka, meret, fek, allapot="Szabad"):
        super().__init__(bicikli_id, marka, "Trekking", meret, fek, allapot)

    def koltseg(self):
        return 3200

class CrossTrekking(Bicikli):
    def __init__(self, bicikli_id, marka, meret, fek, allapot="Szabad"):
        super().__init__(bicikli_id, marka, "CrossTrekking", meret, fek, allapot)

    def koltseg(self):
        return 3300

class MountainBike(Bicikli):
    def __init__(self, bicikli_id, marka, meret, fek, allapot="Szabad"):
        super().__init__(bicikli_id, marka, "Mountain", meret, fek, allapot)

    def koltseg(self):
        return 3800

class SpeedBike(Bicikli):
    def __init__(self, bicikli_id, marka, meret, fek, allapot="Szabad"):
        super().__init__(bicikli_id, marka, "Speedbike", meret, fek, allapot)

    def koltseg(self):
        return 3000

# MTB bicikli:
MTB = MountainBike(bicikli_id=1, marka="MTB", meret="M", fek="Hidraulikus tárcsafék")
print(MTB)
# További biciklik
road_bike = RoadBike(bicikli_id=1, marka="KTM", meret="M", fek="Hidraulikus tárcsafék")
trekking_bike = TrekkingBike(bicikli_id=2, marka="Rockrider", meret="L", fek="V-fék")
cross_trekking_bike = CrossTrekking(bicikli_id=3, marka="Trek", meret="S", fek="Hidraulikus tárcsafék")
mtb = MountainBike(bicikli_id=4, marka="Cannondale", meret="XL", fek="V-fék")
speed_bike = SpeedBike(bicikli_id=5, marka="KTM", meret="S", fek="Hidraulikus tárcsafék")

print(road_bike)
print(trekking_bike)
print(cross_trekking_bike)
print(mtb)
print(speed_bike)

class Kolcsonzes:
    def __init__(self, kolcsonzo, biciklik):
        self.kolcsonzo = kolcsonzo
        self.biciklik = biciklik
        self.kezdeti_idopont = datetime.now()
        self.befejezesi_idopont = None

    def befejezes(self):
        self.befejezesi_idopont = datetime.now()

    def __str__(self):
        return f"Kölcsönzés kezdete: {self.kezdeti_idopont}, Befejezés: {self.befejezesi_idopont}, Kolcsonzo: {self.kolcsonzo.nev}"

class Kolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.biciklik = []
        self.kolcsonzott_biciklik = []  # Új lista hozzáadva

    def bicikli_hozzaad(self, bicikli):
        self.biciklik.append(bicikli)

    def bicikli_torol(self, bicikli):
        self.biciklik.remove(bicikli)

    def kolcsonzesek_listazasa(self):
        for bicikli in self.biciklik:
            print(f"{bicikli.marka} - {bicikli.tipus} - {bicikli.allapot}")

    def biciklik_kolcsonzese(self, biciklik, nap):
        for bicikli in biciklik:
            if bicikli.allapot != "Szabad":
                print(f"{bicikli.marka} nem elérhető.")
                return

        osszkoltseg = sum([bicikli.koltseg() for bicikli in biciklik])

        kolcsonzes = Kolcsonzes(self, biciklik)
        kolcsonzes.napok = nap
        kolcsonzes.osszkoltseg = osszkoltseg

        for bicikli in biciklik:
            bicikli.allapot = "Kölcsönzött"

        self.kolcsonzott_biciklik.append(kolcsonzes)

        print(f"A biciklik kölcsönözve {nap} napra, összköltség: {osszkoltseg} Ft.")

    def foglalas_lemondasa(self, bicikli):      #Kölcsönzések lemondásának lehetősége
        bicikli.foglalas_lemondasa()

    def kolcsonzesek_kilistazasa(self):         #Kölcsönzések listázásának lehetősége
        for kolcsonzes in self.kolcsonzott_biciklik:
            print(f"{kolcsonzes}")

#Proba
kolcsonzo = Kolcsonzo("Rent@Bike")
road_bike = RoadBike(bicikli_id=1, marka="KTM", meret="M", fek="Hidraulikus tárcsafék")
kolcsonzo.bicikli_hozzaad(road_bike)

# Proba
kolcsonzo = Kolcsonzo("Rent@Bike")
road_bike = RoadBike(bicikli_id=1, marka="KTM", meret="M", fek="Hidraulikus tárcsafék")

# Foglalás
road_bike.allapot = "Foglalt"
kolcsonzo.foglalas_lemondasa(road_bike)  # Foglalás lemondása

kolcsonzo.bicikli_hozzaad(road_bike)

# Kölcsönzés
kolcsonzo.biciklik_kolcsonzese([road_bike], nap=2)

# Foglalás lemondása
kolcsonzo.foglalas_lemondasa(road_bike)

# Kölcsönzések kilistázása
kolcsonzo.kolcsonzesek_kilistazasa()
