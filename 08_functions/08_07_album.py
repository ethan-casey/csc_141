def make_album(name, title, number=None):
    album = {'artist name': name, 'album title': title}
    if number:
        album['number'] = number
    return album

music = make_album('jimi hendrix', 'vodoo child')
music_two = make_album('big time rush', 'elevate', 12)
music_three = make_album('amamiya sora', 'various BLUE')
print(music)
print(music_two)
print(music_three)

#instead of making a new value for the second part of this, I just changed
#music_two so it shows that it's working