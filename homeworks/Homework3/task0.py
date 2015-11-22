__author__ = 'Alex'


class Song:
    def __init__(self, name, artist, album, track_position, release_year, duration):
        self.name = name
        self.artist = artist
        self.album = album
        self.track_position = track_position
        self.release_year = release_year
        self.duration = duration

    def __repr__ (self):
        if int(self.duration) != 0:
            song = 'Song \'%s\' by %s, album \'%s\', track position %s,' \
                   ' release year %s.' % (self.name, self.artist, self.album, self.track_position, self.release_year)
        else:
            song = 'Song \'%s\' by %s, album \'%s\', track position %s,' \
                   ' release year %s, length - %s seconds.' % (self.name, self.artist, self.album, self.track_position,
                                                                                        self.release_year, self.duration)
        return song

    def __lt__ (self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.album < other.album:
            return True
        if self.artist == other.artist and self.album == other.album and self.name < other.name:
            return True
        return False


def import_songs(file_name):
    input = open(file_name, 'r')
    song_strings = input.readlines()
    list = []
    for i in song_strings:
        name, artist, album, track_position, release_year, duration = i.split('\t')
        list.append(Song(name, artist, album, track_position, release_year, duration))
    return list
def export_songs(original_list, destination):
    write_file = open(destination, 'w')
    for self in original_list:
        write_file.write('%s\t%s\t%s\t%s\t%s\t%s'%(self.name, self.artist, self.album, self.track_position,
                                                           self.release_year, self.duration))
def shuffle_songs(songs):
    from random import shuffle
    shuffle(songs)
    return (songs)

test_run1 = import_songs('1.txt')
shuffle_songs(test_run1)
export_songs(test_run1, '2.txt')


