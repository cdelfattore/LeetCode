import requests
import re

def urlDecode(url):
    response = requests.get(url);
    if response.status_code == 200:
        rows = re.findall('<tr class="[A-z0-9]*">(.*?)</tr>', response.text)
        del rows[0] # we don't need the table headers
        locations = {}
        for columns in rows:
            col_array = re.findall('<span class="[0-9A-z]*">(.*?)</span>', columns)
            locations[(int(col_array[0]), int(col_array[2]))] = col_array[1]
        x_max, y_max = max(locations.keys())

        result = []
        for y in range(y_max, -1, -1):
            row = []
            for x in range(x_max, -1, -1):
                value = locations.get((x, y))
                if value != None:
                    row.insert(0, value)
                else:
                    row.insert(0, ' ')
            result.append(row)

        for s in result:
            print(''.join(s))
            
urlDecode("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")

# Program has three parts, retrieving the information from the HTML page, processing and storing the result from the HTML into a data structure that can then be processed further and then printing the results to the console. Easiest way to parse information from an HTML page is to use regular expressions. I used the HTTP module/package to retrieve the HTML page contents. I then captured the rows in the html table using the "re" (regular expression) module and the regular expression to retrieve all the table rows in the HTML, the <tr> tags contained all of this information. The findall method put each separate row into a list called rows. Then for each row I stored the information in a dictionary called locations, with the key being the coordinates (tuple) and the value being the character at that coordinate. With the dictionary (locations), I then used a double (nested) for loop to iterate over the dictionary keys, starting at the top of the message (greatest y coordinate values) and the right most characters in the message (greatest x coordinates values) and stored these values in an array called result. I then printed line by line the result array and got the message BOECWXH.