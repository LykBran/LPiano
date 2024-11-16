import pygame, sys, time
from PySide6.QtGui import QImage, QPainter
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene


def get_key_index(key, kList):
    for i in range(len(kList)):
        if key == ord(kList[i]):
            return i
    return -1


# Piano init
pygame.init()
pianoImg = pygame.image.load("./resources/piano.bmp")
PIANO_WIDTH, PIANO_HEIGHT = pianoImg.get_size()
screen = pygame.display.set_mode(pianoImg.get_size())
pygame.display.set_caption("LPiano")

# Notes init
noteImg = pygame.image.load("./resources/note.bmp")
keyList = "zxcvbnmqwertyuiop"
keyListM = "sdghj2356790"
soundList = [
    pygame.mixer.Sound(f"./resources/{i}{j}.ogg") for j in "345" for i in "cdefgab"
][:-4]
soundListM = [
    pygame.mixer.Sound(f"./resources/{i}{j}m.ogg") for j in "345" for i in "cdfga"
][:-3]
keyFlagList = [0] * (len(keyList) + len(keyListM))


pygame.key.stop_text_input()


class PianoFrame(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFixedSize(PIANO_WIDTH, PIANO_HEIGHT)

        # Recording init
        self.recordTimes = []
        self.record = []
        self.recordFlag = False
        self.recordTime = -1

        self.sound = None
        self.cnt = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_piano)
        self.timer.start(1000 // 100)

    def update_piano(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                i = get_key_index(event.key, keyList)
                im = get_key_index(event.key, keyListM)
                # Press white key
                if i >= 0:
                    if self.sound:
                        self.sound.stop()
                    self.sound = soundList[i]
                    if self.recordFlag:
                        if self.recordTime != -1:
                            self.recordTimes.append(time.time() - self.recordTime)
                        self.recordTime = time.time()
                        self.record.append(self.sound)
                    self.sound.play()
                    keyFlagList[i] = 1
                # Press black key
                if im >= 0:
                    if self.sound:
                        self.sound.stop()
                    self.sound = soundListM[im]
                    if self.recordFlag:
                        if self.recordTime != -1:
                            self.recordTimes.append(time.time() - self.recordTime)
                        self.recordTime = time.time()
                        self.record.append(self.sound)
                    self.sound.play()
                    keyFlagList[im + len(keyList)] = 1
                # Press SPACE to record
                if event.key == pygame.K_SPACE:
                    if self.recordFlag:
                        if self.recordTime != 0:
                            self.recordTimes.append(time.time() - self.recordTime)
                        self.recordFlag = False
                        # print(record)
                        # print(recordTimes)
                    else:
                        self.recordFlag = True
                        self.recordTime = -1
                        self.record = []
                        self.recordTimes = []
                # Press K to play the record
                if event.key == pygame.K_k and not self.recordFlag and self.record:
                    lst = None
                    for ks, t in zip(self.record, self.recordTimes):
                        if lst:
                            lst.stop()
                        lst = ks
                        ks.play()
                        time.sleep(t)
                    pygame.event.clear()
            elif event.type == pygame.KEYUP:
                i = get_key_index(event.key, keyList)
                im = get_key_index(event.key, keyListM)
                # Release white key
                if i >= 0:
                    keyFlagList[i] = 0
                # Release black key
                if im >= 0:
                    keyFlagList[im + len(keyList)] = 0

        screen.blit(pianoImg, (0, 0))
        for i in range(len(keyList)):
            if keyFlagList[i]:
                screen.blit(noteImg, (i * 30 + 2, 80))
        for i in range(len(keyListM)):
            if keyFlagList[i + len(keyList)]:
                if i in range(2, 5):
                    i += 1
                elif i in range(5, 7):
                    i += 2
                elif i in range(7, 10):
                    i += 3
                elif i in range(10, 13):
                    i += 4
                screen.blit(noteImg, (i * 30 + 17, 80))
        if self.recordFlag:
            self.cnt += 1
            if self.cnt % 40 < 20:
                pygame.draw.circle(screen, (255, 0, 0), (10, 10), 5)
        pygame.display.flip()


# Main body
"""while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            i = get_key_index(event.key, keyList)
            im = get_key_index(event.key, keyListM)
            # Press white key
            if i >= 0:
                if sound:
                    sound.stop()
                sound = soundList[i]
                if recordFlag:
                    if recordTime != -1:
                        recordTimes.append(time.time() - recordTime)
                    recordTime = time.time()
                    record.append(sound)
                sound.play()
                keyFlagList[i] = 1
            # Press black key
            if im >= 0:
                if sound:
                    sound.stop()
                sound = soundListM[im]
                if recordFlag:
                    if recordTime != -1:
                        recordTimes.append(time.time() - recordTime)
                    recordTime = time.time()
                    record.append(sound)
                sound.play()
                keyFlagList[im + len(keyList)] = 1
            # Press SPACE to record
            if event.key == pygame.K_SPACE:
                if recordFlag:
                    if recordTime != 0:
                        recordTimes.append(time.time() - recordTime)
                    recordFlag = False
                    # print(record)
                    # print(recordTimes)
                else:
                    recordFlag = True
                    recordTime = -1
                    record = []
                    recordTimes = []
            # Press K to play the record
            if event.key == pygame.K_k and not recordFlag and record:
                lst = None
                for ks, t in zip(record, recordTimes):
                    if lst:
                        lst.stop()
                    lst = ks
                    ks.play()
                    time.sleep(t)
        elif event.type == pygame.KEYUP:
            i = get_key_index(event.key, keyList)
            im = get_key_index(event.key, keyListM)
            # Release white key
            if i >= 0:
                keyFlagList[i] = 0
            # Release black key
            if im >= 0:
                keyFlagList[im + len(keyList)] = 0

    screen.blit(pianoImg, (0, 0))
    for i in range(len(keyList)):
        if keyFlagList[i]:
            screen.blit(noteImg, (i * 30 + 2, 80))
    for i in range(len(keyListM)):
        if keyFlagList[i + len(keyList)]:
            if i in range(2, 5):
                i += 1
            elif i in range(5, 7):
                i += 2
            elif i in range(7, 10):
                i += 3
            elif i in range(10, 13):
                i += 4
            screen.blit(noteImg, (i * 30 + 17, 80))
    if recordFlag:
        cnt += 1
        if cnt % 40 < 20:
            pygame.draw.circle(screen, (255, 0, 0), (10, 10), 5)
    clock.tick(100)
    pygame.display.update()"""

if __name__ == "__main__":
    app = QApplication(sys.argv)

    piano = PianoFrame()
    # piano.show()

    sys.exit(app.exec())
