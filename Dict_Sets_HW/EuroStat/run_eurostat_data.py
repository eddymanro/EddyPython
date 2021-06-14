import xlrd
import pprint


def check_gender(gender):
    if gender == 'female':
        gen = 'F'
    else:
        gen = 'M'
    return gen


def check_year(year):
    if year == 2017:
        y_ind = 1
    else:
        y_ind = 2
    return y_ind


def get_raw_data(gender, year):
    countries_list = []
    health_index_list = []

    gen = check_gender(gender)
    yr_index = check_year(year)

    file_name = ('eurostat_' + gender + '.xls')
    wb = xlrd.open_workbook(file_name)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    nr_entries = sheet.nrows

    for i in range(nr_entries):
        countries_list.append(sheet.cell_value(i, 0))
        health_index_list.append(sheet.cell_value(i, yr_index))

    year_list = [year] * nr_entries
    gender_list = [gen] * nr_entries

    data_set = list(zip(countries_list, year_list, gender_list, health_index_list))
    return data_set


def get_dict_by_country_data(data):
    health_index_dict_by_country = {
        country: [sex, health_index] for country, _, sex, health_index in data
    }
    return health_index_dict_by_country


def get_country_specific_data(data, yr, country):
    country_dict = {yr: data.get(country)}
    return country_dict


def get_country_year_data(data):
    temp_country_year_dict = {
        (country + '_' + str(year)): [year, sex, health_index] for country, year, sex, health_index in data
    }
    # country_year_dict = {key: temp_country_year_dict.get(country)}
    return temp_country_year_dict


# created this function to check if the data is available
# if tried to check this directly in the dictionary comprehension together with the value condition
# it did not work because it would change all the items to string type and then the string cannot be compared to an int
# ex: the unavailable data for 'Kosovo' is ':', which is a string
# tried this:
# "key: value for (key, value) in filtered_dict.items() if (type(value[1]) == float) and (value[1] > 5.0)"
#
# therefore created this extra check-function
def create_dict_check_for_unavailable_data(temp_data):
    temp_dict = {
        key: value for (key, value) in temp_data.items() if type(value[1]) == float
    }
    return temp_dict


def filter_health_index_above_5(data_dict):
    filtered_dict = create_dict_check_for_unavailable_data(data_dict)
    filtered_dict = {
        key: value for (key, value) in filtered_dict.items() if value[1] > 5.0
    }
    return filtered_dict


def filter_health_index_and_sex(data_dict):
    filtered_dict = create_dict_check_for_unavailable_data(data_dict)
    # this filter little redundant since the check is done by the input and either the male or female data is selected
    filtered_dict = {
        key: value for (key, value) in filtered_dict.items() if (value[0] == 'F') and (value[1] > 10)
    }
    return filtered_dict


def __main__():
    gender = input('Enter gender that you would like to see, type "male" / "female": ')
    year = input('Enter the year that you would like to check, enter "2017" / "2018": ')

    if (gender == 'male' or gender == 'female') and (year == '2017' or year == '2018'):
        year = int(year)
        data_set = get_raw_data(gender, year)
    else:
        print('Some data was entered incorrectly')
        return 404

    pprint.pprint(data_set)
    health_index_dict_by_country = get_dict_by_country_data(data_set)
    pprint.pprint(health_index_dict_by_country)

    country = input('Enter country for which you would like to see the data: ')
    health_index_specific_by_country = get_country_specific_data(health_index_dict_by_country, year, country)
    pprint.pprint(health_index_specific_by_country)

    health_index_dict_by_country_and_year = get_country_year_data(data_set)
    pprint.pprint(health_index_dict_by_country_and_year)

    filter_data_1 = filter_health_index_above_5(health_index_dict_by_country)
    pprint.pprint(filter_data_1)

    filter_data_2 = filter_health_index_and_sex(health_index_dict_by_country)
    pprint.pprint(filter_data_2)


__main__()
