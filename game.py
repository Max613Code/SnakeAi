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

    food_location = (50,200)

    score =0

    survived = 0

    fitness=0

    ai_choice = 0

    choices = []

    draw_ai = False

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
        #print(self.food_location)
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

    def calculted_fitness(self):
        self.fitness = 10 * self.score + 0.1 * self.survived
        return self.fitness

    def get_surrounding(self):
        current_pos = self.snake[-1]
        result = [[0 for i in range(9)] for j in range(9)]
        for i in range(-4,5):
            for j in range(-4,5):
                position = [current_pos[0] + 25 * i, current_pos[1]+ 25 * j]
                if (position[0], position[1]) == self.food_location:
                    result[i+2][j+2] = 3
                elif position[0] == 0 or position[0] == self.x:
                    result[i+2][j+2] = 1
                elif position[1] == 0 or position[1] == self.y:
                    result[i+2][j+2] = 1
                for k in self.snake:
                    if k == (position[0], position[1]):
                        result[i+2][j+2] = 2
                if (result[i+2][j+2] == None):
                    position[i+2][j+2] = 0

        return result


    def reset(self):
        self.x = 500
        self.y = 500
        self.size = 25;

        self.squares = int(self.x / self.size)

        self.start_pos = (50, 50)

        self.snake = [self.start_pos, (50, 75), (50, 100), (50, 125), (50, 250)]
        self.snake_length = 1
        self.direction = 1

        self.win = 0

        self.run = True

        self.food_location = (50,200)  #(200,300)

        self.score = 0

        self.survived = 0

        self.fitness = 0

        self.ai_choice = 0

        self.choices = []

        self.draw_ai = False
    def play_ai(self, ai):
        while self.run:

            self.survived += 1
            self.calculted_fitness()

            state = self.check_state()

            if state == True:
                self.run = False
            elif state == "f":
                self.snake_length += 1
                self.score += 1
                if self.snake[0][1] == self.snake[1][1] + 25:
                    self.snake.insert(0, (self.snake[0][0], self.snake[0][1] - 25))
                if self.snake[0][0] == self.snake[1][0] - 25:
                    self.snake.insert(0, (self.snake[0][0] - 25, self.snake[0][1]))
                if self.snake[0][1] == self.snake[1][1] - 25:
                    self.snake.insert(0, (self.snake[0][0], self.snake[0][1] + 25))
                if self.snake[0][0] == self.snake[1][0] + 25:
                    self.snake.insert(0, (self.snake[0][0] + 25, self.snake[0][1]))
                a = random.randint(0,self.x)
                b = random.randint(0, self.y)
                self.food_location = (a - a%25, b-b%25)

            self.choice = ai.get_choice(self.get_surrounding())


            if self.choice ==1 and self.direction != 3:
                self.direction = 1
            elif self.choice == 2 and self.direction != 4:
                self.direction = 2
            elif self.choice == 3 and self.direction != 1:
                self.direction = 3
            elif self.choice == 4 and self.direction != 2:
                self.direction = 4

            self.choices.append(self.choice)

            ai.submit_info(self.get_surrounding(), self.run, self.choices, state)
            self.move()
            time.sleep(0.05)



        ai.submit_info(self.get_surrounding(), self.run, self.choices, state)

    def play_draw_ai(self,ai):
        pygame.event.pump()
        while self.run:
            self.survived += 1
            self.calculted_fitness()

            self.win = pygame.display.set_mode((1000, 500))

            pygame.time.delay(5)

            state = self.check_state()

            if state == True:
                self.run = False
            elif state == "f":
                self.snake_length += 1
                self.score += 1
                if self.snake[0][1] == self.snake[1][1] + 25:
                    self.snake.insert(0, (self.snake[0][0], self.snake[0][1] - 25))
                if self.snake[0][0] == self.snake[1][0] - 25:
                    self.snake.insert(0, (self.snake[0][0] - 25, self.snake[0][1]))
                if self.snake[0][1] == self.snake[1][1] - 25:
                    self.snake.insert(0, (self.snake[0][0], self.snake[0][1] + 25))
                if self.snake[0][0] == self.snake[1][0] + 25:
                    self.snake.insert(0, (self.snake[0][0] + 25, self.snake[0][1]))
                a = random.randint(0, self.x)
                b = random.randint(0, self.y)
                self.food_location = (a - a % 25, b - b % 25)

            self.draw_board()
            pygame.display.update()

            self.choice = ai.get_choice(self.get_surrounding())

            if self.choice == 1 and self.direction != 3:
                self.direction = 1
            elif self.choice == 2 and self.direction != 4:
                self.direction = 2
            elif self.choice == 3 and self.direction != 1:
                self.direction = 3
            elif self.choice == 4 and self.direction != 2:
                self.direction = 4

            self.choices.append(self.choice)

            ai.submit_info(self.get_surrounding(),  self.run, self.choices, state)
            self.move()
            pygame.display.update()
            time.sleep(0.25)
            #0.005


        ai.submit_info(self.get_surrounding(),  self.run, self.choices,state)

        pygame.quit()

    def play_draw(this):
        pygame.event.pump()
        while this.run:
            this.survived += 1
            this.calculted_fitness()
            print(this.fitness)
            this.win = pygame.display.set_mode((1000, 500))

            pygame.time.delay(90)

            state = this.check_state()

            if state == True:
                this.run = False
            elif state == "f":
                this.snake_length += 1
                this.score += 1
                if this.snake[0][1] == this.snake[1][1] + 25:
                    this.snake.insert(0,(this.snake[0][0], this.snake[0][1]-25))
                if this.snake[0][0] == this.snake[1][0]-25:
                    this.snake.insert(0,(this.snake[0][0]-25, this.snake[0][1]))
                if this.snake[0][1] == this.snake[1][1] - 25:
                    this.snake.insert(0,(this.snake[0][0], this.snake[0][1]+25))
                if this.snake[0][0] == this.snake[1][0]+25:
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
            #print(this.get_surrounding())


            #print(this.snake)




        pygame.quit()

