I read the problem multiple times to really know the format of the csv file which was the original source of all the processes. Since the instruction said that each unique entry is stored in each column, I put every unique HOST in every column.

I created a module utils.py to handle the following processes:
	1. read_csv function - accepts a csv file and returns a list of dictionaries that will be used for the succeeding processes. I used the strip() function to get rid of the characterss or spaces found in the csv file. I used split() function to split group of characters/words; this function returns a list. These 2 functions were used several times in all of the python scripts.

	2.get_min_value function returns the minimum value of each unique hostnames. Since I only saw one value with a number, the  metric, I thought that I had to extract the number from value.

	3. get_max_value function returns the maximum value of each unique hostnames. Just like getting the minimum value, I extracted the number from the  metric, and compare the extracted values of each unique hostname.

	4. get_avg_value function returns a dictionary that contains the average value of each unique hostnames. 

	5. dict_to_xml function converts dictionaries to XML, checking for nested key/value pairs if there are any.

The main script calls all the functions mentioned above. "with open" was used several times in the code, to open and close the file instead of open() and close() functions. Using "with open" will automatically close the file once the blocked is completed.

I imported the built-in module json with the dumps() function to convert the python object into json formatted string. Then used the converted string as an input to the write() function which will write the string to the json file.

Notes/Instructions:
The input file is located on the root folder

Using python 3.11, run the main.py
>>> python main.py

All generated files should go to the main folder

