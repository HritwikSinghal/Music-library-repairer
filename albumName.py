from tools import *


def modifyAlbum(tags):
    print("Curr Album Name: ", tags['album'][0])

    oldAlbumName = tags['album'][0]
    newName = removeYear(oldAlbumName)
    newName = removeGibberish(newName)

    newAlbumName = newName + ' (' + tags['date'][0] + ')'

    if oldAlbumName != newAlbumName:
        tags['album'] = newAlbumName
        tags.save()
        print("New Album Name : ", newAlbumName)


def start(tags):
    modifyAlbum(tags)
