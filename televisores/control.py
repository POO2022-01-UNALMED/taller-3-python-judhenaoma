

import this


class Control:


    def __init__(self):

        self._tv=""
    

    def enlazar(self, televisor):
        self._tv = televisor
        televisor.control = this
    
    def getTv(self):
        return self._tv
    
    def setTv(self, tv):
        self._tv = tv

    


    def turnOn(self):
        self._tv._estado = True
    
    def turnOff(self):
        self._tv._estado = False
        
    def getEstado(self):
        return self._tv._estado
    
    def canalUp(self):
        if self._tv._estado == True:
            if self._tv._canal <= 120 and self._tv._canal >= 1:
                self._tv._canal += 1
    
    def canalDown(self):
        if self._tv._estado == True:
            if self._tv._canal <= 120 and self._tv._canal >= 1:
                self._tv._canal -= 1

    def volumenUp(self):
        if self._tv._estado == True:
            if self._tv._volumen <= 7 and self._tv._volumen >= 0:
                self._tv._volumen += 1
    
    def volumenDown(self):
        if self._tv._estado == True:
            if self._tv._volumen <= 7 and self.__tv.volumen >= 0:
                self._tv._volumen -= 1
    
    def setCanal(self, canal):
        self._tv._canal = canal


