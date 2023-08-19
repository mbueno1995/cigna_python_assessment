from utils import read_csv, get_min_value, get_max_value, get_avg_value, dict_to_xml
import json
if __name__ == '__main__':
    csv_fpath = 'data.csv'
    json_fpath = 'json_results.json'
    txt_fpath = 'txt_results.txt'
    xml_fpath = 'xml_results.xml'
    dicts_to_write_in_json = []
    dicts_to_write_in_xml = []

    # Read the csv file
    list_of_dicts = read_csv(csv_fpath)


    # Write the generated dictionaries for the
    # minimum value, maximum value, and average value
    # for each unique hostname in the json file
    with open(json_fpath,'w') as json_file:
        # Print the minimum value of each unique hostname
        dicts_min_val = get_min_value(list_of_dicts)
        print('Minimum value of each unique hostname')
        for k,v in dicts_min_val.items():
            print(f'{k}:{v}', end=' ')
        
        # Print the maximum value of each unique hostname
        dicts_max_val = get_max_value(list_of_dicts)
        print('\n\nMaximum value of each unique hostname')
        for k,v in dicts_max_val.items():
            print(f'{k}:{v}', end=' ')

        # Print the average value of each unique hostname
        get_avg_value(list_of_dicts)
        dicts_avg_val = get_avg_value(list_of_dicts)
        print('\n\nAverage value of each unique hostname')
        for k,v in dicts_avg_val.items():
            print(f'{k}:{v}', end=' ')

        # Write the results to a json file
        dicts_to_write_in_json.append(dicts_min_val)
        dicts_to_write_in_json.append(dicts_max_val)
        dicts_to_write_in_json.append(dicts_avg_val)
        js = json.dumps(dicts_to_write_in_json)
        json_file.write(js)

    # Write the generated dictionaries for the
    # minimum value, maximum value, and average value
    # for each unique hostname in the xml file
    with open(xml_fpath,'w') as xml_file:
        # Print the minimum value of each unique hostname
        dicts_min_val = get_min_value(list_of_dicts)
        print('Minimum value of each unique hostname')
        for k,v in dicts_min_val.items():
            print(f'{k}:{v}', end=' ')
        
        # Print the maximum value of each unique hostname
        dicts_max_val = get_max_value(list_of_dicts)
        print('\n\nMaximum value of each unique hostname')
        for k,v in dicts_max_val.items():
            print(f'{k}:{v}', end=' ')

        # Print the average value of each unique hostname
        get_avg_value(list_of_dicts)
        dicts_avg_val = get_avg_value(list_of_dicts)
        print('\n\nAverage value of each unique hostname')
        for k,v in dicts_avg_val.items():
            print(f'{k}:{v}', end=' ')

        # Write the results to an xml file
        dicts_to_write_in_xml.append(dicts_min_val)
        dicts_to_write_in_xml.append(dicts_max_val)
        dicts_to_write_in_xml.append(dicts_avg_val)
        
        dct = {i:d for i,d in enumerate(dicts_to_write_in_xml)}
        xml = dict_to_xml(dct)
        xml_file.write(str(xml))


    # Output from the json file result.json
    print('\n\nValues from the json file')
    with open(json_fpath,'r') as json_file2:
        data = json.load(json_file2)
        for i in data:
            print(i, end=',')


    # Print the minimum value for all hostnames
    # Use the dictionary dicts_min_val that contains
    print('\n\nMinimum value for all hostnames')
    for k,v in dicts_min_val.items():
        first_key = list(dicts_min_val.keys())[0]
        minimum = dicts_min_val.get(first_key)
        if minimum >= v:
            minimum = v
    print(minimum)


    # Print the maximum value for all hostnames
    # Use the dictionary dicts_max_val that contains
    print('\nMaximum value for all hostnames')
    for k,v in dicts_max_val.items():
        first_key = list(dicts_max_val.keys())[0]
        maximum = dicts_max_val.get(first_key)
        if maximum <= v:
            maximum = v
    print(maximum)


    # Print the average value for all hostnames
    # the average value for each unique host
    print('\nAverage value for all hostnames')
    sum_of_vals = 0
    count_vals = 0
    for i in list_of_dicts:
        for k,v in i.items():
            count_vals += 1
            sum_of_vals += int(v.split('#')[-1].split(' ')[-1].strip('h'))
    average = sum_of_vals//count_vals
    print(average)


    # Export results to pipe delimited flat.txt file
    with open(json_fpath,'r') as json_file:
        data = json.load(json_file)
        for line in data:
            column_names = []
            for k in line.keys():
                if k not in column_names:
                    column_names.append(k)

    with open(txt_fpath,'w') as txt_file:
        cols = ''
        for col in column_names:
            cols += col + '|'
        txt_file.write(f'{cols[:-1]}\n')
        
        for line in data:
            string1 = ''
            for k in line:
                string1 += str(line[k]) + '|'
            txt_file.write(f'{string1[:-1]}\n')
            



    


