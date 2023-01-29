import pip 
pip.main(['install','pygame']#pour install 

import pygame


class Power4Game:
    def __init__(self):
        pygame.init()
        self.width = 700
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Power 4")

        self.grid = [[0 for x in range(7)] for y in range(6)]
        self.turn = 1
        self.Gris_token = pygame.image.load("Gris_token.png")
        self.white_token = pygame.image.load("white_token.png")
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // (self.width // 7)
                    self.play(col)

            self.draw_grid()
            pygame.display.update()

        pygame.quit()

    def draw_grid(self):
        self.screen.fill((255, 255, 255))

        for row in range(6):
            for col in range(7):
                pygame.draw.rect(self.screen, (0, 0, 0), (col * (self.width // 7), row * (self.height // 6), self.width // 7, self.height // 6), 2)
                if self.grid[row][col] == 1:
                    self.screen.blit(self.Gris_token, (col * (self.width // 7) + (self.width // 14) - 20, row * (self.height // 6) + (self.height // 12) - 20))
                elif self.grid[row][col] == 2:
                    self.screen.blit(self.white_token, (col * (self.width // 7) + (self.width // 14) - 20, row * (self.height // 6) + (self.height // 12) - 20))

    def play(self, col):
        for row in range(5, -1, -1):
            if self.grid[row][col] == 0:
                self.grid[row][col] = self.turn
                self.check_win(row, col)
                self.turn = 2 if self.turn == 1 else 1
                break
    def end_game(self):
            
            self.running = False
            font = pygame.font.Font(None, 36)
            text = font.render("Player " + str(self.turn) + " wins!", True, (0, 0, 0))
            self.screen.blit(text, (250, 300))
            pygame.display.update()
            pygame.time.wait(3000)
    def check_win(self, row, col):
    
            count = 0
            for i in range(col, 7):
                if self.grid[row][i] == self.turn:
                    count += 1
                    if count == 4:
                        self.end_game()
                else:
                    break
            for i in range(col, -1, -1):
                if self.grid[row][i] == self.turn:
                    count += 1
                    if count == 4:
                        self.end_game()
                else:
                    break
            count = 0
          
            for i in range(row, 6):
                if self.grid[i][col] == self.turn:
                    count += 1
                    if count == 4:
                        self.end_game()
                else:
                    break

            count = 0
            for i, j in zip(range(row, 6), range(col, -1, -1)):
                if i > 5 or j < 0:
                    break
                if self.grid[i][j] == self.turn:
                    count += 1
                if count == 4:
                        self.end_game()
                else:
                    break

    def check_win(self, row, col):
        
        count = 0
        for i in range(col, 7):
            if self.grid[row][i] == self.turn:
                count += 1
                if count == 4:
                    self.end_game()
            else:
                break
        for i in range(col, -1, -1):
            if self.grid[row][i] == self.turn:
                count += 1
                if count == 4:
                    self.end_game()
            else:
                break
        count = 0
        
        for i in range(row, 6):
            if self.grid[i][col] == self.turn:
                count += 1
                if count == 4:
                    self.end_game()
            else:
                break
       
        count = 0
        for i, j in zip(range(row, 6), range(col, -1, -1)):
            if i > 5 or j < 0:
                break
            if self.grid[i][j] == self.turn:
                count += 1
                if count == 4:
                    self.end_game()
            else:
                break
  
            
        
        


if __name__ == "__main__":
    game = Power4Game()
    
    game.run()
