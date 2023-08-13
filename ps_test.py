# """
# test --> ation before tion
# """
#
# import pandas as pd
#
# pd.set_option('display.max_columns', None)
# pd.set_option('max_colwidth', None)
#
# # lt_brailleData = pd.read_csv(r'C:\Users\yang\Desktop\Coding\Braille-Translator\letters_braille.csv')
# # df_lt_brailleData = pd.DataFrame(lt_brailleData)
#
# ps_brailleData = pd.read_csv(r'C:\Users\yang\Desktop\Coding\Braille-Translator\prefix_suffix_braille.csv')
# df_ps_brailleData = pd.DataFrame(ps_brailleData)
#
# string = 'partition'
#
# prefix = string.startswith('part')
# suffix = string.endswith('tion')
#
# unicode_string = ''
# #
# # print(df_ps_brailleData['whole_word'])
# idx = 0
#
# for elem in df_ps_brailleData['partial_word']:
#     idx += 1
#     if string.endswith(elem):
#         prefix = df_ps_brailleData.iloc[idx - 1, 1]
#         suffix = df_ps_brailleData.iloc[idx - 1, 2]
#
#         unicode_string += chr(int(prefix))
#         unicode_string += chr(int(suffix))
#
#         string = string.replace(elem, '')
#
#         break
#
# print(string)
# print(unicode_string)
#
# # print(chr(10256))
# # print(chr(10255))
# # print(chr(10250))
# # print(chr(10288))
# # print(chr(10257))
#
# # if string.endswith()

string = 'abc hehehe'
a = string.split()
for i in range(len(a)):
    a.insert(i+1, ' ')

print(a)