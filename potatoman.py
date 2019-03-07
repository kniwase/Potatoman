# -*- coding: utf-8 -*-

import random
import potatomanCore, potatomanAI

colors_str = ['黄', '緑', '青', '赤']

def fullgame(playerName, AI_level, isSilent = False):
	if not isSilent: print('ゲームスタート！')
	#フィールドの作成
	field = potatomanCore.Field()
	#カードの作成
	cards = list(potatomanCore.deck)
	#4人分に分ける
	hand = [[cards.pop(random.randrange(len(cards))) for i in range(12)] for i in range(4)]
	#CPUプレイヤーの作成
	players = [potatomanCore.Player(playerName[i], hand[i], potatomanAI.level[AI_level[i]], AI_level[i] == 'H') for i in range(4)]
	#プレイヤーのシャッフル
	random.shuffle(players)

	for player in players:
		if player.isHuman:
			if not isSilent: print('%s の手札' % player.getName())
			for color in potatomanCore.colors:
				if not isSilent: print('%s色： %s' % (colors_str[color], ' '.join([str(card) for card in player.getCard(color)])))
			if not isSilent: print()

	count = 1
	flg = [0, -1, -1]
	field.pointCard = [3 for color in potatomanCore.colors]

	while flg[0] == 0:
		if not isSilent: print("ターン {0}".format(count))
		flg, result_str = potatomanCore.trick(field, players, isSilent)
		#ターンの結果表示
		if not isSilent: print()
		if not isSilent: print('このターンの結果： %s' % ',   '.join(result_str))
		if flg[0] == 1 or count == 12:
			break
		if field.pointCard[flg[2]] != 0:
			point = potatomanCore.color_point(flg[2])
			field.pointCard[flg[2]] -= 1
		else:
			point = 5
		players[flg[1]].addPoint(point)
		if not isSilent: print("このターンの勝者 {0:<4} （{1}点）".format(players[flg[1]].getName(), point))
		if not isSilent: print()
		if not isSilent: print('%-10s%-10s' % ('現在の得点', '残りのポイントカード'))
		for player, color in zip(players, potatomanCore.colors):
			if not isSilent: print('%-14s%-10s' % ('{0:<4} : {1:>2}点'.format(player.getName(), player.getPoint()), '{0} :  {1}枚'.format(potatomanCore.colors_str[color], field.pointCard[color])))
		if not isSilent: print()
		count = count + 1
		if flg[1] != 0:
			for i in range(flg[1]):
				players.append(players.pop(0))

	if count == 12 and flg[0] == 0:
		if not isSilent: print('12ターン経過のためゲーム終了')
		if not isSilent: print()
	else:
		if not isSilent: print(players[flg[1]].getName() + ' の ' + potatomanCore.colors_str[flg[2]] + '色 がないためゲーム終了')
		if not isSilent: print()

	for name in playerName:
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
