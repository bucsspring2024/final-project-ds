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
        self.title = self.screen.blit(self.font.render("Cookie Clicker", True, "white"), (self.width/2-250,100))
        
        self.start_cookie = Sprite(self.width/2-250, self.height/2-200)
        self.start_group = pygame.sprite.GroupSingle()
        self.main_group = pygame.sprite.GroupSingle()
        self.start_group.add(self.start_cookie)
        self.blit = self.start_group.draw(self.screen)
        # self_start_cookie_sprite = pygame.sprite.Group()
        # self.all_sprites = pygame.sprite.Group(self.start_cookie)
        
        
        self.bills_per_click = 1
        self.siwabills = 0
        self.click_per_second = 0
        next()
    
    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_cookie.rect.collidepoint(event.pos):
                        self.screen.fill(self.background_color)
                        next()
                        
                        self.screen.fill(self.background_color)    
                        self.title
                        self.store_color = (10, 154, 250)
                        self.store_box = pygame.draw.rect(self.screen, self.store_color, (self.width/2, 0, self.width/2, self.height))
                        self.game_cookie = Sprite(self.width/8, self.height/4, "./../assets/chocchip.png", 0.5)
                        self.main_group.add(self.game_cookie)
                        self.main_group.draw(self.screen)
                        self.game_currency = Sprite(0, 0, "./../assets/siwabill.png", 0.33)
                        self.currency_group = pygame.sprite.GroupSingle(self.game_currency)
                        self.currency_group.draw(self.screen)
                        self.currency_count = self.screen.blit(self.font.render(":"+str(self.siwabills), True, "green"), (self.width/4-250,0))
                        next()
                        
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.game_cookie.rect.collidepoint(event.pos):
                                self.siwabills += self.bills_per_click
                                self.screen.fill(self.background_color)
                                self.store_box
                                self.currency_group.draw(self.screen)
                                self.currency_count = self.screen.blit(self.font.render(":"+str(self.siwabills), True, "green"), (self.width/4-100,0))
                                
                                
                        
                        
                        
                        

    # def store(self):
    #     self.store_color = (10, 154, 250)
    #     self.store_box = pygame.draw.rect(self.screen, self.store_color, (self.width/2, 0, self.width/2, self.height))
        
    def main_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            
    def mainloop(self):
        self.start = self.start_game()

def main():
    pygame.init()   
    start = Controller()
    start.mainloop()
                      
if __name__ == '__main__':
    main()
# if True:
#     for event in pygame.event.get():
#         pass
#         screen = pygame.display.set_mode() 
#         width = screen.get_width() #1680
#         height = screen.get_height() #1050
#         screen.fill((209,152,61))
#         title = pygame.font.Font(None, 100)
#         screen.blit(title.render("Cookie Clicker", True, "white"), (width/2-250,100))
#         next()
#         wait()
#         while event.type == pygame.QUIT():
#             pygame.quit()
#             exit()