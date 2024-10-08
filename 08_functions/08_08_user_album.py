def make_album(name, title, number=None):
    album = {'artist name': name, 'album title': title}
    if number:
        album['number'] = number
    return album

while True:
    print("\nPlease tell me your artist name and album:")
    f_name = input("Artist: ")
    f_title = input("Title: ")
    finished_album = make_album(f_name, f_title)
    print(f"\n{finished_album}")
    go_again = input("\ntype 'quit' to exit, otherwise type 'g' to go again: ")
    if go_again == 'quit':
        break