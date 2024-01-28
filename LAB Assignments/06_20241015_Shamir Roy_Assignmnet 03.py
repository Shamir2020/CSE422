# Name - Shamir Roy
# ID - 20241015
# Course - CSE422
# Section - 06
# LAB 03

def AlphaBetaPruning(Index, depth ,alpha, beta, maxPlayer, points):

    if depth == 3:
        terminal = points[Index]
        return terminal
    if maxPlayer:
        optimalVal = -float('inf')

        for i in range(0, 2):
            value = AlphaBetaPruning(Index*2+i, depth + 1, alpha, beta, False, points)
            optimalVal = max(optimalVal, value)
            alpha = max(alpha, optimalVal)

            if beta <= alpha:
                break

        return optimalVal
    else:
        optimalVal = float('inf')

        for i in range(0,2):
            value = AlphaBetaPruning(Index*2 + i, depth+1, alpha, beta, True, points)
            optimalVal = min(optimalVal, value)
            beta = min(optimalVal, beta)

            if beta <= alpha:
                break

        return optimalVal



id = input('Enter your student ID: ')

minimum = id[4]
if minimum == '0':
    minimum = '8'
minimum = int(minimum)

last = id[len(id)-1]
beforeLast = id[len(id)-2]

maximum = 0
if last == '0':
    last = '8'
if beforeLast == '0':
    beforeLast = '8'

winPoints = int(last+beforeLast)
maximum = int(int(last+beforeLast) * 1.5)

points = []
import random
for i in range(8):
    points.append(random.randint(minimum, maximum))

print('Generated 8 random points between the minimum and maximum point')
print(f'Limits: {points}')
print(f'Total points to win: {winPoints}')

optimalPoint = AlphaBetaPruning(0, 0, -float('inf'),float('inf'), True, points)
print(f'Achieved by applying alpha-beta pruning = {optimalPoint}')

if optimalPoint >= winPoints:
    print('The winner is Optimus Prime')
else:
    print('The winner is Megatron')
