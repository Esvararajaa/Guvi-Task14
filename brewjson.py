import requests


class Brew:

    # Constructor
    def __init__(self, web_url, state):
        self.url = web_url
        self.s = state

    # Method to read the json data
    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    # Method to fetch all brew details
    def brew_details(self, state):
        cnt1 = 1
        self.s = state
        print()
        print(f"Name of all breweries present in {self.s}:")
        print()
        for data in self.fetch_data():
            # print(data['name'])
            # print(data['state_province'])
            if str(data['state']) == self.s:
                print(f"{cnt1}. {data['name']}")
                cnt1 = cnt1 + 1
        print()
        print(f"Number of Breweries: {cnt1-1}")

    # Method to fetch Brew types
    def brew_type(self, state):
        self.s = state
        list1 = []
        res1 = {}
        for data in self.fetch_data():
            list1.append(data['brewery_type'])
            for i in list1:
                res1[i] = list1.count(i)
        print()
        print("Total number of type of brews in the individual cities:")
        print()
        print(*[str(k) + ' = ' + str(v) for k, v in res1.items()], sep='\n')

    # Method to fetch the brew with website
    def brew_webCount(self, state):
        self.s = state
        count2 = 1
        print()
        print(f"List of websites in the {self.s} for breweries")
        print()
        for data in self.fetch_data():
            if data['website_url']:
                print(f"{count2}.{data['website_url']}")
                count2 = count2 + 1
        print()
        print(f"Total count of breweries having websites in the {self.s} = {count2 - 1}")


url1 = "https://api.openbrewerydb.org/v1/breweries?by_state=Alaska"
print("Details of state: Alaska")
s = Brew(url1, "Alaska")
s.brew_details("Alaska")
s.brew_type("Alaska")
s.brew_webCount("Alaska")

url2 = "https://api.openbrewerydb.org/v1/breweries?by_state=Maine"
print("Details of state: Maine")
b = Brew(url2, "Maine")
b.brew_details("Maine")
b.brew_type("Maine")
b.brew_webCount("Maine")

url3 = "https://api.openbrewerydb.org/v1/breweries?by_state=New%20York"
print("Details of state: New York")
a = Brew(url1, "New York")
a.brew_details("New York")
a.brew_type("New York")
a.brew_webCount("New York")

