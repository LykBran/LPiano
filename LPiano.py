import pygame, sys, time


def get_key_index(key, kList):
    for i in range(len(kList)):
        if key == ord(kList[i]):
            return i
    return -1


# Piano init
pygame.init()
pianoImg = pygame.image.load("./resources/piano.bmp")
screen = pygame.display.set_mode(pianoImg.get_size())
clock = pygame.time.Clock()
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

# Recording init
recordFlag = False
recordTimes = []
recordTime = -1
record = []

# Main body
pygame.key.stop_text_input()
cnt = 0
sound = None
while True:
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
    pygame.display.update()
