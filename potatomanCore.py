# -*- coding: utf-8 -*-

colors = (YELLOW, GREEN, BLUE, RED) = range(4)
colors_str = {YELLOW:'黄', GREEN:'緑', BLUE:'青', RED:'赤'}
#colors_str = {YELLOW:'Yellow', GREEN:'Green', BLUE:'Blue', RED:'Red'}
colors_str_short = {YELLOW:'Y', GREEN:'G', BLUE:'B', RED:'R'}
def color_point(color):
	if YELLOW == color:
		return 4
	elif GREEN == color:
		return 3
	elif BLUE == color:
		return 2
	elif RED == color:
		return 1

class Card():
	def __init__(self, number, color):
		self.__color = color
		self.__number = number
	def getColor(self):
		return self.__color
	def getNumber(self):
		return self.__number
	def isPotatoman(self):
		return self.__number <= 3 and self.__number >= 1 and self.__color == YELLOW
	def isPotatokiller(self):
		return self.__number <= 18 and self.__number >= 16 and self.__color == RED
	def __str__(self):
		#return "{0:>2}".format(self.__number) + " of " + colors_str[self.__color]
		#return "{0} {1:>2}".format(colors_str[self.__color], self.__number)
		return '%s%s' % (colors_str[self.__color], self.__number)
	def __lt__(self, card):
		return str(self) < str(card)

deck = tuple([Card(i, YELLOW) for i in range(1, 14)] +
			 [Card(i, GREEN) for i in range(3, 15)] +
			 [Card(i, BLUE) for i in range(4, 17)] +
			 [Card(i, RED) for i in range(5, 19)]
			 )

class Player:
	def __init__(self, name, cards, potatomanAI, isHuman = False):
		self.__name = name
		self.__point = 0
		self.__hand = [[],[],[],[]]
		self.AI = potatomanAI
		self.isHuman = isHuman
		for card in cards:
			if YELLOW == card.getColor():
				self.__hand[YELLOW].append(card)
			elif GREEN == card.getColor():
				self.__hand[GREEN].append(card)
			elif BLUE == card.getColor():
				self.__hand[BLUE].append(card)
			elif RED == card.getColor():
				self.__hand[RED].append(card)
		for hand in self.__hand:
			hand.sort()
	def __str__(self):
		hand = self.__name
		for h in self.__hand:
			for card in h:
				hand = hand + '\n' + colors_str_short[card.getColor()] + str(h.index(card)) + ' :  ' + str(card)
		return hand
	def getName(self):
		return self.__name
	def getPoint(self):
		return self.__point
	def getCardNumber(self, color):
		return len(self.__hand[color])
	def getAllCardNumber(self):
		return sum([self.getCardNumber(color) for color in colors])
	def addPoint(self, n):
		self.__point = self.__point + n
	def discard(self, color, number):
		return self.__hand[color].pop(number)
	def getCard(self, color, number = None):
		if number == None:
			return self.__hand[color]
		else:
			return self.__hand[color][number]
	def hasPotatoman(self):
		flg = False
		for card in self.__hand[YELLOW]:
			flg = flg or card.isPotatoman()
		return flg

class Field:
	def __init__(self):
		self.__cards = []
		self.__discarded = []
		self.pointCard = [3 for color in colors]
	def getDiscarded (self):
		return self.__discarded
	def resetCards(self):
		self.__cards = []
	def append(self, card):
		self.__cards.append(card)
		self.__discarded.append(card)
	def size(self):
		return len(self.__cards)
	def getCardlist(self):
		return self.__cards
	def getCard(self, __index):
		return self.__cards[__index]
	def index(self, card):
		return self.__cards.index(card)
	def hasPotatoman(self):
		flg = False
		for card in self.__cards:
			flg = flg or card.isPotatoman()
		return flg
	def hasPotatokiller(self):
		flg = False
		for card in self.__cards:
			flg = flg or card.isPotatokiller()
		return flg


def compareCard(cards):
	flg = [False, False]
	winner = cards[0]
	for card in cards[1:]:
		if winner.getNumber() <= card.getNumber():
			winner = card
		if card.isPotatoman():
			flg[0] = True
			potatoman = card
		if card.isPotatokiller():
			flg[1] = True
	if flg[0] and flg[1]:
		winner = potatoman
	return winner


def trick(field, players, isSilent = False):
	#フィールドの初期化
	field.resetCards()
	#結果出力用変数 初期化
	s = []
	#フィールド上の残りの色の初期化
	restColors = list(colors)
	#各プレイヤートリック開始
	for player in players:
		for color in restColors:
			if player.getCardNumber(color) == 0:
				s.append(player.getName() + " : 出せるカードがない...")
				if not isSilent: print(s[-1])
				return [1, players.index(player), color], s

		#プレイヤーが人間なら現在のフィールドの状況を表示
		if player.isHuman:
			if not s:
				print('このトリックは ' + player.getName() + ' が最初のプレーヤーです')
			print('%s のターン！' % player.getName())

		player.AI(player, field, restColors)

		#結果出力
		s.append("{0}: {1}".format(player.getName(), str(field.getCard(players.index(player)))))
		if not isSilent: print(s[-1])

	#勝者の決定
	winner = compareCard(field.getCardlist())
	return [0, field.index(winner), winner.getColor()], s
