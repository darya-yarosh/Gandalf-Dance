import sys
import os

import pygame

def loadFile(filename):
    filePath = getFilePath(filename)
    file = pygame.image.load(filePath)
    return file

def getFilePath(filename):
    FOLDER = 'Files'
    return resource_path(os.path.join(FOLDER, filename))

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)