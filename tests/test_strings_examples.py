import unittest
from sample.strings_example import StringsExamples
from repeticion.prueba import StringsContador
from mock import patch, Mock


class TestStringsExamples(unittest.TestCase):

    def test_empty_file(self):
        file = "textoLeerVacio"
        try:
            StringsContador.readfile(file)
        except ValueError as e:
            assert str(e) == "Empty File"

    def test_empty_file_name(self):
        file = ''
        try:
            StringsContador.readfile(file)
        except ValueError as e:
            assert str(e) == "Empty NameFile"

    def test_no_special_chars(self):
        file = "textoCaracteresEspeciales"
        words = StringsContador.readfile(file)
        wordsWithoutPunctuation = StringsContador.ArraysWithTextAndRepetitions(
            words)
        res = wordsWithoutPunctuation[0][0]
        assert res == "CALABAZA"

    def test_no_stop_words(self):
        file = "textoConStopWords"
        words = StringsContador.readfile(file)
        wordsWithoutPunctuation = StringsContador.ArraysWithTextAndRepetitions(
            words)
        res = wordsWithoutPunctuation[0][0]
        assert res == "CALABAZA"

    def test_count_reps(self):
        file = "textoLeer"
        word = "HOLA"
        words = StringsContador.readfile(file)
        wordsWithoutPunctuation = StringsContador.ArraysWithTextAndRepetitions(
            words)
        index = wordsWithoutPunctuation[0].index(word)
        res = wordsWithoutPunctuation[1][index]
        assert res == 4

    def test_max_reps_word_is_in_index_zero(self):
        file = "textoLeer"
        word = "OCHO :4"
        words = StringsContador.readfile(file)
        wordsWithoutPunctuation = StringsContador.ArraysWithTextAndRepetitions(
            words)
        wordsOrdenate = StringsContador.returnListOrdenate(
            wordsWithoutPunctuation[0], wordsWithoutPunctuation[1])
        assert wordsOrdenate[0] == word

    def test_min_reps_word_is_in_index_max(self):
        file = "textoLeer"
        word = "CRACK :1"
        words = StringsContador.readfile(file)
        wordsWithoutPunctuation = StringsContador.ArraysWithTextAndRepetitions(
            words)
        wordsOrdenate = StringsContador.returnListOrdenate(
            wordsWithoutPunctuation[0], wordsWithoutPunctuation[1])
        assert wordsOrdenate[len(wordsOrdenate) - 1] == word

if __name__ == '__main__':
    unittest.main()
