import pygame as py
from pygame.locals import *
from sys import exit
from random import *
from spritesheet import SpriteSheet, Origin

py.init()

musica_intro = py.mixer.Sound('BoxCat Games - Defeat.mp3')
musica_intro.set_volume(0.3)

py.mixer.music.set_volume(0)
musica_fundo = py.mixer_music.load('audiofinalizado.mp3')
py.mixer_music.play(-1)

musica_morte = py.mixer.Sound('audiomorte.mp3')
musica_morte.set_volume(0.3)

musica_colisao = py.mixer.Sound('explosion-6055.mp3')
musica_colisao.set_volume(0.2)

#Configutações iniciais da tela
largura = 1280
altura = 768

#Configurações da nave
referencia_x = largura // 2
referencia_y = altura - 120

#Criação da tela inicial
tela = py.display.set_mode((largura, altura))
fonte = py.font.SysFont("Arial", 20, True, False)
pontos = 0
py.display.set_caption("SPACE-Z")
relogio = py.time.Clock()

#Quando o usuário morre
def reiniciar_jogo():
    global pontos, xnave, ynave, xasteroide, xasteroide2, yasteroide, yasteroide2, asteroide_rect, asteroide2_rect, asteroide_mask, asteroide2_mask, morte, jogo_ativo, fim_de_jogo, reiniciamento
    pontos = 0
    xnave = (largura//2)
    ynave = (altura//2 + 320)
    xasteroide = randint(16, 1024)
    xasteroide2 = randint(16, 1024)
    yasteroide = -30
    yasteroide2 = -30
    asteroide_rect.topleft = (xasteroide, yasteroide)
    asteroide2_rect.topleft = (xasteroide2, yasteroide2)
    asteroide_mask = py.mask.from_surface(asteroide)
    asteroide2_mask = py.mask.from_surface(asteroide2)
    py.mixer.music.set_volume(1)
    py.mixer.music.play(start=0.0)
    musica_morte.stop()
    morte = False
    jogo_ativo = True
    fim_de_jogo = False
    reiniciamento = 0

#Contador que inicia para retornar para o início do jogo
reiniciamento = 0

#Quando o usuário passa os Asteroides
def ganhou_jogo():
    global codigofinal, texto_formatado6, reiniciamento
    codigofinal = f'Seu código é:{win}'
    texto_formatado6 = fonte6.render(codigofinal, False, (0, 255, 0))
    tela.blit(texto_formatado6, (largura//2 - 160, altura//2))
    reiniciamento = reiniciamento + 1
    if reiniciamento >= 14000:
        reiniciar_tudo()

#Aqui é a def responsável por retornar o game para o início
def reiniciar_tudo():
    global reiniciamento, start, pontos
    reiniciar_jogo()
    py.mixer.music.set_volume(0)
    reiniciamento = 0
    start = True
    pontos = 0
    return

# Primeiro asteroide
xasteroide = randint(16, 1020)
yasteroide = -30
asteroide = py.image.load('AsteroideOficial.png').convert_alpha()
asteroide_mask = py.mask.from_surface(asteroide)
asteroide_rect = asteroide.get_rect(center=(xasteroide, yasteroide))

# Segundo asteroide
xasteroide2 = randint(20, 1000)
yasteroide2 = -30
asteroide2 = py.image.load('AsteroideOficial.png').convert_alpha()
asteroide2_mask = py.mask.from_surface(asteroide2)
asteroide2_rect = asteroide2.get_rect(center=(xasteroide2, yasteroide2))

#Velocidade da nave e do asteroide
velocidadeasteroide = 3
vadd = 0.1
velocidadanave = 3.2

#Criação da nave
nave = py.image.load('spaceship.png').convert_alpha()
nave_mask = py.mask.from_surface(nave)
nave_rect = nave.get_rect(center=(referencia_x, referencia_y))

#É o plano de fundo durante o game
animacao = SpriteSheet("imgfinalizada.png", 5, 2)
qntframes = animacao.sprite_count() - 1
frameatt = 0
vframeatt = 0.063

#É a tela de instrução antes de iniciar o game
inst = SpriteSheet("inst.png", 3, 1)
qntframesinst = inst.sprite_count() - 1
frameattinst = 0
vframeattinst = 0.0063

#Aqui é quando a pessoa consegue concluir seu objetivo
telafinal = SpriteSheet('imgf2.png', 5, 2)
qntframefinal = telafinal.sprite_count() - 1
framefinal = 0
vframefinal = 0.063

#É o desenho da nave na tela
nave = py.image.load('spaceship.png').convert_alpha()
nave_mask = py.mask.from_surface(nave)
nave_rect = nave.get_rect(center=(largura // 2, altura // 2 + 340))

#Configurações da localização da nave (hitbox)
xnave, ynave = nave_rect.topleft

#Frase de início
imagem_inicio = py.image.load('tro.png')
imagem_transformada = py.transform.scale(imagem_inicio, (largura, altura))
telainicio = SpriteSheet("fraseinicial.png", 2, 1)
inicioframes = telainicio.sprite_count() - 0.01
inicioatt = 0
vinicioatt = 0.005

#Imagem da caveira na morte
telamorte = SpriteSheet("kill5.png", 7, 3)
morteframes = telamorte.sprite_count() - 1
morteatt = 0
vmorteatt = 0.04

#Fontes de texto
fonte2 = py.font.Font('Press_Start_2P/PressStart2P-Regular.ttf', 30)
fonte3 = py.font.Font('Press_Start_2P/PressStart2P-Regular.ttf', 13)
fonte4 = py.font.Font('Press_Start_2P/PressStart2P-Regular.ttf', 15)
fonte5 = py.font.Font('Press_Start_2P/PressStart2P-Regular.ttf', 12)
fonte6 = py.font.Font('Press_Start_2P/PressStart2P-Regular.ttf', 20)
fonte7 = py.font.Font('Press_Start_2P/PressStart2P-Regular.ttf', 17)

#Frase de morte
frasemorte = SpriteSheet("frasekill.png", 2, 1)
frasemorteframes = frasemorte.sprite_count() - 0.01
frasemorteatt = 0
vfrasemorteatt = 0.005

#Códigos que aparecem quando o usuário vence
codigowin = ['00LKH', '2ASD9', '9OOQM']
numcod = randint(0, 2)
win = (codigowin[numcod])

#Operadores lógicos que utilizei para parar a geração de asteroides quando o usuário vence
jogo_ativo = True
fim_de_jogo = False

#Definimos quanto tempo o jogo irá durar (quantidade de asteroides que o usuário deve ultrapassar)
tempojogo = 30

#Contador que utilizei para dar a impressão de "carregamento do jogo" na instrução
carregamento = 0

while True:
    relogio.tick(200)
    musica_intro.play()

    tela.blit(imagem_transformada, (0, 0))

    mensagem_inicio = fonte2.render('SPACE-Z', True, (255, 255, 255))
    start = True
    controlenave = False
    frase = True
    instrucao = False

    while start:
        controlenave = True
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_c:
                    instrucao = True
                    
        if frase == True:
            tela.blit(mensagem_inicio, (largura//2 - 90, altura//2 - 40))
            py.display.update()

            if inicioatt >= inicioframes:
                inicioatt = 0
            else:
                inicioatt += vinicioatt
            telainicio.blit(tela, int(inicioatt), (largura/2 + 10, altura/2 + 5), Origin.Center)


        while instrucao:
            for event in py.event.get():
                if event.type == QUIT:
                    py.quit()
                    exit()
            if frameattinst >= qntframesinst:
                frameattinst = 0
                carregamento = carregamento + 1
            else:
                frameattinst = frameattinst + vframeattinst
            inst.blit(tela, int(frameattinst), (largura/2, altura/2), Origin.Center)
            frase = False
            py.display.update()
            py.mixer.music.play(start=0.0)
            if carregamento >= 10:
                start = False
                instrucao = False

    while start == False:
        py.mixer.music.set_volume(1)
        musica_intro.stop()
        pontuacao = f'Pontos:{pontos}'
        texto_formatado = fonte5.render(pontuacao, False, (255, 255, 255))
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                exit()
        nave_rect.topleft = (xnave, ynave)

        offset = (nave_rect.left - asteroide_rect.left, nave_rect.top - asteroide_rect.top)
        result = asteroide_mask.overlap(nave_mask, offset)

        offset2 = (nave_rect.left - asteroide2_rect.left, nave_rect.top - asteroide2_rect.top)
        result2 = asteroide2_mask.overlap(nave_mask, offset2)

        if frameatt >= qntframes:
            frameatt = 0
        else:
            frameatt = frameatt + vframeatt
        animacao.blit(tela, int(frameatt), (largura/2, altura/2), Origin.Center)


        if controlenave == True:
            keys = py.key.get_pressed()
            if keys[py.K_a]:
                xnave -= velocidadanave
            if keys[py.K_d]:
                xnave += velocidadanave

        if jogo_ativo:
            tela.blit(asteroide, asteroide_rect.topleft)

            if pontos < 4:
                yasteroide += velocidadeasteroide
                asteroide_rect.y = yasteroide
                if yasteroide >= (altura + 220):
                    pontos += 1
                    xasteroide = randint(16, 1246)
                    yasteroide = -30
                    asteroide_rect.topleft = (xasteroide, yasteroide)
                    asteroide_mask = py.mask.from_surface(asteroide)

            if pontos >= 4:
                yasteroide += velocidadeasteroide
                asteroide_rect.y = yasteroide
                if yasteroide >= (altura + 220):
                    pontos += 1
                    xasteroide = randint(16, 585)
                    yasteroide = -30
                    asteroide_rect.topleft = (xasteroide, yasteroide)
                    asteroide_mask = py.mask.from_surface(asteroide)

                yasteroide2 += velocidadeasteroide + vadd
                asteroide2_rect.y = yasteroide2

                if yasteroide2 >= (altura + 220):
                    pontos += 1
                    xasteroide2 = randint(635, 1246)
                    yasteroide2 = -30
                    asteroide2_rect.topleft = (xasteroide2, yasteroide2)
                    asteroide2_mask = py.mask.from_surface(asteroide2)

                tela.blit(asteroide2, asteroide2_rect.topleft)

            tela.blit(nave, nave_rect.topleft)

            if (result) or (result2):
                py.mixer.music.set_volume(0)
                mensagem_morte = 'Um asteroide atingiu você!'
                texto_formatado = fonte3.render(mensagem_morte, True, (255, 255, 255))
                ret_texto = texto_formatado.get_rect()
                musica_colisao.play()
                musica_morte.play()
                morte = True
                while morte:
                    tela.fill((0, 0, 0))
                    for event in py.event.get():
                        if event.type == QUIT:
                            py.quit()
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_r:
                                reiniciar_jogo()

                    ret_texto.center = ((largura // 2 + 7.4), (altura // 2 + 7))
                    tela.blit(texto_formatado, ret_texto)
                    if morteatt >= morteframes:
                        morteatt = 0
                    else:
                        morteatt += vmorteatt
                    telamorte.blit(tela, int(morteatt), ((largura//2), (altura//2 - 55)), Origin.Center)

                    if frasemorteatt >= frasemorteframes:
                        frasemorteatt = 0
                    else:
                        frasemorteatt += vfrasemorteatt
                    frasemorte.blit(tela, int(frasemorteatt), ((largura//2 + 5), altura//2 + 33), Origin.Center)

                    py.display.update()

        if pontos >= tempojogo and not fim_de_jogo:
            jogo_ativo = False
            fim_de_jogo = True

# Aqui colocamos novamente a def reiniciar_jogo justamente pois tem chances da nave pegar em algum dos asteroides mesmo após o jogo "acabar"
        if fim_de_jogo:
            tela.blit(nave, nave_rect.topleft)
            offset = (nave_rect.left - asteroide_rect.left, nave_rect.top - asteroide_rect.top)
            result = asteroide_mask.overlap(nave_mask, offset)

            offset2 = (nave_rect.left - asteroide2_rect.left, nave_rect.top - asteroide2_rect.top)
            result2 = asteroide2_mask.overlap(nave_mask, offset2)

            if (result) or (result2):
                py.mixer.music.set_volume(0)
                mensagem_morte = 'Um asteroide atingiu você!'
                texto_formatado = fonte3.render(mensagem_morte, True, (255, 255, 255))
                ret_texto = texto_formatado.get_rect()
                musica_colisao.play()
                musica_morte.play()
                morte = True
                while morte:
                    tela.fill((0, 0, 0))
                    for event in py.event.get():
                        if event.type == QUIT:
                            py.quit()
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_r:
                                reiniciar_jogo()

                    ret_texto.center = ((largura // 2 + 7.4), (altura // 2 + 7))
                    tela.blit(texto_formatado, ret_texto)
                    if morteatt >= morteframes:
                        morteatt = 0
                    else:
                        morteatt += vmorteatt
                    telamorte.blit(tela, int(morteatt), ((largura//2), (altura//2 - 55)), Origin.Center)

                    if frasemorteatt >= frasemorteframes:
                        frasemorteatt = 0
                    else:
                        frasemorteatt += vfrasemorteatt
                    frasemorte.blit(tela, int(frasemorteatt), ((largura//2 + 5), altura//2 + 33), Origin.Center)

                    py.display.update()
            
            if yasteroide < altura:
                yasteroide += velocidadeasteroide
                asteroide_rect.y = yasteroide
                tela.blit(asteroide, asteroide_rect.topleft)
            
            if yasteroide2 < altura:
                yasteroide2 += velocidadeasteroide + vadd
                asteroide2_rect.y = yasteroide2
                tela.blit(asteroide2, asteroide2_rect.topleft)
            
            if yasteroide >= altura and yasteroide2 >= altura:
                controlenave = False
                ynave -= 1.5


        if ynave < -10:
            if framefinal >= qntframefinal:
                framefinal = 0
            else:
                framefinal = framefinal + vframefinal
            telafinal.blit(tela, int(framefinal), (largura/2, altura/2), Origin.Center)

            mensagem_venceu = "Parabéns, você conseguiu sobreviver aos asteroides!"
            texto_formatado7 = fonte7.render(mensagem_venceu, True, (255, 255, 0))
            ret_texto7 = texto_formatado7.get_rect()
            ret_texto7.center = ((largura // 2 + 7.4), (altura // 2 - 37))
            tela.blit(texto_formatado7, ret_texto7)

        if ynave < -1500:
            ganhou_jogo()

        if xnave > largura:
            xnave = 0
        if xnave < 0:
            xnave = largura

        if pontos < tempojogo:    
            tela.blit(texto_formatado, (1170, 742))
        
        py.display.update()