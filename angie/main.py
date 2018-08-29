# evelyn.angie.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv

ALICE = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiqj6zWppLdAhWCQ5AKHdDxCCEQjRx6BAgBEAU&url=http%3A%2F%2Ffr.fanpop.com%2Fclubs%2Frainbow-unicorn%2Fimages%2F40444811%2Ftitle%2Falice-wonderland-png-photo&psig=AOvVaw1l0pAoI5HPWAvok2IzFMBh&ust=1535633460708667"
BARBIE = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi22O31ppLdAhXEFpAKHWcaDFQQjRx6BAgBEAU&url=https%3A%2F%2Fwww.amazon.com%2FHallmark-Keepsake-African-American-Christmas-Ornament%2Fdp%2FB01N7XPBL3&psig=AOvVaw2a0DZiumyZ5hmfBz3xvGNV&ust=1535633535702570"
FLORESTA = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiH5JKsp5LdAhXFCpAKHXCdAToQjRx6BAgBEAU&url=https%3A%2F%2Fwww.katebackdrop.co.uk%2Fproducts%2Fkate-fantasy-deep-forest-sunshine-backdrops-for-photography-uk&psig=AOvVaw3AZNaaQ7DkqXY21y0CbHsH&ust=1535633623819310"
TARZAN = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwitx6Php5LdAhUDxpAKHdewD7kQjRx6BAgBEAU&url=http%3A%2F%2Fvsdebating.wikia.com%2Fwiki%2FTarzan_(Disney)&psig=AOvVaw0ocSzWatxiPr8QFrZepB39&ust=1535633777072388"
YODA = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi9z7j-p5LdAhVJkJAKHWeMDoYQjRx6BAgBEAU&url=http%3A%2F%2F123emoji.com%2Fpt%2Fstar-wars-yoda-collection-2311%2F&psig=AOvVaw2Mu-oZ7FbQlgm8g5nUJP9J&ust=1535633826946663"
HOMEM_ARANHA = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjbyvGeqJLdAhVLgZAKHYmIB0UQjRx6BAgBEAU&url=http%3A%2F%2Fqueroimagem.blogspot.com%2F2011%2F12%2Fhomem-aranha.html&psig=AOvVaw2NqNsliTqDVC0VZJxRPMCp&ust=1535633900937456"
CASTELO = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj_3bLAqJLdAhXEIZAKHbOSC3kQjRx6BAgBEAU&url=https%3A%2F%2Fwww.elo7.com.br%2Fpainel-de-festa-castelo-encantado-rosas-200x150-cm%2Fdp%2FBFB4D8&psig=AOvVaw1JN3b6DZFqIB0li0Lm5A7m&ust=1535633942571352V"
CENTRAL = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjO0YjaqJLdAhXQnJAKHU-zAQkQjRx6BAgBEAU&url=http%3A%2F%2Fomeupomar.blogspot.com%2F2013%2F06%2F&psig=AOvVaw3OC5Ek4zOzlyJbjxddlNAT&ust=1535634014514734"
CINDERELA = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwittbrzqJLdAhVElZAKHfw3CrYQjRx6BAgBEAU&url=http%3A%2F%2Foliveirafashionando.blogspot.com%2F2016%2F11%2Fcinderela-png.html&psig=AOvVaw3ETNLj9exlLe_agRWkv_A3&ust=1535634069400788"

def criarcenas():
    floresta = Cena(img=FLORESTA) 
    central = Cena(img=CENTRAL)
    floresta.direita = CENTRAL
    
    barbie = Elemento(img=BARBIE, tit="BARBIE", style=dict(left="100px", top="160px", width="60px", height="200 
    barbie.entra(floresta)
    ebarbie = Texto (floresta, "Que floresta assustadora minha gente")
    barbie.vai = ebarbie.vai
    
    castelo = Cena(img=CASTELO)
    central.direita = castelo
    
    Alice = Elemento(img=Alice, tit="BARBIE", style=dict(left="100px", top="160px", width="60px", height="200 
    alice.entra(castelo)
    ealice = Texto (castelo, "o que houve querida?")
    alice.vai = ealice.vai
    
    
    floresta.vai()
criarcenas()
    
    
