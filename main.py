import csv
import json
import os
from os import walk

app_path = input("Enter path to your Flutter application: ")
app_translation_dir_path = app_path + '/' + 'lib/l10n/'
output_csv_file_path = app_translation_dir_path + "translations" + '.csv'

arb_file_names = next(walk(app_translation_dir_path), (None, None, []))[2]  # [] if no file
arb_paths = []

# create all .arb paths
for file in arb_file_names:
    if "arb" in file:
        arb_paths.append(app_translation_dir_path + file)

# find intl_en.arb path
# intl_en_file_path = ""
# for file in arb_paths:
#     if "intl_en" in file:
#         intl_en_file_path = file

# go through all keys of en and compare to other dict translations and add if some key is missing check first if
# it exists in dictionary and take its text and add new item on correct position (same as intl_en) with its string
# otherwise just add item
intl_en_dict = {}
translation_dict = []

# get dictionaries for all arb files except intl_en
for file_path in arb_paths:
    if "intl_en" not in file_path:
        with open(file_path, 'r', encoding='utf8') as f:
            translation_dict.append(json.load(f))
    if "intl_en" in file_path:
        intl_en_dict = json.load(f)
        print()

# with open(intl_en_file_path, 'r', encoding='utf8') as f:
#     intl_en_dict = json.load(f)
# for key in list(intl_en_dict):
#     print(intl_en_dict[key])
    # if key.startswith('@') and key != '@@locale':
    #     del intl_dict[key]

# Write to csv
# with open(csv_file_path, mode='w', encoding='utf8') as csv_file:
#     fieldnames = ['key', 'string']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     for key in list(intl_dict):
#         writer.writerow({'key': key, 'string': intl_dict[key]})


