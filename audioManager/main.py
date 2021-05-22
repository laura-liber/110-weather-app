""" 
Audio Manager:
    Console application that allow the user to register his/her audio collection
Author:
    Laura Liber

Functionality:
    1 - Register Album
    2 - Register Song
    3 - Display Catalog    
"""

# imports
from os import write
from display import print_menu, clear_screen, print_header
from album import Album
from song import Song
import pickle

# global vars
catalog = []

#functions

def serialize_data():
    try:
        writer = open("sngManager.data", "wb") # wb= write binary
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data saved!")

    except:
        print("** Error saving data")


def deserialize_data():
    try:
        reader = open("sngManager.data", "rb") #rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for item in temp_list:
            catalog.append(item)

        print(f"** Loaded {len(catalog)} albums ")

    except:
        print("** Error loading data")




def register_album():
    print_header("Register Album")

    title = input("Provide the Title: ")
    genre = input("Provide the Genre: ")
    artist = input("Provide the Artist Name: ")
    price = float(input("Provide the Price: "))
    year = int(input("Provide the Release Year: "))

    id = 1
    if(len(catalog) > 0):
        last = catalog[-1]
        id = last.id + 1


    album = Album(id, title, genre, artist, price, year)
    catalog.append(album)

    print(album)


def print_catalog():
    print_header("Your Catalog")

    for album in catalog:
        print(album)


def register_song():
    print_catalog()

    id = int(input("Please select an Album id"))

    found = False
    for album in catalog:
        if(album.id == id):
            found = True
            print_header(f"Add song to album: {album.title}")
            title = input("Provide the Title: ")
            length = int(input("Provide the Length in secs"))
            writer = input("Provide the name of the writer: ")

            id = 1
            if(len(album.songs) > 0):
                id = album.songs[-1].id + 1

            song = Song(id, title, length, writer)
            album.songs.append(song)

    if not found:
        print("Error: Wrong album id, try again!")


def print_songs():
    print_catalog()

    id = int(input("Please select an Album id"))

    found = False
    for album in catalog:
        if(album.id == id):
            found = True
            print_header(f"Songs inside album: {album.title}")
            for song in album.songs:
                print(f"{song.id} | {song.title}")


    if not found:
        print("Error: Wrong album id, try again!")

def count_song():
    print_header("Tota' songs in the system")

    num = 0
    for albums in catalog:
        num += len(albums.songs)

    num2 = len([al.songs for al in catalog])

    print(f"You have: {num}")
    print(f"You have: {num2}")

def total_money():
    print_header("Total $ of the catalog")

    total = 0 
    for album in catalog:
        total += album.price

    print(f"The total is ${total}")

# instructions

# read data
deserialize_data()

opc = ""
while(opc != "q"):
    clear_screen()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == "1"):
        register_album()
        serialize_data()

    if(opc == "2"):
        register_song()
        serialize_data()


    elif(opc == "3"):
        print_catalog()

    elif(opc == "4"):
        print_songs()

    elif(opc == "5"):
        count_song()

    elif(opc == "6"):
        total_money()

    input("Press Enter to continue...")

print("Good byte!")


"""

1 - display the list of albums
2 - ask the user to pick an album
3 - if the album exists:
    a - print the songs inside
  
4 - if not, show an error

 """

 # test 2
 #[album.songs.append(song) for album in catalog if album.id == id]