from SnakeAi import game
from SnakeAi import ai

#main_game = game.Game()
#main_game.initialize()
#main_game.play_draw()

Ai = ai.ai()
ai_game = game.Game()

dataa = []
dataa_result = []

for i in range(200):
    del Ai
    Ai = ai.ai()
    Ai.data = []
    Ai.data_result = []
    del ai_game
    ai_game = game.Game()
    ai_game.reset()
    ai_game.initialize()
    print(ai_game.fitness)
    ai_game.play_draw_ai(Ai)
    dataa += Ai.data
    dataa_result += Ai.data_result


