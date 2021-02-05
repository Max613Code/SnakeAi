from SnakeAi import game
from SnakeAi import ai
import numpy as np
import random

#main_game = game.Game()
#main_game.initialize()
#main_game.play_draw()

Ai = ai.ai()
ai_game = game.Game()

dataa = []
dataa_result = []

ai_list=[]
list_fitness = []
best_ai = []
highest_scores = []
random_len = 100

for i in range(25):
    ai_list.append(ai.ai())
    ai_list[i].num = i
for j in ai_list:
    j.game = game.Game()
    j.game.reset()
    j.game.initialize()
    j.game.play_ai(j)
    #print(len(j.data), len(j.data_result))
    for i in range(1):
        j.game.reset()
        j.game.initialize()
        j.game.play_ai(j)
for j in ai_list:
    list_fitness.append(j.game.calculted_fitness())
    print(j.game.fitness)

highest = list_fitness.index(np.amax(list_fitness))
listfc = list_fitness.copy()
listfc.sort()
highest_scores.append(list_fitness.index(listfc[-3]))
highest_scores.append(list_fitness.index(listfc[-2]))
highest_scores.append(highest)
best_ai.append(ai_list[list_fitness.index(listfc[-3])])
best_ai.append(ai_list[list_fitness.index(listfc[-2])])
best_ai.append(ai_list[highest])

j = best_ai[-1]
j.game = game.Game()
j.game.reset()
j.game.initialize()
j.game.play_draw_ai(j)

for ii in range(50):
    ai_list=[]
    list_fitness = []

    for i in range(15):
        ai_list.append(ai.ai())
        ai_list[i].num = i
        if ((len(best_ai[-1].data))>random_len):
            ranAI = random.randint(1,3)
            random_len = int(len(best_ai[-ranAI].data)/17)
            randomL = [random.randint(0,len(best_ai[-ranAI].data)) for iii in range(random_len)]
            for j in randomL:
                ai_list[i].data.append(best_ai[-ranAI].data[j-1])
                ai_list[i].data_result.append(best_ai[-ranAI].data_result[j-1])
    for j in ai_list:
        j.game = game.Game()
        j.game.reset()
        j.game.initialize()
        j.game.play_ai(j)
        for i in range(1):
            j.game.reset()
            j.game.initialize()
            j.game.play_ai(j)

    for j in ai_list:
        list_fitness.append(j.game.calculted_fitness())
        print(j.game.fitness)

    highest = list_fitness.index(np.amax(list_fitness))
    listfc = list_fitness.copy()
    listfc.sort()
    highest_scores.append(list_fitness.index(listfc[-3]))
    highest_scores.append(list_fitness.index(listfc[-2]))
    highest_scores.append(highest)
    best_ai.append(ai_list[list_fitness.index(listfc[-3])])
    best_ai.append(ai_list[list_fitness.index(listfc[-2])])
    best_ai.append(ai_list[highest])

    for iiii in range(2):
        a = input()
        j = best_ai[-1]
        j.game = game.Game()
        j.game.reset()
        j.game.initialize()
        j.game.play_draw_ai(j)

j = best_ai[-1]
j.game = game.Game()
j.game.reset()
j.game.initialize()
j.game.play_draw_ai(j)

# for i in range(200):
#     del Ai
#     Ai = ai.ai()
#     Ai.data = []
#     Ai.data_result = []
#     del ai_game
#     ai_game = game.Game()
#     ai_game.reset()
#     ai_game.initialize()
#     print(ai_game.fitness)
#     ai_game.play_draw_ai(Ai)
#     dataa += Ai.data
#     dataa_result += Ai.data_result


