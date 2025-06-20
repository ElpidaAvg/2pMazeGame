import pygame
import time
import threading

screenwidth = 1380
screenheight = 960

x1 = 20
y1 = 20

x2 = 1330
y2 = 20

p1_wins = 0
p2_wins = 0
winner = "-"
timer = 0
start_timer = time.time()

best_time = 100000000000000000

w7_w = 200
w10_h = 480
w11_h = 480

def resize_parts():
    global w7_w
    while True:
        for i in range(200):
            w7_w -= 1
            time.sleep(0.01)
        time.sleep(1)
        for i in range(200):
            w7_w += 1
            time.sleep(0.01)
        time.sleep(1)

resize_thread = threading.Thread(target = resize_parts)
resize_thread.daemon =  True
resize_thread.start()

def resize_parts2():
    global w10_h # me to global kanw mia metavliti gnwsti se olo ton kwdika (eite einai o main kwdikas eite def)
    while True: # gia na kinountai oi tyxoi olh thn wra
        for i in range(100):
            w10_h -= 1
            time.sleep(0.01)
        time.sleep(1)
        for i in range(100):
            w10_h += 1
            time.sleep(0.01)
        time.sleep(1)

resize_thread2 = threading.Thread(target = resize_parts2)
resize_thread2.daemon =  True
resize_thread2.start()

def resize_parts3():
    global w11_h # me to global kanw mia metavliti gnwsti se olo ton kwdika (eite einai o main kwdikas eite def)
    while True: # gia na kinountai oi tyxoi olh thn wra
        for i in range(100):
            w11_h -= 1
            time.sleep(0.01)
        time.sleep(1)
        for i in range(100):
            w11_h += 1
            time.sleep(0.01)
        time.sleep(1)

resize_thread3 = threading.Thread(target = resize_parts3)
resize_thread3.daemon =  True
resize_thread3.start()

pygame.init() #init = initialize, arxikopoiw tin vivliothiki
screen = pygame.display.set_mode((screenwidth, screenheight)) # dimiourgw parathyro
running = True # voithitiki metavliti

while running: # forever loop gia na trexei to paixnidi
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # to x panw deksia sto parathyro
            running = False # gia na stamatisw loypa, dhladh na kleisw parathyro
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((43, 207, 240))

    p1 = pygame.draw.rect(screen, (97, 6, 164), pygame.Rect(x1, y1, 30, 30))
    p2 = pygame.draw.rect(screen, (253, 249, 0), pygame.Rect(x2, y2, 30, 30))

    finish = pygame.draw.rect(screen, (44, 245, 87), pygame.Rect(630, 840, 100, 100))

    pressed = pygame.key.get_pressed()

# Player 1:
    if pressed[pygame.K_w]:
        y1 -= 1

    if pressed[pygame.K_s]:
        y1 += 1

    if pressed[pygame.K_a]:
        x1 -= 1

    if pressed[pygame.K_d]:
        x1 += 1

# Player 2:
    if pressed[pygame.K_UP]:
        y2 -= 1

    if pressed[pygame.K_DOWN]:
        y2 += 1

    if pressed[pygame.K_LEFT]:
        x2 -= 1

    if pressed[pygame.K_RIGHT]:
        x2 += 1

# Walls:
    topb = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(0, 0, 1380, 10))
    bottomb = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(0, 950, 1380, 10))
    rightb = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(1370, 0, 10, 1380))
    leftb = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(0, 0, 10, 1380))

    w1 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(120, 0, 20, 700))
    w2 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(1240, 0, 20, 700))
    w3 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(200, 400, 20, 560))
    w4 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(1160, 400, 20, 560))

    w5 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(570, 800, 20, 160))
    w6 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(770, 800, 20, 160))
    w7 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(570, 800, w7_w, 20))

    w8 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(200, 0, 20, 300))
    w9 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(1160, 0, 20, 300))
    w10 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(300, 0, 20, w10_h))
    w11 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(1060, 0, 20, w11_h))
    w12 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(300, 480, 20, 480))
    w13 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(1060, 480, 20, 480))
    w14 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(400, 0, 20, 100))
    w15 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(400, 200, 20, 760))
    w16 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(960, 0, 20, 100))
    w17 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(960, 200, 20, 760))
    w18 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(500, 0, 20, 700))
    w19 = pygame.draw.rect(screen, (217, 18, 18), pygame.Rect(860, 0, 20, 700))

# Walls Collision:
    if p1.colliderect(topb) or p1.colliderect(bottomb) or p1.colliderect(rightb) or p1.colliderect(leftb) or p1.colliderect(w1) or p1.colliderect(w2) or p1.colliderect(w3) or p1.colliderect(w4) or p1.colliderect(w5) or p1.colliderect(w6)or p1.colliderect(w7) or p1.colliderect(w8) or p1.colliderect(w9) or p1.colliderect(w10) or p1.colliderect(w11) or p1.colliderect(w12) or p1.colliderect(w13) or p1.colliderect(w14) or p1.colliderect(w15) or p1.colliderect(w16) or p1.colliderect(w17) or p1.colliderect(w18) or p1.colliderect(w19):
        if pressed[pygame.K_w]:
            y1 += 3

        if pressed[pygame.K_s]:
            y1 -= 3

        if pressed[pygame.K_a]:
            x1 += 3

        if pressed[pygame.K_d]:
            x1 -= 3

    if p2.colliderect(topb) or p2.colliderect(bottomb) or p2.colliderect(rightb) or p2.colliderect(leftb) or p2.colliderect(w1) or p2.colliderect(w2) or p2.colliderect(w3) or p2.colliderect(w4) or p2.colliderect(w5) or p2.colliderect(w6)or p2.colliderect(w7) or p2.colliderect(w8) or p2.colliderect(w9) or p2.colliderect(w10) or p2.colliderect(w11) or p2.colliderect(w12) or p2.colliderect(w13) or p2.colliderect(w14) or p2.colliderect(w15) or p2.colliderect(w16) or p2.colliderect(w17) or p2.colliderect(w18) or p2.colliderect(w19):
        if pressed[pygame.K_UP]:
            y2 += 3

        if pressed[pygame.K_DOWN]:
            y2 -= 3

        if pressed[pygame.K_LEFT]:
            x2 += 3

        if pressed[pygame.K_RIGHT]:
            x2 -= 3

# Finish Collision:
    if p1.colliderect(finish):
        p1_wins += 1
        winner = "Player 1"
        end_timer = time.time()
        timer = round(end_timer - start_timer, 2)  # stroggylopoiw ton xrono sta 2 dekadika psifia
        print(timer)
        if timer < best_time: # gia na vrw to kalutero xrono apo tous 5 gyrous
            best_time = timer
            print("Player 1, you achieved a highscore!")
        x1 = 20
        y1 = 20
        start_timer = time.time()

    if p2.colliderect(finish):
        p2_wins += 1
        winner = "Player 2"
        end_timer = time.time()
        timer = round(end_timer - start_timer, 2)  # stroggylopoiw ton xrono sta 2 dekadika psifia
        print(timer)
        if timer < best_time: # gia na vrw to kalutero xrono apo tous 5 gyrous
            best_time = timer
            print("Player 2, you achieved a highscore!")
        x2 = 1330
        y2 = 20
        start_timer = time.time()

    font = pygame.font.SysFont("Tahoma", 25)  # Tahoma = onoma grammatoseiras, 25 = megethos grammatwn
    text = font.render("Winner: " + winner, True, (0, 0, 0))
    screen.blit(text, (590, 20))
    timer_text = font.render("Time: " + str(timer), True, (0, 0, 0))  # grafw to keimeno pou thelw kai to xrvmatizw
    screen.blit(timer_text, (590, 50))

# End:
    if p1_wins == 3:
        screen.fill((43, 207, 240))
        font = pygame.font.SysFont("Tahoma", 25)
        gameovertext = font.render("Congratulations! Player 1 won. Your best time was: " + str(best_time), True, (255, 238, 238))
        screen.blit(gameovertext, (500, 500))

    elif p2_wins == 3:
        screen.fill((43, 207, 240))
        font = pygame.font.SysFont("Tahoma", 25)
        gameovertext = font.render("Congratulations! Player 2 won. Your best time was: " + str(best_time), True, (255, 238, 238))
        screen.blit(gameovertext, (370, 420))

    pygame.display.flip()