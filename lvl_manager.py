import files_manager

from pygame import mixer

def loadNotes(lvlFileName):
    lvlPath = files_manager.getFilePath(lvlFileName)
    with open(lvlPath, 'r') as file:
        notes = file.read().splitlines()
    return notes

def checkKeyTap(platforms, panelKey):
    isNoteClick = False
    for note in platforms:
        if panelKey.colliderect(note) == True:
            isNoteClick = True
            platforms.remove(note)
    return isNoteClick

def updateLvlInfo(isNoteClick, points, HP, badFlag):
    if isNoteClick == True:
        points += 10
    elif isNoteClick == False:
        soundPath = files_manager.getFilePath('sound.wav')
        sound = mixer.Sound(soundPath)
        mixer.Channel(0).play(sound, maxtime=200)
        badFlag += 1
        HP -= 1
    return points, HP, badFlag