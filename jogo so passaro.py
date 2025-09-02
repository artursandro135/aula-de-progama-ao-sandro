import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CAMO = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))  
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png"))) 
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png"))) 
IMAGEM_PASSARO = [
  pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))),
  pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))),
  pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))
]
pygame.font.init()
FORNTE_PONTOS = pygame.font.SysFont('arial', 50)
class passaro:
        IMGS = IMAGEM_PASSARO
    #ANIMAÇAO DA ROTAÇAo
rotacao_maxima = 25
velocidade_rotacao =20
tempo_animacao = 5
def__init__(self,x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0 
        self.contagem_imagem = 0
        self.imagem = self.imgs[0]
def pular(self)
      self.velocidade = -10.5
      self.tempo = 0
      self.altura = self.y
def mover(self):
      #calcula o deslocamento
      self>tempo += 1
      deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

      #retringir o deslocamento
      if deslocamento > 16:
            deslocamento = 16
      elif deslocamento < 0:
            deslocamento -= 2
        self.y = deslocamento
      #angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                 self.angulo -= self.velocidade_rotacao
    def desenhar(self, tela):
     #definir qual imadem do passaro vai aparecer
      self.contagem_imagem < self.tempo_animacao:

       if self.contagem_imagem < self.tempo_animacao:
           self.imagem = self.imgs[0]
       elif self.contagem_imagem < self.tmpo_animacao*2:
           self.imagem = self.imgs[1]
       elif self.contagem_imagem < self.tmpo_animacao*3:
           self.imagem = self.imgs[2]
       elif self.contagem_imagem < self.tmpo_animacao*4:
           self.imagem = self.imgs[1]
       elif self.contagem_imagem < self.tmpo_animacao*4 + 1:
           self.imagem = self.imgs[0]
           self.contagem_imagem = 0
        #se o passaro estiver caindo, nao bater as asas
        if self.angulo <= -80:
           self.imagem = self.imgs[1]
           self.comtagem_imagem = self.tempo_animecao*2
        #desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(toplef=(self.x, self.y)).conter
      retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
      tela.blit(imagem_rotacionada, retangulo.topleft)
      def get_mask(self):
           return pygame.mask.from_surface(self.imagem)
class cano:
    distancia = 200
    velocidde = 5
    def __init__(self, x):
         self.x = x
         self.altura = 0
         self.pos_topo = 0
         self.pos_base = 0 
         self.cano_topo = IMAGEM_CAMO
         self.cano_base = pygame.transform.flip(imagem_cano, false, True)
         self.passou = False
         self.definir_altura()
    def definir_altura(self):
         self.altura = random.randrange(50, 450)
         self.pos_base = self.altura - self.cano_topo.get_height()
         self.pos_topo = self.altura + self.distancia

         def mover(self):
              self.x -= self.velocidade


         def desenhar(self, tela):
             tela.blit(self.cano_topo, (self.x, self.pos_topo))
             tela.blit(self.cano_base, (self.x, self.pos_base))
         def colidir(self, passaro):
              passaro_mask = passaro.get_mask()
              topo_mask = pygame.mask.from_surface(self.cano_topo)
              base_mask = pygame.mask.from_surface(self.cano_base)

              distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
              distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

              topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
              base_ponto = passaro_mask.overlap(topo_mask, distancia_base)

              if base_ponto or topo_ponto:
                   return True
              else:
                   return False

class chao:
     velocidade = 5
     LARGURA = IMAGEM_CHAO.get_width()
     IMAGEM = IMAGEM_CHAO

        def __init__(self, y):
          self.y = y
          self.x1 = 0
          self.x2 = self.LARGURA
        def movere(self):
          self.x1 -= self.velocidade
          self.x2 -= self.velocidade

          if self.x1 + self.LARGURA < 0:
              self.x1 = self.x1 + self.LARGURA
          if self.x2 = self.largura < 0:
              self.x2 = self.x2 + self.LARGURA
        def desenhar(self, tela):
         tela.blit(self.imagem, (self.x1, self.y))
         tela.blit(self.imagem, (self.x2, self.y))

def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0,0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela) 
        pygame.display.update()
def main():
    Passaros = [passaro(230, 350)]
    chao = chao(730)
    canos = [cano(700)]
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()

    #loop do jogo
    rodando = True
    while rodando:
        relogio.tick(30)
        #interaçao com o usuario
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False 
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame. K_SPACE:
                    for passaro in passaros:
                        passaro.pular()
    #mover as coisas 
    for passaro in passaros:
        passaro.mover()
    chao.mover()
    
    adicionar_cano = False 
    remover_canos = []
    for cano in canos:
        for i, passaro in enumerate(passaros):
            if cano.colidir(passaro):
              passaro.pop(i)
            if not cano.passau and passaro.x > cano.x:
                cano.passaou = True
                adicionar_cano = True
        cano.mover()
        if cano.x + cano.Cano_topo.get_width() < 0:
            remover_canos.append(cano)
    if adicionar_cano:
        pontos += 1
        canos.append(Cano(600))
    for cano in remover_canos:
        canos.remove(cano)
    for i, passaro in enumerate(Passaros):
        if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
            passa