import pgzrun
import random
import math

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

player = Actor('player', (CENTER_X, CENTER_Y))
player.angle = 0

bugs = []
bullets = []
score = 0
bug_speed = 2
bullet_speed = 5

def spawn_bug():
    bug = Actor('bug', (random.choice([0, WIDTH]), random.choice([0, HEIGHT])))
    bug.angle = random.randint(0, 360)
    bugs.append(bug)

def update():
    global score
    if score >= 100:
        print("You won! Score: 100")
        exit()
    
    if keyboard.left:
        player.angle += 5
    if keyboard.right:
        player.angle -= 5
    if keyboard.space:
        shoot_bullet()

    for bug in bugs[:]:
        bug.x += bug_speed * math.cos(math.radians(bug.angle))
        bug.y -= bug_speed * math.sin(math.radians(bug.angle))

        if bug.colliderect(player):
            print("Game Over! You were hit by a bug.")
            exit()

        if bug.x < 0 or bug.x > WIDTH or bug.y < 0 or bug.y > HEIGHT:
            bugs.remove(bug)
            score += 1

    for bullet in bullets[:]:
        #bullet.x += bullet_speed * math.cos(math.radians(player.angle))
        #bullet.y -= bullet_speed * math.sin(math.radians(player.angle))
        bullet.x += bullet_speed * math.cos(math.radians(xvel))
        bullet.y += bullet_speed * math.cos(math.radians(yvel))

        if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
            bullets.remove(bullet)
            continue

        for bug in bugs[:]:
            if bullet.colliderect(bug):
                bugs.remove(bug)
                bullets.remove(bullet)
                score += 1
                break

def shoot_bullet():
    global xvel, yvel
    xvel = player.angle
    yvel = player.angle
i
    if len(bugs) != 0:
        bullets.append(Actor('bullet', (player.x, player.y), angle=player.angle))

def draw():
    screen.clear()
    screen.fill(color=(23, 28, 41))
    player.draw()
    for bug in bugs:
        bug.draw()
    for bullet in bullets:
        bullet.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")

def update_bug_spawn():
    spawn_bug()
    clock.schedule(update_bug_spawn, random.uniform(0.5, 2.0))

update_bug_spawn()
pgzrun.go()
