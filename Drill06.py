from pico2d import *
from random import randint

# 클릭한 위치에 손 화살표가 만들어짐(2점)
# 소년이 차례대로 따라감(1점)
# 소년이 도착한 손화살표는 사라짐(1점)

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
	global pointList
	events = get_events()

	for event in events:
		if event.type == SDL_MOUSEBUTTONDOWN:
			x, y = event.x, TUK_HEIGHT - 1 - event.y
			pointList.append([x,y])

frame = 0
def animation_right(x, y):
	global frame, pointList
	clear_canvas()
	TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	for arrx, arry in pointList:
		arrow.draw(arrx, arry)
	character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y, 100, 100)
	update_canvas()
	frame = (frame + 1) % 8

def animation_left(x, y):
	global frame
	clear_canvas()
	TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	for arrx, arry in pointList:
		arrow.draw(arrx, arry)
	character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
	update_canvas()
	frame = (frame + 1) % 8

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
pointList = []

while True:
	animation_left(x, y)
	handle_events()
