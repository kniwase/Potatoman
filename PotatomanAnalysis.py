# -*- coding: utf-8 -*-
import sys
import potatoman

def main():
	args = sys.argv

	#試行回数 n
	n = int(args[1])
	#AIのレベル設定
	AI_level = []
	if len(args) >= 3:
		for arg in args[2]:
			if arg != 'H':
				AI_level.append(int(arg))
			elif arg != 'A':
				AI_level.append(arg)
			else:
				AI_level.append(arg)
	else:
		AI_level = [3,3,3,3]

	turn = [0 for i in range(12)]
	s = 0.0
	points = [0 for i in range(8)]

	for i in range(n):
		print("第 " + str(i+1) + " 試合")
		result = potatoman.fullgame(['CPU1', 'CPU2', 'CPU3', 'CPU4'], AI_level, isSilent=True)
		turn[result[0]-1] = turn[result[0]-1] + 1
		s = s + result[0]
		for i in range(8):
			points[i] = points[i] + result[i + 1]

	for i in range(4):
		points[i] = round(float(points[i]) / n * 100, 2)
	for i in range(4,8):
		points[i] = round(float(points[i]) / n, 2)
	print("ターン数分布")
	print(turn)
	print("平均ターン数 : " + str(s / n))
	print("　　勝率　　 : " + str(points[0:4]))
	print("　平均得点　 : " + str(points[4:8]))

if __name__=='__main__':
	main()
