# Data to work with:

description = ('Country', ['2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 '])
raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 ', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 ', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 ', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 ', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 ', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]


def prepare_dataset(raw_data_list):
    country_keys_list = [country_code[0] for country_code in raw_data_list]  # get a list of all the country codes
    # print('Country codes list:')
    # print(country_keys_list)

    years_lst = (lambda years: years[1][::-1])(description)  # get a list of all the years decreasing
    # print('Years list: ')
    # print(years_lst)

    coverage_values_lists = [data[1][::-1] for data in
                             raw_data_list]  # get a list of coverage values of each sublist and invert to match example
    # print('Coverage values list of lists: ')
    # print(coverage_values_lists)
    # print('--------------------------------')
    country_data_list = generate_country_list_of_dictionaries(years_lst, coverage_values_lists)
    final_data = dict(zip(country_keys_list, country_data_list))
    # print(final_data)
    return final_data


def generate_country_list_of_dictionaries(yr_list, values_list_of_lists):
    all_countries_data = []
    for country_values in values_list_of_lists:
        individual_country_data = []
        for i in range(len(yr_list)):
            temp_individual_dict = (lambda yr, coverage: {'year': yr, 'coverage': coverage}) \
                (yr_list[i], country_values[i])
            individual_country_data.append(temp_individual_dict)
        all_countries_data.append(individual_country_data)

    return all_countries_data


def get_country_data(dataset, country_code):
    country_dict = {country_code: list(map(lambda d: (d['year'], int(d['coverage'])), dataset[country_code]))}
    return country_dict


def perform_average(data):
    numbers = [nr[1] for nr in data]
    return sum(numbers) / len(numbers)


# Should return something like this:
# {'2019': [('Romania', 84), ('Germany', 95), ..., ('Latvia', 85)]}

def get_year_data(dataset, year):
    year_dict = {
        year: list(map(lambda country_code, coverage_value: (country_code, coverage_value),
                       dataset.keys(),
                       [d['coverage'] for sublist in dataset.values() for d in sublist if d['year'] == (year + ' ')]
                       ))
    }
    return year_dict


def __main__():
    my_data = prepare_dataset(raw_data)
    yearly_data = get_year_data(my_data, '2019')
    print(yearly_data)
    country_data = get_country_data(my_data, 'RO')
    print(country_data)
    average_value = perform_average(country_data['RO'])
    print('Average value is: ' + str(average_value))


__main__()
