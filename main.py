from asyncio import events
import pygame 
pygame.init()






class FlappyBird:
    running = True

    def __init__(self,**kwargs):
        super(FlappyBird,self).__init__(**kwargs)
        self.screen = pygame.display.set_mode((1200,600))
        self.clock = pygame.time.Clock()
        self.fps = 60  
        self.bg = Load_background()
        self.character = Load_BirdPlayer()
        self.load_main_game()

    
    def load_main_game(self):
        while self.running:
            self.clock.tick(self.fps)
            self.load_controls()
            self.update()
    
    def load_controls(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.running = False
            
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_RIGHT:
                    pass
            
                if self.event.key == pygame.K_UP:
                    self.character.dy -= 3
                
                if self.event.key == pygame.K_DOWN:
                    self.character.dy += 3

            if self.event.type == pygame.KEYUP:
                self.character.MOVING = False
                self.character.dy = 0
              




    def update(self):
        self.screen.fill((0,0,0))
        self.bg.draw_background(self.screen)
        self.character.draw_bird(self.screen)

        pygame.display.update()



class Load_background:
    def __init__(self,**kwargs):
        super(Load_background,self).__init__(**kwargs)
        self.img_list = []
        self.load_images()
        self.width = self.img_list[0].get_width()
        self.scroll = 5
        self.move_bg = False
        self.state = "moving"
        

    def load_images(self):
        for i in range(1,6):
            self.img = pygame.image.load(f"assets/plx-{i}.png").convert_alpha()
            self.img = pygame.transform.scale(self.img,(1200,600))
            self.img_list.append(self.img)   

    def draw_background(self,screen):
        self.keys()
        for i in range(10):
            speed = 1
            
            for x in self.img_list:
                screen.blit(x,((i*self.width)-self.scroll * speed,0))
                

                speed += 0.2
    
    def keys(self):
        key = pygame.key.get_pressed()

        if self.state == "moving" and self.scroll <= 6000:
            self.scroll += 5


        if key[pygame.K_RIGHT] and self.scroll <= 6000:
            # self.scroll += 5
            pass
            
        
        elif key[pygame.K_LEFT] and self.scroll > 0:
            # self.scroll -= 5
            pass



class Load_BirdPlayer:
    def __init__(self,**kwargs):
        super(Load_BirdPlayer,self).__init__(**kwargs)
        self.birdList = []
        self.load_images()
        self.current_frame = 0
        self.last_updated = 0
        self.current_image = self.birdList[0]
        self.state = "playing"
        self.dy = 0
        self.y = 200
        self.MOVING = True
        # self.background = Load_background()

    

    
    def load_images(self):
        path = "assets/bird/images/"
        for i in range(1,15):
            self.img = pygame.image.load(path+f"bird ({i}).png").convert_alpha()
            self.img = pygame.transform.rotozoom(self.img,0,0.6)
            self.birdList.append(self.img)

    def draw_bird(self,screen):
        self.animate_bird()
        # self.keys()
        self.y += self.dy

        screen.blit(self.current_image,(600,self.y))
    
    def keys(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and self.MOVING:
            self.dy -= 2 
            print("pass")
        
        if key[pygame.K_DOWN] and self.y <= 500 and self.MOVING:
            self.dy += 2
        
        


    
    def animate_bird(self):
        now = pygame.time.get_ticks()

        if (now - self.last_updated) > 40:
            self.last_updated = now
            self.current_frame = (self.current_frame + 1) % len(self.birdList)

            if self.state == "playing":
                self.current_image = self.birdList[self.current_frame]
            











FlappyBird()   