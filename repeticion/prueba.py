import re
import string
from stop_words import get_stop_words


class StringsContador(object):

    @staticmethod
    def readfile(nombre):
        if len(nombre) == 0:
            raise ValueError("Empty NameFile")

        res = open(nombre, "r").read().split()

        if not res:
            raise ValueError("Empty File")

        return res

    @staticmethod
    def searchvalue(list, valueforsearch):
        for value in list:
            if valueforsearch == value:
                return list.index(valueforsearch)
        return -1

    @staticmethod
    def ArraysWithTextAndRepetitions(lines):
        auxarraytext = []
        auxarrayrepetitions = []
        stop_words = get_stop_words('spanish')

        for line in lines:
            line = re.sub('[%s]' % re.escape(string.punctuation), '', line)
            if line in stop_words:
                continue

            if len(auxarraytext) < 1:
                auxarraytext.append(line.upper())
                auxarrayrepetitions.append(1)
            else:
                position = StringsContador.searchvalue(
                    auxarraytext, line.upper())
                if position != -1:
                    auxarrayrepetitions[position] += 1
                else:
                    auxarraytext.append(line.upper())
                    auxarrayrepetitions.append(1)

        return auxarraytext, auxarrayrepetitions

    @staticmethod
    def returnListOrdenate(arraytext, Arrayrepetitions):
        listordenate = []
        while len(arraytext) > 0:
            value = max(Arrayrepetitions)
            position = Arrayrepetitions.index(value)
            listordenate.append(arraytext[position] + " :" + str(value))
            del arraytext[position], Arrayrepetitions[position]
        return listordenate

if __name__ == "__main__":
    ArrayWithText, StringsContador.ArrayWithRepetitions = StringsContador.ArraysWithTextAndRepetitions(
        StringsContador.readfile("textoLeer"))
    ListForPrint = StringsContador.returnListOrdenate(
        ArrayWithText, StringsContador.ArrayWithRepetitions)

    print(ListForPrint)
