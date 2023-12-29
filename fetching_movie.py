from bs4 import BeautifulSoup
import requests

year = input("Enter the year you want to listen songs of in YYYY-MM-DD format")
# print(year)
response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}").text

soup = BeautifulSoup(response, 'html.parser')
# print(soup)
songs_name = soup.select(selector="div main div div div div div div div ul li h3")
# print(songs_name)

# List that will hol all the songs name
songs_list = []
for song in songs_name:
    songName = BeautifulSoup(song.text, 'html.parser')
    single_song_name = songName.getText()
    song_name_without_whitespaces = ''.join(single_song_name.split())
    # print(song_name_without_whitespaces)
    # print(type(sn))
    songs_list.append(song_name_without_whitespaces)

print(songs_list)
# print("hi")