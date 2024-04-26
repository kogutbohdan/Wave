class Wave:
    def type(self):
        print("Хвилі")

class RadioWave(Wave):
    def type(self):
        print("Радіо")
        super().type()

class Sound(Wave):
    def type(self):
        print("Звукові")
        super().type()

class VisibleWave(Wave):
    def type(self):
        print("Видимі")
        super().type()

class InfraRadWave(Wave):
    def type(self):
        print("інфра червоні")
        super().type()

class UltraVioletWave(Wave):
    def type(self):
        print("Ультра фіолетові")
        super().type()

class GammaWave(Wave):
    def type(self):
        print("Гамма випромінювання")

class RengenWave(Wave):
    def type(self):
        print("Ренгенівські")
        super().type()

class Ration:
    def wave(self):
        print("Рація випромінює")
        Sound().type()
        RadioWave().type()

class Drotil:
    def wave(self):
        print("Вибух дротилу випромінює")
        Sound().type()
        VisibleWave().type()
        InfraRadWave().type()
        RadioWave().type()

class Bulb:
    def wave(self):
        print("Лампочка може випромінювати")
        VisibleWave().type()
        InfraRadWave().type()
        UltraVioletWave().type()

class Sun:
    def wave(self):
        print("Сонце може випромінювати")
        InfraRadWave().type()
        VisibleWave().type()
        UltraVioletWave().type()
        GammaWave().type()
        RengenWave().type()


Bulb().wave()
print("Рація-________________________________________________________________")
Ration().wave()

