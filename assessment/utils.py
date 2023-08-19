def read_csv(fpath):
    '''Accept a file path for a csv file
    and return list of dictionaries
    '''
    with open(fpath, 'r') as file:
        first_row = file.readline()
        list_first_row = first_row.strip('\n').split(',')
        hostnames = []
        for i in list_first_row:
            hostnames.append(i.split('#')[1])
        
        no_of_cols = len(hostnames)
        list_of_dicts = []
        list_of_rows = []
    
    with open(fpath, 'r') as file2:
        data = file2.readlines()
        for rows in data:
            list_of_rows.append(rows.strip('\n').split(','))
        
        for item in list_of_rows:
            row_as_dict = {}
            for i in range(no_of_cols):
                row_as_dict[hostnames[i]] = item[i]
            list_of_dicts.append(row_as_dict)
        
        return list_of_dicts

    
def get_min_value(list_of_ddicts):
    '''Return a dictionary that contains
    the minimum value of each unique hostname'''
    dicts_min_val = {}
    for i in list_of_ddicts:
        
        for k,v in i.items():
            minimum = int(v.split('#')[-1].split(' ')[-1].strip('h'))
            if dicts_min_val.get(k):
                if minimum <= dicts_min_val.get(k):
                    dicts_min_val[k] = minimum
            else:
                dicts_min_val[k] = minimum
    
    return dicts_min_val

    
def get_max_value(list_of_ddicts):
    '''Return a dictionary that contains
    the maximum value of each unique hostname'''
    dicts_max_val = {}
    for i in list_of_ddicts:
        
        for k,v in i.items():
            maximum = int(v.split('#')[-1].split(' ')[-1].strip('h'))
            if dicts_max_val.get(k):
                if maximum >= dicts_max_val.get(k):
                    dicts_max_val[k] = maximum
            else:
                dicts_max_val[k] = maximum
    
    return dicts_max_val


def get_avg_value(list_of_ddicts):
    '''Return a dictionary that contains
    the avg value of each unique hostname'''
    dicts_val = {}
    dicts_avg_val = {}

    for i in list_of_ddicts:
        
        for k,v in i.items():
            value = int(v.split('#')[-1].split(' ')[-1].strip('h'))
            
            if dicts_val.get(k):
                dicts_val[k].append(value)
            else:
                dicts_val[k] = [value]

    for k,v in dicts_val.items():
        dicts_avg_val[k] = sum(v)//len(v)
        
    return dicts_avg_val


def dict_to_xml(dict1):
    '''Converts dictionary to XML'''
    result = ''
    if isinstance(dict1, str) or isinstance(dict1, int):
        return dict1
    elif isinstance(dict1, dict):
        for key in dict1.keys():
            result += '<' + str(key) + '>' + str(dict_to_xml(dict1[key])) + '</' + str(key) + '>'
        return result






