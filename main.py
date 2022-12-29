import csv
from bs4 import BeautifulSoup
import requests


url = 'https://gist.github.com/samuelcolvin/1743d8919acb465c1fbbcea2c3cdaf3e'

# Get data from GitHub Gist.
data = requests.get(url).text

# Parse it
soup = BeautifulSoup(data, 'html.parser')

# Find the Mastodon handles

def to_text(el):
  return el.get_text()

main_div = soup.find(id="file-python-people-md")
people_raw = main_div.find_all('ul')[0]

print(f"Fetched list of Python people ({len(people_raw)} people in total).")

people = []

for p in people_raw:
  if str(type(p)) == "<class 'bs4.element.Tag'>":
    people.append(p)

def get_mastodon(person):
  lis = person.find_all('li')
  for li in lis:
    if 'Mastodon' in li.decode_contents():
      handle = li.decode_contents().split('rel="nofollow"')[1].split('>')[1].split('</a')[0]
      return handle
  return None

def get_name(person):
  name = person.decode_contents().split('<strong>')[1].split('</strong>')[0]
  return name

mastodon_info = []

for person in people:
  mastodon = get_mastodon(person)
  if mastodon is not None:
    mastodon_info.append({
      "name": get_name(person),
      "mastodon": mastodon
    })

print(f"Filtered out Python people who are not on Mastodon ({len(mastodon_info)} are on Mastodon).")

# Using the Mastodon handles, create a CSV that can be imported.
# CSV modelled after Java Champions CSV at https://javachampions.org/resources/mastodon.csv

file_name = 'python_people_mastodon_import.csv'

print(f"Creating CSV import file at {file_name}.")

with open(file_name, 'w', encoding='UTF8') as f:
  writer = csv.writer(f)
  writer.writerow(['Account address', 'Show boosts', 'Notify on new posts' ,'Languages'])
  for person in mastodon_info:
    writer.writerow([person['mastodon'], 'true', 'false',''])
    print(f"Added {person['name']} ({person['mastodon']}).")

print('Done.')
