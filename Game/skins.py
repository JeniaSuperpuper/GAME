import pygame

screen = pygame.display.set_mode((950, 555))



skins = {
    'base_dog': (
        [
            pygame.image.load('img/right/r1.png').convert_alpha(),
            pygame.image.load('img/right/r2.png').convert_alpha(),
            pygame.image.load('img/right/r3.png').convert_alpha(),
            pygame.image.load('img/right/r4.png').convert_alpha(),
        ],
        [
            pygame.image.load('img/left/l1.png').convert_alpha(),
            pygame.image.load('img/left/l2.png').convert_alpha(),
            pygame.image.load('img/left/l3.png').convert_alpha(),
            pygame.image.load('img/left/l4.png').convert_alpha(),
        ]
    ),

    'white_dog': (
        [
            pygame.image.load('img/skins/white_dog/right/skin1_R1.png').convert_alpha(),
            pygame.image.load('img/skins/white_dog/right/skin1_R2.png').convert_alpha(),
            pygame.image.load('img/skins/white_dog/right/skin1_R3.png').convert_alpha(),
            pygame.image.load('img/skins/white_dog/right/skin1_R4.png').convert_alpha(),
        ],
        [
            pygame.image.load('img/skins/white_dog/left/skin1_L1.png').convert_alpha(),
            pygame.image.load('img/skins/white_dog/left/skin1_L2.png').convert_alpha(),
            pygame.image.load('img/skins/white_dog/left/skin1_L3.png').convert_alpha(),
            pygame.image.load('img/skins/white_dog/left/skin1_L4.png').convert_alpha(),
        ]
    )
}
