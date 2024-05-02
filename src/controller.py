import pygame
from src.sprite import Sprite
import time
import random

class Controller:
    def font(self, font_scale = 5):
        """This method creates a standardized font and font size.

        Args:
            font_scale (int, optional): 5 is the highest scale that I use for this game. Defaults to 5.

        Returns:
            pygame.font.Font(): I used a good amount of code that needed this module, so I decided to return this.
        """
        self.font_standard = pygame.font.Font(None, 20*font_scale)
        return self.font_standard
    
    def next(self):
        """All this does is flips the pygame screen.
        """
        pygame.display.flip()
        
    def __init__(self):
        """The first section is where I placed all the screen variables; the next holds my game variables; then game sprites; and finally, their respective single sprite groups.
        """
        #Screen variables
        self.screen = pygame.display.set_mode() 
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background_color = (209, 152, 61)
        self.screen.fill(self.background_color)
        self.store_color = (10, 154, 250)
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        
        #Game variables
        self.offset = 5
        self.siwabills = 0
        self.clicks_per_second = 0
        self.better_auto_cost = 100
        self.bills_per_click = 1
        self.better_click_cost = 200
        self.better_sugar_cost = 300
        self.sugar_lower_limit = 1
        self.sugar_upper_limit = 11
        self.sugar_upper_limit_subtraction = 0
        self.win_condition = 1000000
        
        #Game sprites
        self.start_cookie = Sprite(self.width/2 - 250, self.height/2 - 200)
        self.game_cookie = Sprite(self.width/8, self.height/4, "assets/chocchip.png", 0.5)
        self.game_currency = Sprite(0, 0, "assets/siwabill.png", 0.25)
        self.auto_boost = Sprite(self.width/2 + 3*self.offset, self.height/10, "assets/autoupgrade.png", 0.25)
        self.clicker_boost = Sprite(self.auto_boost.rect.x + self.auto_boost.rect.width + 3*self.offset, self.auto_boost.rect.y, "assets/clickerupgrade.png", 0.25)
        self.sugar_cookie = Sprite(random.randrange(0, self.width/2 - 14*self.offset), random.randrange(self.game_currency.rect.height, self.height - 25*self.offset), "assets/sugarcook.png", 0.25)
        self.sugar_boost = Sprite(self.clicker_boost.rect.x + self.clicker_boost.rect.width + 3*self.offset, self.clicker_boost.rect.y, "assets/sugarupgrade.png", 0.25)
        
        #Sprite groups
        self.start_group = pygame.sprite.GroupSingle(self.start_cookie)
        self.main_group = pygame.sprite.GroupSingle(self.game_cookie)
        self.currency_group = pygame.sprite.GroupSingle(self.game_currency)
        self.auto_group = pygame.sprite.GroupSingle(self.auto_boost)
        self.clicker_group = pygame.sprite.GroupSingle(self.clicker_boost)
        self.sugar_group = pygame.sprite.GroupSingle()
        self.sweet_group = pygame.sprite.GroupSingle(self.sugar_boost)

    
    def load(self):
        """This creates the image of the entire main game screen.
        """
        self.screen.fill(self.background_color)
        self.store_box = pygame.draw.rect(self.screen, self.store_color, (self.width/2, 0, self.width/2, self.height))
        self.store = self.screen.blit(self.font().render("Store", True, "white"), (self.store_box.x + 5*self.offset, self.store_box.y + 4*self.offset))
        self.main_group.draw(self.screen)
        self.currency_group.draw(self.screen)
        self.currency_count = self.screen.blit(self.font().render(":" + str(self.siwabills) + " J", True, "green"), (self.game_currency.rect.width + self.offset, self.game_currency.rect.height/4 - self.offset))
        self.auto_group.draw(self.screen)
        self.auto_upgrade_cost = self.screen.blit(self.font(2).render(str(self.better_auto_cost)+" J", True, "green"), (self.auto_boost.rect.x + 3*self.offset, self.auto_boost.rect.y + self.auto_boost.rect.height + self.offset))
        self.clicker_group.draw(self.screen)
        self.click_upgrade_cost = self.screen.blit(self.font(2).render(str(self.better_click_cost)+" J", True, "green"), (self.clicker_boost.rect.x + 3*self.offset, self.clicker_boost.rect.y + self.auto_boost.rect.height + self.offset))
        self.sugar_group.draw(self.screen)
        self.sweet_group.draw(self.screen)
        self.sugar_upgrade_cost = self.screen.blit(self.font(2).render(str(self.better_sugar_cost)+" J", True, "green"), (self.sugar_boost.rect.x + 3*self.offset, self.sugar_boost.rect.y + self.clicker_boost.rect.height + self.offset))

        
    def refresh(self):
        """This flips the pygame screen to show the main game screen.
        """
        self.load()
        self.next()
    
    def start_screen(self):    
        """Reveals the start screen and handles the eventual transition to the main game screen. Also allows player to exit out of the game.
        """
        self.title = self.screen.blit(self.font().render("Cookie Clicker", True, "white"), (self.width/2 - 250, 100))
        self.start_group.draw(self.screen)
        self.next()
        while self.siwabills < self.win_condition and len(self.start_group) == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_cookie.rect.collidepoint(event.pos):
                        self.start_group.remove(self.start_cookie)
                        self.screen.fill(self.background_color)
                        self.goal = self.screen.blit(self.font().render("Reach 1,000,000 Jojobills. Good luck!", True, "green"), (self.width/7, self.height/2 - 5*self.offset))
                        self.next()
                        self.wait = time.sleep(3.00)
                        self.refresh()
                        
                  
    def main_game(self):
        """There are two parts to this module. The first section handles the mouse click interactions with each clickable sprite. The next part handles interactions with the shop. This area also manages the refreshing of the screen. Also allows player to exit out of the game.
        """
        while self.siwabills < self.win_condition:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                #Click interactions    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_cookie.rect.collidepoint(event.pos):
                        self.siwabills += self.bills_per_click
                        self.sugar_chance = random.randrange(self.sugar_lower_limit, self.sugar_upper_limit - self.sugar_upper_limit_subtraction)
                        if self.sugar_chance == 1 and len(self.sugar_group) == 0:
                            self.sugar_cookie = Sprite(random.randrange(0, self.width/2 - 14*self.offset), random.randrange(self.game_currency.rect.height, self.height - 25*self.offset), "assets/sugarcook.png", 0.25)
                            self.sugar_group.add(self.sugar_cookie)                         
                    if self.auto_boost.rect.collidepoint(event.pos):
                        if self.siwabills >= self.better_auto_cost:
                            if self.clicks_per_second == 0:
                                self.clicks_per_second += 1
                            else:
                                self.clicks_per_second *= 5
                            self.siwabills -= self.better_auto_cost
                            self.better_auto_cost *= 6
                    if self.clicker_boost.rect.collidepoint(event.pos):
                        if self.siwabills >= self.better_click_cost:
                            self.bills_per_click *= 5
                            self.siwabills -= self.better_click_cost
                            self.better_click_cost *= 6         
                    if self.sugar_cookie.rect.collidepoint(event.pos):
                        self.sugar_group.remove(self.sugar_cookie)
                        self.sugar_cookie = Sprite(-self.width, 0, "assets/sugarcook.png", 0.25)
                        self.siwabills += self.bills_per_click*100
                        self.refresh()
                    if self.sugar_boost.rect.collidepoint(event.pos):
                        if self.siwabills >= self.better_sugar_cost:
                            if self.sugar_upper_limit - self.sugar_upper_limit_subtraction > self.sugar_lower_limit + 1:
                                self.sugar_upper_limit_subtraction += 2
                                self.siwabills -= self.better_sugar_cost
                                self.better_sugar_cost *= 10
                                self.refresh()
            #Shop interactions
            if len(self.start_group) == 0:
                self.x, self.y = pygame.mouse.get_pos()                     
                if self.auto_boost.rect.collidepoint((self.x, self.y)):
                    self.load()
                    self.upgrade_box = pygame.draw.rect(self.screen, "white", (self.x - self.width/8, self.y, self.width/4, self.height/17))
                    self.upgrade_description = self.screen.blit(self.font(1).render("Multiplies clicks per second by 5 after second purchase!", True, (self.store_color)), (self.upgrade_box.x + self.offset, self.upgrade_box.y + self.upgrade_box.height/2 - self.offset))
                    self.next()    
                if self.clicks_per_second > 0:
                    time.sleep(1.00)
                    self.siwabills += self.clicks_per_second
                    self.refresh()
                if self.clicker_boost.rect.collidepoint((self.x, self.y)):
                    self.load()
                    self.upgrade_box = pygame.draw.rect(self.screen, "white", (self.x - self.width/12, self.y, self.width/6, self.height/17))
                    self.upgrade_description = self.screen.blit(self.font(1).render("Multiplies power of clicking by 5!", True, (self.store_color)), (self.upgrade_box.x + self.offset, self.upgrade_box.y + self.upgrade_box.height/2 - self.offset))
                    self.next()
                if self.sugar_boost.rect.collidepoint((self.x, self.y)):
                    self.load()
                    self.upgrade_box = pygame.draw.rect(self.screen, "white", (self.x - self.width/10, self.y, self.width/5, self.height/17))
                    self.upgrade_description = self.screen.blit(self.font(1).render("Increases chance of getting sugar cookie!", True, (self.store_color)), (self.upgrade_box.x + self.offset, self.upgrade_box.y + self.upgrade_box.height/2 - self.offset))
                    self.next()
                #Refreshs pygame screen               
                if self.auto_boost.rect.collidepoint(pygame.mouse.get_pos()) == False and self.clicker_boost.rect.collidepoint(pygame.mouse.get_pos()) == False and self.sugar_boost.rect.collidepoint(pygame.mouse.get_pos()) == False:
                    self.refresh()
                    
    def end(self):    
        """This handles the transition to the end screen when the currency reachs high enough. Also allows player to exit out of the game.
        """
        while self.siwabills >= self.win_condition:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()     
            self.background_group = pygame.sprite.Group()            
            for x in range(7):
                self.money_horizontal = Sprite(0 + self.game_currency.rect.width*x, 0, "assets/siwabill.png", 0.25)
                for y in range(10):
                    self.money_vertical = Sprite(self.money_horizontal.rect.x, self.game_currency.rect.height*y, "assets/siwabill.png", 0.25)
                    self.background_group.add(self.money_horizontal, self.money_vertical)
            self.background_group.draw(self.screen)
            self.win_words = self.screen.blit(self.font().render("Wow, you are so rich!", True, "white"), (self.width/4 + 15*self.offset, self.height/2 - 5*self.offset))
            self.next()
            
    def mainloop(self):
        """Handles the complete transition of the game.
        """
        self.start_screen()
        self.main_game()
        self.end()
        