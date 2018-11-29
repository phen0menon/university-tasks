import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

HEIGHT = 600
WIDTH = 800

BALL_RADIUS = 20
BALL_ALLOWED_VELOCITY = (-5, -4, -2, 2, 4, 5)

PAD_WIDTH = 8
PAD_HEIGHT = 80
PAD_SPEED = 5

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

paddle1_pos_end = [PAD_WIDTH, HEIGHT / 2 - PAD_HEIGHT / 2]
paddle1_pos_start = [PAD_WIDTH, HEIGHT / 2 + PAD_HEIGHT / 2]

paddle2_pos_end = [WIDTH - PAD_WIDTH, HEIGHT / 2 - PAD_HEIGHT / 2]
paddle2_pos_start = [WIDTH - PAD_WIDTH, HEIGHT / 2 + PAD_HEIGHT / 2]

paddle1_vel = [0, 0]
paddle2_vel = [0, 0]

score_right = 0
score_left = 0

def create_ui():
    frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
    frame.set_draw_handler(draw)
    frame.add_button("START GAME", new_game)
    frame.set_keydown_handler(keydown)
    frame.set_keyup_handler(keyup)
    frame.start()

def spawn_ball(direction):
    global ball_pos, ball_vel, score_right, score_left
    ball_pos = [WIDTH / 2, HEIGHT / 2]

    if direction == "RIGHT":
        ball_vel[0] = -random.randrange(120 / 60, 240 / 60)
        ball_vel[1] = -random.randrange(60 / 60, 180 / 60)
        score_left += 1
    if direction == "LEFT":
        ball_vel[0] = random.randrange(120 / 60, 240 / 60)
        ball_vel[1] = -random.randrange(60 / 60, 180 / 60)
        score_right += 1


def new_game():
    global paddle1_pos_end, paddle1_pos_start, paddle2_pos_end, paddle2_pos_start, paddle1_vel, paddle2_vel
    global score_left, score_right, ball_pos, ball_vel

    score_left = 0
    score_right = 0

    paddle1_pos_end = [PAD_WIDTH, HEIGHT / 2 - PAD_HEIGHT / 2]
    paddle1_pos_start = [PAD_WIDTH, HEIGHT / 2 + PAD_HEIGHT / 2]

    paddle2_pos_end = [WIDTH - PAD_WIDTH, HEIGHT / 2 - PAD_HEIGHT / 2]
    paddle2_pos_start = [WIDTH - PAD_WIDTH, HEIGHT / 2 + PAD_HEIGHT / 2]

    ball_pos = [WIDTH / 2, HEIGHT / 2]

    ball_vel[0] = random.choice(BALL_ALLOWED_VELOCITY)
    ball_vel[1] = random.choice(BALL_ALLOWED_VELOCITY)

def move_ball(canvas):
    global ball_pos, score_right, score_left, ball_vel

    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "Red")
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[0] <= BALL_RADIUS:
        if ball_pos[1] <= paddle1_pos_start[1] + 5 and ball_pos[1] > paddle1_pos_end[1] + 5:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:
            spawn_ball("LEFT")
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - 1:
        if ball_pos[1] <= paddle2_pos_start[1] + 5 and ball_pos[1] > paddle2_pos_end[1] + 5:
            ball_vel[0] *= -1.1
            ball_vel[1] *= 1.1
        else:
            spawn_ball("RIGHT")

    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS - 1:
        ball_vel[1] *= -1

def draw_lines(canvas):
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

def draw_paddles(canvas):
    canvas.draw_line(paddle1_pos_start, paddle1_pos_end, 12, "Red")
    canvas.draw_line(paddle2_pos_start, paddle2_pos_end, 12, "Red")

def draw_score(canvas):
    canvas.draw_text(str(score_left) + "  " + str(score_right), [WIDTH / 2 - 23, 30], 30, "White")

def draw(canvas):
    global paddle1_pos_end, paddle1_pos_start, paddle2_pos_start, paddle2_pos_end

    paddle1_pos_end, paddle1_pos_start = move_paddle(paddle1_pos_end, paddle1_pos_start, paddle1_vel)
    paddle2_pos_end, paddle2_pos_start = move_paddle(paddle2_pos_end, paddle2_pos_start, paddle2_vel)

    move_ball(canvas)
    draw_lines(canvas)
    draw_paddles(canvas)
    draw_score(canvas)

def move_paddle(paddle_pos_start, paddle_pos_end, paddle_vel):
    if (paddle_pos_start[1] + paddle_vel[1] > 5 and (paddle_pos_end[1] + paddle_vel[1]) < HEIGHT - 5):
        paddle_pos_end[1] += paddle_vel[1]
        paddle_pos_start[1] += paddle_vel[1]

    return (paddle_pos_start, paddle_pos_end)

def keydown(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -PAD_SPEED
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = PAD_SPEED
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = -PAD_SPEED
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = PAD_SPEED


def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0

if __name__ == '__main__':
    new_game()
    create_ui()