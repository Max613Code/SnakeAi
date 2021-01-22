from SnakeAi import game
from SnakeAi import ai

#main_game = game.Game()
#main_game.initialize()
#main_game.play_draw()

Ai = ai.ai()
ai_game = game.Game()
ai_game.initialize()
ai_game.play_draw_ai(Ai)