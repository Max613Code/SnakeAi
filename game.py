import random
import time
import pygame


class Game:
    x = 500
    y = 500
    size=25;

    squares = int(x/size)

    start_pos = (50, 50)

    snake = [start_pos, (50,75),(50,100), (50,125), (50,250)]
    snake_length = 1
    direction = 1

    win = 0

    run = True

    food_location = (200,300)

    def move(this):
        if (this.direction == 1):
            this.snake.append((this.snake[-1][0], this.snake[-1][1] - this.size))
            this.snake.pop(0)
        elif (this.direction == 2):
            this.snake.append((this.snake[-1][0] + this.size, this.snake[-1][1]))
            this.snake.pop(0)
        elif (this.direction == 3):
            this.snake.append((this.snake[-1][0], this.snake[-1][1] + this.size))
            this.snake.pop(0)
        elif (this.direction == 4):
            this.snake.append((this.snake[-1][0] - this.size, this.snake[-1][1]))
            this.snake.pop(0)

    def one_turn(self):
        for i in range(10):
            time.sleep(0.05)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                print("hi")

    def initialize(self):
        pygame.init()

    def get_win(self):
        global win
        return win

    def draw_board(self):
        pygame.draw.line(self.win, (255,255,255), (0,0), (0+self.x,0), 10)
        pygame.draw.line(self.win, (255, 255, 255), (self.x, 0), (self.x, 0+self.y), 10)
        pygame.draw.line(self.win, (255, 255, 255), (self.x, self.y), (0, self.y), 10)
        pygame.draw.line(self.win, (255, 255, 255), (0, 0), (0 , self.y), 10)

        for i in range(self.squares):
            for j in range(self.squares):
                pygame.draw.rect(self.win,(255,255,255), (i*self.size, j*self.size, self.size, self.size),1)
                #print((i*self.size, j*self.size))

        for i in self.snake:
            #print(i)
            pygame.draw.rect(self.win,(255,255,255), (i[0] - i[0] % 25, i[1] - i[1] % 25, self.size, self.size))
        print(self.food_location)
        pygame.draw.rect(self.win, (255, 0, 0), (self.food_location[0] - self.food_location[0] % 25, self.food_location[1] - self.food_location[1] % 25, self.size, self.size))

    def check_state(self):
        if (self.snake[-1][0] < 0 or self.snake[-1][0] > self.x or self.snake[-1][1] < 0 or self.snake[-1][1] > self.y):
            return True
        for i in self.snake:
            if self.snake.count(i) > 1:
                return True
            if (i == self.food_location):
                return "f"
        return False


    def play_draw(this):
        pygame.event.pump()
        while this.run:

            this.win = pygame.display.set_mode((1000, 500))

            pygame.time.delay(100)

            state = this.check_state()

            if state == True:
                this.run = False
            elif state == "f":
                this.snake_length += 1
                if this.direction == 1:
                    this.snake.insert(0,(this.snake[0][0], this.snake[0][1]-25))
                if this.direction == 2:
                    this.snake.insert(0,(this.snake[0][0]-25, this.snake[0][1]))
                if this.direction == 3:
                    this.snake.insert(0,(this.snake[0][0], this.snake[0][1]+25))
                if this.direction == 4:
                    this.snake.insert(0,(this.snake[0][0]+25, this.snake[0][1]))
                a = random.randint(0,this.x)
                b = random.randint(0, this.y)
                this.food_location = (a - a%25, b-b%25)

            #pygame.draw.rect(this.win,(255,255,255),(200,150,100,50))

            this.draw_board()
            pygame.display.update()

            keys = pygame.key.get_pressed()
            #print(keys)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_UP and this.direction != 3:
                        this.direction = 1
                    elif event.key == pygame.K_RIGHT and this.direction != 4:
                        this.direction = 2
                    elif event.key == pygame.K_DOWN and this.direction != 1:
                        this.direction = 3
                    elif event.key == pygame.K_LEFT and this.direction != 2:
                        this.direction = 4
                if event.type == pygame.QUIT:
                    this.run = False
            this.move()


            #print(this.snake)




        pygame.quit()

