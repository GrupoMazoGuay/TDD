import urllib2

class StringsExamples(object):
    """A class to play with the strings"""

    @staticmethod
    def concat_strings(string1, string2):
        if type(string1) is not str or type(string2) is not str:
            raise TypeError
        return string1+string2

    @staticmethod
    def get_first_string():
        response = urllib2.urlopen('https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt')
        full_text = response.read()
        text_tokenized = full_text.split(' ')
        return text_tokenized[0]
