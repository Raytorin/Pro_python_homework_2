import csv
import re


pattern = r"(\+7|8)\s*\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})((\s*)\(?(\w{3}\.?)\s*(\d{4})\)?)?"
example = r"+7(\2)\3-\4-\5\7\8\9"


def fix_phones(list_phones):
    for element_list in list_phones:
        lastname = element_list[0].strip()
        firstname = element_list[1].strip()
        separate_lastname = lastname.split()
        separate_firstname = firstname.split()
        if len(separate_lastname) > 1:
            i = 0
            while i < len(separate_lastname):
                element_list[i] = separate_lastname[i]
                i += 1
        elif len(separate_firstname) == 2:
            element_list[1] = separate_firstname[0]
            element_list[2] = separate_firstname[1]

        element_list[-2] = re.sub(pattern, example, element_list[-2])
    return list_phones


def string_compliment(list_for_compliment):
    for correct_string in list_for_compliment:
        correct_element1 = correct_string[0]
        correct_element2 = correct_string[1]
        for check_string in list_for_compliment:
            if correct_element1 == check_string[0] and correct_element2 == check_string[1]:
                count = 0
                while count < len(list_for_compliment[0]):
                    if len(correct_string[count]) < 1 and len(check_string[count]) >= 1:
                        correct_string[count] = check_string[count]
                    count += 1
    return list_for_compliment


def remove_duplicates(list_for_remove_duplicates):
    temp = []
    for temp_string in list_for_remove_duplicates:
        temp1 = []
        count_fields = 0
        while count_fields < len(list_for_remove_duplicates[0]):
            temp1.append(temp_string[count_fields])
            count_fields += 1
        if temp1 not in temp:
            temp.append(temp1)
    list_for_remove_duplicates = temp
    return list_for_remove_duplicates


if __name__ == '__main__':
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    step_1 = fix_phones(contacts_list)
    step_2 = string_compliment(step_1)
    result = remove_duplicates(step_2)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(result)