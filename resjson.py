# OOPS concept is used
# Working with JSON
import requests


class DataJson:

    # URL is gained in the constructor
    def __init__(self, web_url):
        self.url = web_url

    # Below method fetch's the json data
    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    # Below method fetch's the total json data
    def count_json(self):
        count = 0
        for data in self.fetch_data():
            count += 1
        return count

    # Below method fetch's the name of countries, currency name and symbol
    def fetch_name(self):
        try:
            print("List of data: ")
            for data in self.fetch_data():
                if data['name']['official'] == 'Antarctica' or data['name']['official'] == 'Bouvet Island' or data['name']['official'] == 'Heard Island and McDonald Islands':
                    continue
                print(data['name']['official'])
                for key, value in data['currencies'].items():
                    if value['name'] == 'Bosnia and Herzegovina convertible mark' or value['name'] == 'Sudanese pound':
                        continue
                    print(value['name'], value['symbol'], sep='\n')
        except Exception as e:
            print(e)

    # Below method fetch's the countries name with dollar currency
    def fetch_dollar(self):
        list1 = []
        print("Country with currency dollar:- ")
        print()
        for data1 in self.fetch_data():
            currency_keys = list(data1.get('currencies', {}).keys())
            if currency_keys == ["USD"]:
                list1.append(data1['name']['common'])
        return list1

    # Below method fetch's the countries name with euro currency
    def fetch_euro(self):
        list2 = []
        print("Country with currency euro:- ")
        print()
        for data2 in self.fetch_data():
            currency_keys = list(data2.get('currencies', {}).keys())
            if currency_keys == ["EUR"]:
                list2.append(data2["name"]["common"])
        return list2


url = "https://restcountries.com/v3.1/all"

# create object for the class
s = DataJson(url)
# calling the method using the created object
print(s.fetch_data())
print(s.fetch_name())
fd = s.fetch_dollar()
print(*fd, sep='\n')
fe = s.fetch_euro()
print(*fe, sep='\n')
# print(s.count_json())

