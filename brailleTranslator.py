"""
1. find letter in dataset
2. get unicode
3. check whole word abrv (len 5 first --> len 1), whole word, single words, partial_word, connect word, letter
"""
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

lt_brailleData = pd.read_csv(r'C:\Users\yang\Desktop\Coding\Braille-Translator\letters_braille.csv')
df_lt_brailleData = pd.DataFrame(lt_brailleData)

partial_brailleData = pd.read_csv(r'C:\Users\yang\Desktop\Coding\Braille-Translator\partial_word.csv')
df_partial_brailleData = pd.DataFrame(partial_brailleData)

whole_brailleData = pd.read_csv(r'C:\Users\yang\Desktop\Coding\Braille-Translator\whole_word.csv')
df_whole_brailleData = pd.DataFrame(whole_brailleData)

numData = dict(digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])


def wholeStrUpperCase(string, unicode_string):
    capital_char = chr(10272)
    unicode_string += capital_char
    unicode_string += capital_char
    string = string.lower()

    return string, unicode_string


def checkWholeWord(string, unicode_string):
    idx = 0
    for elem in df_whole_brailleData['whole_word']:
        idx += 1
        if string.startswith(elem):
            prefix = df_whole_brailleData.iloc[idx - 1, 1]
            suffix = df_whole_brailleData.iloc[idx - 1, 2]

            unicode_string += chr(prefix)
            unicode_string += chr(suffix)

            string = string.replace(elem, '')
            break

    ans = [string, unicode_string]
    return ans


def checkPartialWord(string, unicode_string):
    idx = 0
    for elem in df_partial_brailleData['partial_word']:
        idx += 1
        if string.endswith(elem):
            prefix = df_partial_brailleData.iloc[idx - 1, 1]
            suffix = df_partial_brailleData.iloc[idx - 1, 2]

            unicode_string += chr(int(prefix))
            unicode_string += chr(int(suffix))

            string = string.replace(elem, '')

            break

    ans = [string, unicode_string]
    return ans


def translate(string):
    unicode_string = ''
    old_string = string.split()

    for word in old_string:

        if word.isupper():
            word, unicode_string = wholeStrUpperCase(word, unicode_string)

        newString, unicode_string = checkWholeWord(word, unicode_string)

        newString, unicode_string = checkPartialWord(newString, unicode_string)

        list_letter = list(newString)

        isNum = False

        for i in list_letter:
            if i.isupper():
                capital_char = chr(10272)
                unicode_string += capital_char
                i = i.lower()

            if i in numData['digits']:
                numSign_char = chr(10300)
                unicode_string += numSign_char

                letterBooleanList = df_lt_brailleData['letter'] == i
                letter_data = df_lt_brailleData.loc[letterBooleanList]
                letter_unicode = letter_data['unicode']
                braille_char = chr(letter_unicode)
                unicode_string += braille_char

                isNum = True

            else:
                if isNum:
                    letterSign_char = chr(10288)
                    unicode_string += letterSign_char

                letterBooleanList = df_lt_brailleData['letter'] == i
                letter_data = df_lt_brailleData.loc[letterBooleanList]
                letter_unicode = letter_data['unicode']
                braille_char = chr(letter_unicode)
                unicode_string += braille_char

        unicode_string += chr(10240)

    return unicode_string


print(translate('PARTITION hi f f ff'))

