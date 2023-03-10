# lichen_file = "testfile3.txt"


def unique_finder(filename):
    unique_species = []
    unique_choice = input("Which would you like to find unique instances of? Type F for families, G for genera, S for species: ")
    if unique_choice.lower() == "s":
        family_col = input("What column is the taxonomic family in? ")
        family_col = int(family_col) - 1
        genus_col = input("What column is the taxonomic genus in? ")
        genus_col = int(genus_col) - 1
        species_col = input("What column is the taxonomic species in? ")
        species_col = int(species_col) - 1
        with open(filename) as lichens:
            #header = lichens.readline()
            for line in lichens:
                lines = line.rstrip().split("\t")

                if f"{lines[family_col].lower()} {lines[genus_col].lower()} {lines[species_col].lower()}" not in unique_species:
                    unique_species.append(f"{lines[family_col].lower()} {lines[genus_col].lower()} {lines[species_col].lower()}")
    elif unique_choice.lower() == 'f':
        family_col = input("What column is the taxonomic family in? ")
        family_col = int(family_col) - 1
        with open(filename) as lichens:
            #header = lichens.readline()
            for line in lichens:
                lines = line.rstrip().split("\t")

                if f"{lines[family_col].lower()}" not in unique_species:
                    unique_species.append(f"{lines[family_col].lower()}")
    elif unique_choice.lower() == 'g':
        family_col = input("What column is the taxonomic family in? ")
        family_col = int(family_col) - 1
        genus_col = input("What column is the taxonomic genus in? ")
        genus_col = int(genus_col) - 1
        with open(filename) as lichens:
            #header = lichens.readline()
            for line in lichens:
                lines = line.rstrip().split("\t")

                if f"{lines[family_col].lower()} {lines[genus_col].lower()}" not in unique_species:
                    unique_species.append(f"{lines[family_col].lower()} {lines[genus_col].lower()}")

    print(len(unique_species))


def finder_98(filename):
    heading_list = []
    above_98_d = {}
    line_count = 0
    blast_id_column = int(input("What column is the BLAST Percent ID in? ")) - 1
    family_col = int(input("What column is the family assignment in? ")) - 1
    genus_col = int(input("What column is the genus assignment in? ")) - 1
    species_col = int(input("What column is the species assignment in? ")) - 1
    with open(filename) as lichens:
        header = lichens.readline()
        header = header.rstrip().split("\t")
        for heading in header:
            above_98_d[heading] = []
            heading_list.append(heading)
        for line in lichens:
            lines = line.rstrip().split("\t")
            line_count += 1
            if lines[blast_id_column] == '':
                continue
            elif lines[blast_id_column] == "multi-identity":
                continue
            elif float(lines[blast_id_column]) >= 98.0:
                for i, item in enumerate(lines):
                    if item != "0":
                        if f"{lines[family_col]} {lines[genus_col]} {lines[species_col]}" not in above_98_d[heading_list[i]]:
                            above_98_d[heading_list[i]].append(f"{lines[family_col]} {lines[genus_col]} {lines[species_col]}")
    above_98 = {}
    for head, value, in above_98_d.items():
        above_98[head] = len(value)
    print(line_count)
    return above_98


def finder_985(filename):
    heading_list = []
    above_985_d = {}
    blast_id_column = int(input("What column is the BLAST Percent ID in? ")) - 1
    family_col = int(input("What column is the family assignment in? ")) - 1
    genus_col = int(input("What column is the genus assignment in? ")) - 1
    species_col = int(input("What column is the species assignment in? ")) - 1
    with open(filename) as lichens:
        header = lichens.readline()
        header = header.rstrip().split("\t")
        for heading in header:
            above_985_d[heading] = []
            heading_list.append(heading)
        for line in lichens:
            lines = line.rstrip().split("\t")

            if lines[blast_id_column] == '':
                continue
            elif lines[blast_id_column] == "multi-identity":
                continue
            elif float(lines[blast_id_column]) >= 98.5:
                for i, item in enumerate(lines):
                    if item != "0":
                        if f"{lines[family_col]} {lines[genus_col]} {lines[species_col]}" not in above_985_d[heading_list[i]]:
                            above_985_d[heading_list[i]].append(f"{lines[family_col]} {lines[genus_col]} {lines[species_col]}")
    above_985 = {}
    for head, value, in above_985_d.items():
        above_985[head] = len(value)

    return above_985


def finder_regional(filename):
    heading_list = []
    regional_d = {}
    # species_list = []
    library_col = int(input("What column is the assessment of the regional database in? ")) - 1
    family_col = int(input("What column is the family assignment in? ")) - 1
    genus_col = int(input("What column is the genus assignment in? ")) - 1
    species_col = int(input("What column is the species assignment in? ")) - 1

    with open(filename) as regional:
        header = regional.readline()
        header = header.rstrip().split("\t")
        for heading in header:
            regional_d[heading] = []
            heading_list.append(heading)
        for line in regional:
            lines = line.rstrip().split("\t")
            if lines[library_col] == "yes":
                for i, item in enumerate(lines):
                    if item != "0":
                        if f"{lines[family_col]} {lines[genus_col]} {lines[species_col]}" not in regional_d[heading_list[i]]:
                            regional_d[heading_list[i]].append(f"{lines[family_col]} {lines[genus_col]} {lines[species_col]}")
                    else:
                        continue

    regional_lengths = {}
    for head, value, in regional_d.items():
        regional_lengths[head] = len(value)

    return regional_lengths


def family_number_finder_98(filename):
    family_d = {}
    family_col = int(input("What column is the family assignment in? ")) - 1
    blast_id_column = int(input("What column is the BLAST ID in? ")) - 1

    with open(filename) as families:
        header = families.readline()

        for line in families:
            lines = line.rstrip().split("\t")
            if lines[blast_id_column] == '':
                continue
            elif lines[blast_id_column] == "multi-identity":
                continue
            elif float(lines[blast_id_column]) >= 98.0:
                if lines[family_col].lower() not in family_d:
                    family_d[lines[family_col].lower()] = []
                    family_d[lines[family_col].lower()].append(f"{lines[family_col+1]} {lines[family_col+2]}")
                else:
                    if f"{lines[family_col+1]} {lines[family_col+2]}" not in family_d[lines[family_col].lower()]:
                        family_d[lines[family_col].lower()].append(f"{lines[family_col+1]} {lines[family_col+2]}")
                    else:
                        continue

    family_lengths = {}
    for head, value, in family_d.items():
        family_lengths[head] = len(value)

    return family_lengths


def family_number_finder_985(filename):
    family_d = {}
    family_col = int(input("What column is the family assignment in? ")) - 1
    blast_id_column = int(input("What column is the BLAST ID in? ")) - 1

    with open(filename) as families:
        header = families.readline()

        for line in families:
            lines = line.rstrip().split("\t")
            if lines[blast_id_column] == '':
                continue
            elif lines[blast_id_column] == "multi-identity":
                continue
            elif float(lines[blast_id_column]) >= 98.5:
                if lines[family_col].lower() not in family_d:
                    family_d[lines[family_col].lower()] = []
                    family_d[lines[family_col].lower()].append(f"{lines[family_col+1]} {lines[family_col+2]}")
                else:
                    if f"{lines[family_col+1]} {lines[family_col+2]}" not in family_d[lines[family_col].lower()]:
                        family_d[lines[family_col].lower()].append(f"{lines[family_col+1]} {lines[family_col+2]}")
                    else:
                        continue

    family_lengths = {}
    for head, value, in family_d.items():
        family_lengths[head] = len(value)

    return family_lengths


def regional_family_finder(filename):
    family_d = {}
    family_col = int(input("What column is the family assignment in? ")) - 1
    id_col = int(input("What column is the database assessment in? ")) - 1

    with open(filename) as families:
        header = families.readline()

        for line in families:
            lines = line.rstrip().split("\t")
            if lines[id_col] == "yes":
                if lines[family_col].lower() not in family_d:
                    family_d[lines[family_col].lower()] = []
                    family_d[lines[family_col].lower()].append(f"{lines[family_col + 1]} {lines[family_col + 2]}")
                else:
                    if f"{lines[family_col + 1]} {lines[family_col + 2]}" not in family_d[lines[family_col].lower()]:
                        family_d[lines[family_col].lower()].append(f"{lines[family_col + 1]} {lines[family_col + 2]}")
                    else:
                        continue

    family_lengths = {}
    for head, value, in family_d.items():
        family_lengths[head] = len(value)

    return family_lengths


def main_function():
    file_is = input("Please input filename: ")
    start = True
    while start:
        user_input = input("98 for 98 analysis, 98.5 for 98.5 analysis, R for Regional, \nU for Unique, F98 for Family "
                           "Finder 98, F98.5 for Family Finder 98.5, \nFR for Regional Family Finder, or X for exit: ")
        if user_input == "98":
            print(finder_98(file_is))
        elif user_input == "98.5":
            print(finder_985(file_is))
        elif user_input.lower() == "u":
            print(unique_finder(file_is))
        elif user_input.lower() == "r":
            print(finder_regional(file_is))
        elif user_input == "F98":
            print(family_number_finder_98(file_is))
        elif user_input == "F98.5":
            print(family_number_finder_985(file_is))
        elif user_input.lower() == "fr":
            print(regional_family_finder(file_is))
        elif user_input.lower() == "x":
            start = False


main_function()
