# -*- coding: utf-8 -*-

import random
colors = (YELLOW, GREEN, BLUE, RED) = range(4)
colors_str2num = {'Y':YELLOW, 'G':GREEN, 'B':BLUE, 'R':RED}
colors_str = ['黄', '緑', '青', '赤']

#人間用
def human(player, field, restColors):
	restColors_tmp = list(restColors)
	for color in restColors:
		if player.getCardNumber(color) == 0:
			restColors_tmp.remove(color)
	for color in restColors:
		print('%s色で出せるカード： %s' % (colors_str[color], ' '.join([str(card) for card in player.getCard(color)])))
	print()
	print('出すカードの色を選んでください（黄:Y, 緑:G, 青:B, 赤:R 例: 赤15 → R15）')
	while True:
		sel_card = input()
		try:
			sel_color = colors_str2num[sel_card[0]]
			if not sel_color in restColors:
				print('%s色は今は選べないので、もう一度入力してください' % colors_str[sel_color])
				continue
		except KeyError:
			print('色を正しく指定して、もう一度入力してください')
			continue
		try:
			sel_num = int(sel_card[1:])
			sel_idx = [card.getNumber() for card in player.getCard(sel_color)].index(sel_num)
		except ValueError:
			print('数字を正しく指定して、もう一度入力してください')
			continue
		break
	field.append(player.discard(sel_color, sel_idx))

#POTATOMAN AI
#完全乱数
def level0(player, field, restColors):
	restColors_tmp = list(restColors)
	for color in restColors:
		if player.getCardNumber(color) == 0:
			restColors_tmp.remove(color)
	color = restColors.pop(restColors.index(random.choice(restColors_tmp)))
	field.append(player.discard(color, random.randrange(player.getCardNumber(color))))

#残り枚数が一番多い色から出す
def level1(player, field, restColors):
	restColors_tmp = list(restColors)
	for color in restColors:
		if player.getCardNumber(color) == 0:
			restColors_tmp.remove(color)
	numbers = [player.getCardNumber(color) for color in restColors]
	color = restColors[numbers.index(max(numbers))]
	restColors.remove(color)
	field.append(player.discard(color, random.randrange(player.getCardNumber(color))))

#大きな数が出ている場合ポテトマンを除く一番小さい数字を出す
def level2(player, field, restColors):
	restColors_tmp = list(restColors)
	for color in restColors:
		if player.getCardNumber(color) == 0:
			restColors_tmp.remove(color)
	numbers = [player.getCardNumber(color) for color in restColors]
	color = restColors[numbers.index(max(numbers))]
	restColors.remove(color)
	if field.size() == 0:
		field.append(player.discard(color, random.randrange(player.getCardNumber(color))))
	else:
		if max([card.getNumber() for card in field.getCards()]) > max([player.getCard(color)[i].getNumber() for i in range(player.getCardNumber(color))]):
			if color == YELLOW:
				c = player.getCard(YELLOW)[0]
				for card in player.getCard(YELLOW):
					if card.getNumber() >= 4:
						c = card
						break
				field.append(player.discard(color, player.getCard(YELLOW).index(c)))
			else:
				field.append(player.discard(color, 0))
		else:
			field.append(player.discard(color, random.randrange(player.getCardNumber(color))))

#ポテトキラーが出ていて黄色が出ていなかったらポテトマンを出す
def level3(player, field, restColors):
	restColors_tmp = list(restColors)
	for color in restColors:
		if player.getCardNumber(color) == 0:
			restColors_tmp.remove(color)

	numbers = [player.getCardNumber(color) for color in restColors]
	color = restColors[numbers.index(max(numbers))]
	restColors.remove(color)
	if field.size() == 0:
		field.append(player.discard(color, random.randrange(player.getCardNumber(color))))
	else:
		if max([card.getNumber() for card in field.cardlist()]) > max([player.getCard(color)[i].getNumber() for i in range(player.getCardNumber(color))]):
			if color == YELLOW:
				c = player.getCard(YELLOW)[0]
				for card in player.getCard(YELLOW):
					if card.getNumber() >= 4:
						c = card
						break
				field.append(player.discard(color, player.getCard(YELLOW).index(c)))
			else:
				field.append(player.discard(color, 0))
		else:
			field.append(player.discard(color, random.randrange(player.getCardNumber(color))))

level = [level0, level1, level2, level3]
level.append(human)
