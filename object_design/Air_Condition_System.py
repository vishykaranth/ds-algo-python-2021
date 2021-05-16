# Default Methods: AC.on(), AC.off(), AC.getTemp() to get current temperature, AC.heat(), AC.cool()
from enum import Enum


class AcMode(Enum):
    cool = 1
    heat = 0


class AcState(Enum):
    standby = 2
    on = 1
    off = 0


class AC():
    def on(self):
        pass

    def off(self):
        pass


class AirControlSystem:
    def __init__(self):
        self.__targetTemperature = 75
        self.__mode = AcMode.cool
        self.__state = AcState.off
        self.__ac = AC()

    def switchOn(self):
        if (self.__state == AcState.off):
            self.__state = AcState.on
            self.__ac.on()
        else:
            raise Exception("AC is already On")

    def switchOff(self):
        if (self.__state == AcState.on or self.__state == AcState.standby):
            self.__state = AcState.off
            if (self.__state == AcState.on):
                self.__ac.off()
        else:
            raise Exception("AC is already Off")

    def setACState(self):
        if (self.__state == AcState.off):
            raise Exception("AC is Off, please turn on the AC to set state")
        if (self.__mode == AcMode.heat):
            if (self.__targetTemperature > self.__ac.getTemp()):
                if (self.state == AcState.standby):
                    self.__state = AcState.on
                    self.__ac.on()
            else:
                if (self.state == AcState.on):
                    self.__state = AcState.standby
                    self.__ac.off()
        elif (self.__mode == AcMode.cool):
            if (self.__targetTemperature < getTemp()):
                if (self.state == AcState.standby):
                    self.__state = AcState.on
                    self.__ac.on()
            else:
                if (self.state == AcState.on):
                    self.__state = AcState.standby
                    self.__ac.off()

    def setTemp(self, temperature):
        if (self.__state == AcState.off):
            raise Exception("AC is Off, please turn on the AC to set temperature")
        self.__targetTemperature = temperature
        self.setACState()

    def setToHeat(self):
        if (self.__state == AcState.off):
            raise Exception("AC is Off, please turn on the AC to set mode")
        if (self.__mode == AcMode.heat):
            raise Exception("AC is already on heat")
        self.__mode = AcMode.heat
        self.__ac.heat()
        self.setACState()

    def setToCool(self):
        if (self.__state == AcState.off):
            raise Exception("AC is Off, please turn on the AC to set mode")
        if (self.__mode == AcMode.cool):
            raise Exception("AC is already on cool")
        self.__mode = AcMode.cool
        self.__ac.cool()
        self.setACState()
