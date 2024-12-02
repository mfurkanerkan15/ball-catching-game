import pygame
import random

pygame.init()
pencere=pygame.display.set_mode((600,650))

skor=0
skor2=0
hız=10
FPS=30
saat=pygame.time.Clock()

#arka plan
arka_plan=pygame.image.load("Images/background_image.jpg")

#messi ve ballon dor
messi=pygame.image.load("Images/messi.png")
messi_koordinat=messi.get_rect()
messi_koordinat.topleft=(600-37,75)

ballon_dor=pygame.image.load("Images/ballon-dor.png")
ballon_dor_koordinat=ballon_dor.get_rect()
ballon_dor_koordinat.center=(300,420)

ronaldo=pygame.image.load("Images/ronaldo.png")
ronaldo_koordinat=ronaldo.get_rect()
ronaldo_koordinat.topleft=(5,75)

#sesler
ses=pygame.mixer.music.load("Sounds/8bit_sound.mp3")
pygame.mixer.music.play(-1,0.0)
kemirawowo=pygame.mixer.Sound("Sounds/messi wowo.mp3")
suii=pygame.mixer.Sound("Sounds/ronaldo suii.mp3")

#yazı ayarları
font_ismi=pygame.font.SysFont("consolas",40)
font_ismi2=pygame.font.SysFont("consolas",40)
font_bitis=pygame.font.SysFont("consolas",35)

def yeniden_basla():
    global hız, skor, skor2 
    hız=10
    skor=0
    skor2=0
    ronaldo_koordinat.topleft=(5,75)
    messi_koordinat.topleft=(600-37,75)
    ballon_dor_koordinat.center=(300,420)


durum=True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False
        elif etkinlik.type==pygame.KEYDOWN:
            if etkinlik.key==pygame.K_r:
                yeniden_basla()

    yazı=font_ismi.render("MESSİ:"+str(skor),True,(220,0,0),(20,20,20))
    yazı_koordinat=yazı.get_rect()
    yazı_koordinat.topleft=(405,15)
    yazı2=font_ismi2.render("RONALDO:"+str(skor2),True,(220,0,0),(20,20,20))
    yazı2_koordinat=yazı.get_rect()
    yazı2_koordinat.topleft=(20,15)
    
    pencere.blit(arka_plan,(0,0))
    pencere.blit(yazı,yazı_koordinat)
    pencere.blit(yazı2,yazı2_koordinat)
    pygame.draw.line(pencere,(100,0,0),(0,70),(600,70),3)
    pencere.blit(ballon_dor,ballon_dor_koordinat)
    pencere.blit(messi,messi_koordinat)
    pencere.blit(ronaldo,ronaldo_koordinat)

    if skor<10 and skor2<10:
        tus=pygame.key.get_pressed()
        if tus[pygame.K_LEFT] and messi_koordinat.left>0:
            messi_koordinat.x-=hız
        elif tus[pygame.K_RIGHT] and messi_koordinat.right<600:
            messi_koordinat.x+=hız
        elif tus[pygame.K_DOWN] and messi_koordinat.bottom<645:
            messi_koordinat.y+=hız
        elif tus[pygame.K_UP] and messi_koordinat.top>70:
            messi_koordinat.y-=hız

        dugme=pygame.key.get_pressed()
        if dugme[pygame.K_a] and ronaldo_koordinat.left>0:
            ronaldo_koordinat.x-=hız
        elif dugme[pygame.K_d] and ronaldo_koordinat.right<600:
            ronaldo_koordinat.x+=hız
        elif dugme[pygame.K_s] and ronaldo_koordinat.bottom<645:
            ronaldo_koordinat.y+=hız
        elif dugme[pygame.K_w] and ronaldo_koordinat.top>70:
            ronaldo_koordinat.y-=hız

    if messi_koordinat.colliderect(ballon_dor_koordinat):
        ballon_dor_koordinat.x=random.randint(0,600-32)
        ballon_dor_koordinat.y=random.randint(71,650-32)
        skor+=1
        kemirawowo.play()    

    if ronaldo_koordinat.colliderect(ballon_dor_koordinat):
        ballon_dor_koordinat.x=random.randint(0,600-32)
        ballon_dor_koordinat.y=random.randint(71,650-32)
        suii.play()
        skor2+=1
 
    kazanan=""
    if skor>=10:
        kazanan="MESSİ"
    elif skor2>=10:
        kazanan="RONALDO"    

    bitis_yazısı=font_bitis.render(f"OYUN BİTTİ, {kazanan} KAZANDI!",True,(220,0,0),(255,255,255))
    bitis_yazısı_koordinat=bitis_yazısı.get_rect()
    bitis_yazısı_koordinat.center=(300,300)    

    if skor==10 or skor2==10:
        pencere.blit(bitis_yazısı,bitis_yazısı_koordinat)

    pygame.display.update()
    saat.tick(FPS)

pygame.quit()