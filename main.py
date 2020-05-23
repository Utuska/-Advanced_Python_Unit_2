from pprint import pprint
import json
import requests

# date = requests.get("https://raw.githubusercontent.com/mledoze/countries/master/countries.json")
#
# initial_file = date.json()
# print(len(d))
# for i in d:
#     print(i['name']['common'])


class Downloader:

    def __init__(self, file_path):
        f = open('index.json', encoding='utf-8')
        initial_file = json.load(f)

        self.file_json = initial_file
        self.leng_file_json = len(initial_file)
        self.new_value = 0
        self.file_output = open(file_path, 'wb')

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.new_value <= self.leng_file_json:
                country = self.file_json[int(self.new_value)]['name']['common']
                if ' ' in country:
                    long = country.split()
                    country = '_'.join(long)
                couple = f'Страна {country} - https://en.wikipedia.org/wiki/{country} \n'
                self.file_output.write(couple.encode())
                self.new_value += 1
        except IndexError:
            raise StopIteration
        return couple



if __name__ == '__main__':
    for m in Downloader('country.txt'):
        print(m)



