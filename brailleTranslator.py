"""
1. find letter in dataset
2. get unicode
"""
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

brailleData = pd.read_csv(r'C:\Users\yang\Desktop\Coding\Braille-Translator\braile_as_unicode_csv.csv')
df_brailleData = pd.DataFrame(brailleData)

# df_brailleData = pd.DataFrame(brailleData)

# print(df_brailleData)

# letterBooleanList = df_brailleData['letter'] == letter
# letter_data = df_brailleData.loc[letterCBooleanList]
# letter_unicode = letterC_data['unicode']
#
# print(letterC_unicode)


def translate(string):
    list_letter = list(string)
    unicode_string = ''
    for i in list_letter:
        if i.isupper():
            capitalBooleanList = df_brailleData['letter'] == 'capital'
            capital_data = df_brailleData.loc[capitalBooleanList]
            capital_unicode = capital_data['unicode']
            capital_char = chr(capital_unicode)
            unicode_string += capital_char
            i = i.lower()

        letterBooleanList = df_brailleData['letter'] == i
        letter_data = df_brailleData.loc[letterBooleanList]
        letter_unicode = letter_data['unicode']
        braille_char = chr(letter_unicode)
        unicode_string += braille_char

    return unicode_string


print(translate('Hello world my name is Abigail'))
