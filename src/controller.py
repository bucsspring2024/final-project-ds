from sprite import Sprite
import pygame
import random

def next():
    pygame.display.flip()
def wait():
    pygame.time.wait(5000)


class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode() 
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background_color = (209, 152, 61)
        self.screen.fill(self.background_color)
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.font = pygame.font.Font(None, 100)
        self.title = self.screen.blit(self.font.render("Cookie Clicker", True, "white"), (self.width/2 - 250, 100))
        
        self.start_cookie = Sprite(self.width/2 - 250, self.height/2 - 200)
        self.start_group = pygame.sprite.GroupSingle(self.start_cookie)
        self.start_group.draw(self.screen)
        self.game_cookie = Sprite(self.width/8, self.height/4, "./../assets/chocchip.png", 0.5)
        self.main_group = pygame.sprite.GroupSingle(self.game_cookie)
        self.blit = self.start_group.draw(self.screen)
        self.game_currency = Sprite(0, 0, "./../assets/siwabill.png", 0.50)
        self.currency_group = pygame.sprite.GroupSingle(self.game_currency)
        self.store_color = (10, 154, 250)
        self.bills_per_click = 1
        self.siwabills = 0
        self.better_click_cost = 100 
        self.click_boost = Sprite(850, 100, "./../assets/clickerupgrade.png", 0.25)
        self.clicker_group = pygame.sprite.GroupSingle(self.click_boost)
        self.click_per_second = 0
        next()
    
    
    def load(self):
        self.screen.fill(self.background_color)
        self.store_box = pygame.draw.rect(self.screen, self.store_color, (self.width/2, 0, self.width/2, self.height))
        self.main_group.draw(self.screen)
        self.currency_group.draw(self.screen)
        self.currency_count = self.screen.blit(self.font.render(":"+str(self.siwabills), True, "green"), (self.width/4+100, 75))
        self.clicker_group.draw(self.screen)
        
    def refresh(self):
        self.load()
        next()
        
    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_cookie.rect.collidepoint(event.pos):
                        self.screen.fill(self.background_color)
                        self.start_group.remove(self.start_cookie)
                        next()
                        
                        self.store_box = pygame.draw.rect(self.screen, self.store_color, (self.width/2, 0, self.width/2, self.height))
                        self.main_group.draw(self.screen)
                        self.currency_group.draw(self.screen)
                        self.currency_count = self.screen.blit(self.font.render(":"+str(self.siwabills), True, "green"), (self.width/4+100, 75))
                        self.clicker_group.draw(self.screen)
                        next()

                    if self.game_cookie.rect.collidepoint(event.pos):
                        self.siwabills += self.bills_per_click
                     
                    if self.click_boost.rect.collidepoint(event.pos):
                        if self.siwabills >= self.better_click_cost:
                            self.bills_per_click += 1
                            self.siwabills -= self.better_click_cost
                            self.better_click_cost *= 3
                
                x, y = pygame.mouse.get_pos()            
                if self.click_boost.rect.collidepoint((x, y)):
                    self.load()
                    pygame.draw.rect(self.screen, "white", (x, y, self.width/4, self.height/8))
                    next()
                    print(type(self.click_boost.rect.collidepoint(pygame.mouse.get_pos())))
                    
                elif self.click_boost.rect.collidepoint(pygame.mouse.get_pos()) == False and len(self.start_group) == 0:
                    self.refresh()
                    
    def main_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            
    # def mainloop(self):
    #     self.start = self.start_game()

# def main():
#     pygame.init()   
#     start = Controller()
#     start.mainloop()
                      
# if __name__ == '__main__':
#     main()
