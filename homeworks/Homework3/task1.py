__author__ = 'Alex'
from task0 import Song
from task0 import import_songs


def max_number(artist):
    dict = {}
    for i in artist:
        if artist not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict


my_list = import_songs('1.txt')
artist = []
for i in my_list:
    artist.append(i.artist)
a = max_number(artist)
most_songs = max(a, key=a.get)
print(most_songs)



