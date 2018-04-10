# -*- coding: utf-8 -*-

import random
import potatomanCore, potatomanAI

def auto_fullgame(playerName, AI_level):
	#カードの作成
	cards = list(potatomanCore.deck)
	#4人分に分ける
	hand = [[cards.pop(random.randrange(len(cards))) for i in range(12)] for i in range(4)]
	#CPUプレイヤーの作成
	players = [potatomanCore.Player(playerName[i], hand[i], potatomanAI.level[AI_level[i]]) for i in range(4)]
	#プレイヤーのシャッフル
	random.shuffle(players)

	count = 1
	flg = [0, -1, -1]
	pointCard = [3 for color in potatomanCore.colors]
	while flg[0] == 0:
		print("ターン {0}".format(count))
		flg, result_str = potatomanCore.trick(players)
		print(result_str)
		print()
		if flg[0] == 1 or count == 12:
			break

		if pointCard[flg[2]] != 0:
			point = potatomanCore.color_point(flg[2])
			pointCard[flg[2]] = pointCard[flg[2]] - 1
		else:
			point = 5
		players[flg[1]].addPoint(point)
		print("このターンの勝者 {0:<4} （{1}点）".format(players[flg[1]].getName(), potatomanCore.color_point(flg[2])))
		print()
		print('現在の得点')
		for player in players:
			print("{0:<4} : {1:>2}点".format(player.getName(), player.getPoint()))
		print()
		print('残りのポイントカード')
		for color in potatomanCore.colors:
			print("{0} :  {1}枚".format(potatomanCore.colors_str[color], pointCard[color]))
		print()
		count = count + 1
		if flg[1] != 0:
			for i in range(flg[1]):
				players.append(players.pop(0))

	if count == 12 and flg[0] == 0:
		print('12ターン経過のためゲーム終了')
		print()
	else:
		print(players[flg[1]].getName() + ' の ' + potatomanCore.colors_str[flg[2]] + '色 がないためゲーム終了')
		print()

	for name in ['YOU', 'CPU1', 'CPU2', 'CPU3']:
		for player in players:
			if player.getName() == name:
				players.append(players.pop(players.index(player)))
				break

	print('最終得点')
	for player in players:
		print("{0:<4} : {1:>2}点".format(player.getName(), player.getPoint()))
	print()
	points = [players[i].getPoint() for i in range(len(players))]

	p_max_num = 0
	win = [0, 0, 0, 0]
	p_max = max(points)
	for player in players:
		if player.getPoint() == p_max:
			p_max_num = p_max_num + 1
	for player in players:
		if player.getPoint() == p_max:
			win[players.index(player)] = 1 / float(p_max_num)

	return [count,] + win + points



def auto_fullgame_silent(playerName):
	#カードの作成
	cards = list(deck)
	#4人分に分ける
	hand = [[cards.pop(random.randrange(len(cards))) for i in range(12)] for i in range(4)]
	#CPUプレイヤーの作成
	players = [Player(playerName[i], hand[i], potatomanAI.level[3]) for i in range(4)]
	#プレイヤーのシャッフル
	random.shuffle(players)

	count = 1
	flg = [0, -1, -1]
	pointCard = [3 for color in potatomanCore.colors]
	while flg[0] == 0:
		flg = potatomanCore.trick(players)[0]
		if flg[0] == 1 or count == 12:
			break

		if pointCard[flg[2]] != 0:
			point = potatomanCore.color_point(flg[2])
			pointCard[flg[2]] = pointCard[flg[2]] - 1
		else:
			point = 5
		players[flg[1]].addPoint(point)
		count = count + 1
		if flg[1] != 0:
			for i in range(flg[1]):
				players.append(players.pop(0))

	for name in ['YOU', 'CPU1', 'CPU2', 'CPU3']:
		for player in players:
			if player.getName() == name:
				players.append(players.pop(players.index(player)))
				break

	print('最終得点')
	for player in players:
		print("{0:<4} : {1:>2}点".format(player.getName(), player.getPoint()))
	print()
	points = [players[i].getPoint() for i in range(len(players))]

	p_max_num = 0
	win = [0, 0, 0, 0]
	p_max = max(points)
	for player in players:
		if player.getPoint() == p_max:
			p_max_num = p_max_num + 1
	for player in players:
		if player.getPoint() == p_max:
			win[players.index(player)] = 1 / float(p_max_num)

	return [count,] + win + points
