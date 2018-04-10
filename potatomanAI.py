# -*- coding: utf-8 -*-

import random
colors = (YELLOW, GREEN, BLUE, RED) = range(4)

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