import sys

import pygame
import pyganim
import pygame_textinput
from pygame.locals import *

import files_manager
import lvl_manager

from Note import Note

bgMenu = files_manager.loadFile('bgMenu.png')
bgCredits = files_manager.loadFile('bgCredits.png')
bgPause = files_manager.loadFile('bgPause.png')
bgLvlList = files_manager.loadFile('bgLvlList.png')
bgGame = files_manager.loadFile('bgGame1.png')
bgGameUp = files_manager.loadFile('bgGameUp.png')
bgGameOver = files_manager.loadFile('bgGameOver.png')
bgWinNext = files_manager.loadFile('bgWinNext.png')
bgWin = files_manager.loadFile('bgWin.png')
bgTutor1 = files_manager.loadFile('bgTutorial1.png')
bgTutor2 = files_manager.loadFile('bgTutorial2.png')
bgGameEnd = files_manager.loadFile('bgGameEnd.png')
bgSaveF = files_manager.loadFile('bgSaveF.png')
bgSaveT = files_manager.loadFile('bgSaveT.png')
button1 = files_manager.loadFile('button1.png')
button2 = files_manager.loadFile('button2.png')
button3 = files_manager.loadFile('button3.png')
buttonYes = files_manager.loadFile('buttonYes.png')
buttonNo = files_manager.loadFile('buttonNo.png')
buttonLvL_1 = files_manager.loadFile('lvl1.png')
buttonLvL_2 = files_manager.loadFile('lvl2.png')
buttonLvL_3 = files_manager.loadFile('lvl3.png')
buttonBack = files_manager.loadFile('back.png')
buttonLvL_2X = files_manager.loadFile('lvl2block.png')
buttonLvL_3X = files_manager.loadFile('lvl3block.png')
note = files_manager.loadFile('note.png')
panel = files_manager.loadFile('click.png')
panelTap = files_manager.loadFile('click2.png')

AnimFirstPath = files_manager.getFilePath('G01.png')
AnimSecondPath = files_manager.getFilePath('G03.png')
Anim = pyganim.PygAnimation([(AnimFirstPath, 460), (AnimSecondPath, 460)])
Anim.play()
clickTap = pyganim.PygAnimation([(panelTap, 460)])
clickTap.play()

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

save = open(files_manager.getFilePath('save.txt'))
lvl1 = open(files_manager.getFilePath('lvl1.txt'))
lvl2 = open(files_manager.getFilePath('lvl2.txt'))
lvl3 = open(files_manager.getFilePath('lvl3.txt'))

FLAG_LVL2 = False
FLAG_LVL3 = False
FLAG_WIN = False
FLAG_ACC = False
FLAG_START = False

mainClock = pygame.time.Clock()

pygame.init()
textinput = pygame_textinput.TextInput()
pygame.display.set_caption('Gandalf Dance!')
screen = pygame.display.set_mode((500, 700),0,32)
fontPath = files_manager.getFilePath('pixel.ttf')
font = pygame.font.Font(fontPath,50)
fontName = pygame.font.Font(fontPath,70)
fontScore = pygame.font.Font(fontPath, 120)
    
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False

def playMainMusic():
    musicPath = files_manager.getFilePath('Epic Sax Guy - 8-bit Remix.mp3')
    pygame.mixer.music.load(musicPath)
    pygame.mixer.music.play(loops=-1)

def playLosingMusic():
    gameOverMusicPath = files_manager.getFilePath('Game Over.mp3')
    pygame.mixer.music.load(gameOverMusicPath)
    pygame.mixer.music.play()

def playWinMusic():
    winMusicPath = files_manager.getFilePath('HeatleyBros - 8 Bit Win.mp3')
    pygame.mixer.music.load(winMusicPath)
    pygame.mixer.music.play(loops=-1)

def main_menu():
    playMainMusic()
    
    global FLAG_START
    
    while True:  
        screen.blit(bgMenu, (0, 0))
        
        draw_text(None, font, (255, 255, 255), screen, 20, 20)
 
        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_play = pygame.Rect(227, 382, 246, 77)
        button_credits = pygame.Rect(227, 482, 246, 76)
        button_exit = pygame.Rect(227, 582, 246, 76)

        screen.blit(button1, (225,380))
        screen.blit(button2, (225,480))
        screen.blit(button3, (225,580))

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_play.collidepoint((mouse_x, mouse_y)):
            if click:
                if FLAG_START == False:
                    page_createAccount()
                if FLAG_START == True:
                    page_lvlList()
        if button_credits.collidepoint((mouse_x, mouse_y)):
            if click:
                page_credits()
        if button_exit.collidepoint((mouse_x, mouse_y)):
            if click:
                running = False
                pygame.quit()
                sys.exit()
                    
        pygame.display.update()
        mainClock.tick(60)

def page_createAccount():
    running = True
    
    global FLAG_LVL2
    global FLAG_LVL3
    global FLAG_START
    
    while running:
        savePath = files_manager.getFilePath('save.txt')
        with open(savePath, "r") as file:
            name = file.read().splitlines()
            str1 = name[0]
            if str1 == "NULLisTrueNull":
                account = False
            else:
                account = True
                str2 = name[1]
                str3 = name[2]
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_Back = pygame.Rect(46, 660, 75, 30)
        button_Next = pygame.Rect(391, 660, 75, 30)    
        if account == False:
            screen.blit(bgSaveF,(0,0))      
            draw_text('Input your name:', font, (255, 255, 255), screen, 125, 210)
            events = pygame.event.get()
            for event in events:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True    
            textinput.update(events)
            draw_text(textinput.get_text(), font, (0, 0, 0), screen, 125, 295)

            if button_Next.collidepoint((mouse_x, mouse_y)):
                if click:
                    if len(textinput.get_text())>=1:
                        savePath = files_manager.getFilePath('save.txt')
                        with open(savePath, "w") as file:
                            file.write(textinput.get_text())
                            file.write('\nFalse')
                            file.write('\nFalse')
                        FLAG_START = True
                        running = False
                        page_lvlList()
            
        if account == True:
            screen.blit(bgSaveT,(0,0))
            draw_text(("Hello, " + str1 + '!'), font, (255, 255, 255), screen, 80, 240)
            if str2 == "True":
                FLAG_LVL2 = True
                draw_text('Level 2 is unlocked!', font, (255, 255, 255), screen, 125, 310)
            else:
                draw_text('Level 2 is locked.', font, (255, 255, 255), screen, 125, 310)
            if str3 == "True":
                FLAG_LVL3 = True
                draw_text('Level 3 is unlocked!', font, (255, 255, 255), screen, 125, 340)
            else:
                draw_text('Level 3 is locked.', font, (255, 255, 255), screen, 125, 340)
            if button_Next.collidepoint((mouse_x, mouse_y)):
                if click:
                    FLAG_START = True
                    running = False
                    page_lvlList()

        click = False
        events = pygame.event.get()
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True    
        
        if button_Back.collidepoint((mouse_x, mouse_y)):
            if click:
                running = False
            
        pygame.display.update()
        mainClock.tick(60)


def page_lvlList():
    running = True
    
    while running:
        screen.blit(bgLvlList, (0,0))
        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_LvL1 = pygame.Rect(172, 302, 161, 65)
        button_LvL2 = pygame.Rect(172, 382, 161, 65)
        button_LvL3 = pygame.Rect(172, 462, 161, 65)
        button_Back = pygame.Rect(172, 542, 161, 65)

        screen.blit(buttonLvL_1, (170,300))
        screen.blit(buttonBack, (170,540))

        if FLAG_LVL2 == False:
            screen.blit(buttonLvL_2X, (170,380))
        elif FLAG_LVL2 == True:
            screen.blit(buttonLvL_2, (170,380))
        if FLAG_LVL3 == False:
            screen.blit(buttonLvL_3X, (170,460))
        elif FLAG_LVL3 == True:
            screen.blit(buttonLvL_3, (170,460))

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        if click:
            if button_LvL1.collidepoint((mouse_x, mouse_y)):
                tutorial()
                running = False
            elif button_LvL2.collidepoint((mouse_x, mouse_y)):
                if FLAG_LVL2 == True:
                    startGame(lvl2)
                    running = False
            elif button_LvL3.collidepoint((mouse_x, mouse_y)):
                if FLAG_LVL3 == True:
                    startGame(lvl3)
                    running = False
            elif button_Back.collidepoint((mouse_x, mouse_y)):
                running = False
            else:
                click = False

        pygame.display.update()
        mainClock.tick(60)    


def tutorial():
    running = True
    click = False
    FLAG_SCREEN = 1
    while running:
        if FLAG_SCREEN == 1:
            screen.blit(bgTutor1, (0,0))
        else:
            screen.blit(bgTutor2, (0,0))
        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_Menu = pygame.Rect(46, 660, 75, 30)
        button_tutorPageFirst = pygame.Rect(161, 660, 75, 30)
        button_tutorPageSecond = pygame.Rect(276, 660, 75, 30)
        button_startGame = pygame.Rect(391, 660, 75, 30)

        if click:
            if button_Menu.collidepoint((mouse_x, mouse_y)):
                running = False
            elif button_tutorPageFirst.collidepoint((mouse_x, mouse_y)):
                FLAG_SCREEN = 1
            elif button_tutorPageSecond.collidepoint((mouse_x, mouse_y)):
                FLAG_SCREEN = 2
            elif button_startGame.collidepoint((mouse_x, mouse_y)):
                running = False
                startGame(lvl1)
            else:
                click = False
                
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)    

def createNotesGrid(notes, notesSpeed):
    global platforms, entities, Y

    for row in notes:
        colInd = 0
        for col in row:
            colInd += 1
            if col == '1':
                if colInd == 1:
                    pf = Note(55, Y, notesSpeed)
                    platforms.append(pf)
                    entities.add(pf)
                if colInd == 2:
                    pf = Note(155, Y, notesSpeed)
                    platforms.append(pf)
                    entities.add(pf)
                if colInd == 3:
                    pf = Note(255, Y, notesSpeed)
                    platforms.append(pf)
                    entities.add(pf)
                if colInd == 4:
                    pf = Note(355, Y, notesSpeed)
                    platforms.append(pf)
                    entities.add(pf)
        if notesSpeed==2:
            Y -= 30
        else:
            Y -= 26

platforms = []
entities = pygame.sprite.Group()
Y = 400

def startGame(lvl):
    running = True
    musicPath = files_manager.getFilePath('music.mp3')
    pygame.mixer.music.load(musicPath)
    pygame.mixer.music.play()

    panelA = pygame.Rect(55, 602, 57, 58)
    panelW = pygame.Rect(155, 602, 57, 58)
    panelK = pygame.Rect(255, 602, 57, 58)
    panelL = pygame.Rect(355, 602, 57, 58)

    global entities
    entities = pygame.sprite.Group()

    global platforms
    platforms = []
    
    global Y
    Y = 400
    
    NOTES = []
    NOTES_SPEED = 0

    if lvl == lvl1:
        NOTES = lvl_manager.loadNotes('lvl1.txt')
        NOTES_SPEED = 2
    elif lvl == lvl2:
        NOTES = lvl_manager.loadNotes('lvl2.txt')
        NOTES_SPEED = 3
    elif lvl == lvl3:
        NOTES = lvl_manager.loadNotes('lvl3.txt')
        NOTES_SPEED = 4

    createNotesGrid(NOTES, NOTES_SPEED)
    
    points = 0 
    badFlag = 0
    HP = 7
    while running:        
        start_ticks=0
        Click = False
        breakFlag = False
        mainClock.tick(60)
        
        screen.blit(bgGame, (0, 0))        
        
        for event in pygame.event.get():
            if event.type == MUSIC_END:
                pygame.mixer.music.stop()
                win(lvl, points, badFlag)
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.music.pause()
                    result = pause()
                    if result == True:
                        pygame.mixer.music.unpause()
                    else:
                        main_menu()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    isNoteClick = lvl_manager.checkKeyTap(platforms, panelA)
                    points, HP, badFlag = lvl_manager.updateLvlInfo(isNoteClick, points, HP, badFlag)
                    clickTap.blit(screen, (55,602))
                        
                if event.key == K_s:
                    isNoteClick = lvl_manager.checkKeyTap(platforms, panelW)
                    points, HP, badFlag = lvl_manager.updateLvlInfo(isNoteClick, points, HP, badFlag)
                    clickTap.blit(screen, (155,602))
                        
                if event.key == K_k:
                    isNoteClick = lvl_manager.checkKeyTap(platforms, panelK)
                    points, HP, badFlag = lvl_manager.updateLvlInfo(isNoteClick, points, HP, badFlag)
                    clickTap.blit(screen, (255,602))

                if event.key == K_l:
                    isNoteClick = lvl_manager.checkKeyTap(platforms, panelL)
                    points, HP, badFlag = lvl_manager.updateLvlInfo(isNoteClick, points, HP, badFlag)
                    clickTap.blit(screen, (355,602))

        for note in platforms:
            if note.rect.bottom >= 730:
                points, HP, badFlag = lvl_manager.updateLvlInfo(False, points, HP, badFlag)
                platforms.remove(note)

        if badFlag >= 7:
            pygame.mixer.music.stop()
            gameOver()
            running = False
                
        screen.blit(panel, (55,602))
        screen.blit(panel, (155,602))
        screen.blit(panel, (255,602))
        screen.blit(panel, (355,602))

        for e in platforms:
            screen.blit(e.image, e.rect)
            e.update(Click)
        screen.blit(bgGameUp, (0, 0))
        
        if lvl == lvl1:
            drawLvlInfo('lvl1', points, HP)
        elif lvl == lvl2:
            drawLvlInfo('lvl2', points, HP)
        elif lvl == lvl3:
            drawLvlInfo('lvl3', points, HP)
        
        Anim.blit(screen, (20,20))

        pygame.display.update()
        pygame.display.flip()

def drawLvlInfo(lvlName, points, HP):
    draw_text(lvlName, font, (255, 255, 255), screen, 25, 20)
    draw_text(str(points), font, (255, 255, 255), screen, 25, 60)
    draw_text('HP', font, (255, 255, 255), screen, 25, 100)
    draw_text(str(HP), font, (255, 255, 255), screen, 65, 100)

def page_credits():
    running = True
    click = False
    
    while running:
        screen.blit(bgCredits,(0,0))
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        button_Back = pygame.Rect(172, 552, 161, 65)
        screen.blit(buttonBack, (170,550))

        if click:
            if button_Back.collidepoint((mouse_x, mouse_y)):
                running = False
            else:
                click = False

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)

def gameOver():
    running = True
    playLosingMusic()

    click = False
    while running:
        screen.blit(bgGameOver, (0,0))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_Back = pygame.Rect(172, 552, 161, 65)
        screen.blit(buttonBack, (170,550))

        if click:
            if button_Back.collidepoint((mouse_x, mouse_y)):
                running = False
                page_lvlList()
                playMainMusic()
            else:
                click = False

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    page_lvlList()
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def win(lvl, point, miss):
    running = True
    playWinMusic()

    global FLAG_LVL2
    global FLAG_LVL3
    global FLAG_WIN
    click = False
    while running:

        if lvl == lvl1:
            if FLAG_LVL2 == False:
                screen.blit(bgWinNext, (0,0))
            else:
                screen.blit(bgWin, (0,0))
        if lvl == lvl2:
            if FLAG_LVL3 == False:
                screen.blit(bgWinNext, (0,0))
            else:
                screen.blit(bgWin, (0,0))
        if lvl == lvl3:
            if FLAG_WIN == False:
                screen.blit(bgGameEnd,(0,0))
            else:
                screen.blit(bgWin, (0,0))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if lvl == lvl3 and FLAG_WIN == False:
            button_Back = pygame.Rect(172, 572, 161, 65)
            screen.blit(buttonBack, (170,570))
            draw_text(str(point), fontScore, (255, 255, 255), screen, 270, 369)
            draw_text(str(miss), fontScore, (255,255,255), screen, 340, 449)
        else:
            button_Back = pygame.Rect(172, 552, 161, 65)
            screen.blit(buttonBack, (170,550))
            draw_text(str(point), fontScore, (255, 255, 255), screen, 270, 298)
            draw_text(str(miss), fontScore, (255,255,255), screen, 340, 400)

        if click:
            if button_Back.collidepoint((mouse_x, mouse_y)):
                if lvl == lvl1:
                    FLAG_LVL2 = True
                    savePath = files_manager.getFilePath('save.txt')
                    with open(savePath, "r") as file:
                        name = file.read().splitlines()
                    with open(savePath, "w") as file:
                        file.write(name[0])
                        file.write('\nTrue')
                        file.write('\n')
                        file.write(name[2])
                if lvl == lvl2:
                    FLAG_LVL3 = True
                    savePath = files_manager.getFilePath('save.txt')
                    with open(savePath, "r") as file:
                        name = file.read().splitlines()
                    with open(savePath, "w") as file:
                        file.write(name[0])
                        file.write('\n')
                        file.write(name[1])
                        file.write('\nTrue')
                if lvl == lvl3:
                    FLAG_WIN = True
                
                running = False
                page_lvlList()
                playMainMusic()
            else:
                click = False

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)

def pause():
    running = True
    click = False

    while running:
        screen.blit(bgPause, (0, 0))
        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_Yes = pygame.Rect(172, 482, 161, 65)
        button_No = pygame.Rect(172, 577, 161, 65)
        
        if button_Yes.collidepoint((mouse_x, mouse_y)):
            if click:
                running = False
                return False
        if button_No.collidepoint((mouse_x, mouse_y)):
            if click:
                running = False
                return True
    
        screen.blit(buttonYes, (170,480))
        screen.blit(buttonNo, (170,575))
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()
