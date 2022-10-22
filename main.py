import csv
import json
from os import walk

app_path = input("Enter path to your Flutter application: ")
reference_arb_name = input("Enter the name of reference .arb file (where all strings are up-to-date): ")
app_translation_dir_path = app_path + '/' + 'lib/l10n/'

# all files in lib/l10n/ directory
l10n_file_names = next(walk(app_translation_dir_path), (None, None, []))[2]
arb_paths = []

# create all .arb paths
for file in l10n_file_names:
    if "arb" in file:
        arb_paths.append(app_translation_dir_path + file)

intl_en_dictionary = {}
translation_dictionaries = []

for file_path in arb_paths:
    # get dictionaries for all arb files
    if reference_arb_name not in file_path:
        with open(file_path, 'r', encoding='utf8') as f:
            translation_dictionaries.append(json.load(f))
    # get dictionary for reference file
    if reference_arb_name in file_path:
        with open(file_path, 'r', encoding='utf8') as f:
            intl_en_dictionary = json.load(f)

output_csv_file_path = app_translation_dir_path + "translations" + '.csv'

# Write to csv
with open(output_csv_file_path, mode='w', encoding='utf8') as csv_file:
    # create fieldnames for csv file key, en, fr, it...
    fieldnames = ['key', intl_en_dictionary['@@locale']]
    for dictionary in translation_dictionaries:
        fieldnames.append(dictionary['@@locale'])

    # create writer with fieldnames
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    for key in intl_en_dictionary:
        # add en key and value because it is referent
        mapToWrite = {'key': key, intl_en_dictionary['@@locale']: intl_en_dictionary[key]}
        # go through all keys for each language and check if exists,
        # if yes then add it, otherwise just add empty string
        for dictionary in translation_dictionaries:
            translationText = ""
            if key in dictionary.keys():
                translationText = dictionary[key]
            mapToWrite[dictionary['@@locale']] = translationText
        writer.writerow(mapToWrite)
