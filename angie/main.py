# evelyn.angie.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv

BARBIE = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwidoZGyppLdAhXTqZAKHYuBCPYQjRx6BAgBEAU&url=https%3A%2F%2Fwww.rihappy.com.br%2Fboneca-barbie-bailarina-loira-mattel%2Fp&psig=AOvVaw0rtI5FgIugI-rEqk1LoZPD&ust=1535633292299503"
FLORESTA = "https://www.google.com.br/imgres?imgurl=http%3A%2F%2Fwww.litury.com%2Fwp-content%2Fuploads%2F2017%2F12%2Fsombre-fond-d-ecran-hd.jpg&imgrefurl=http%3A%2F%2Fwww.difdifi.com%2Ffond-ecran-sombre%2Fsombre-fonds-d-39-ecran.html&docid=TmXXXnvtP_DcJM&tbnid=8QBA-c6iNDhKYM%3A&vet=10ahUKEwisgYKJp5LdAhWITZAKHfLHBpcQMwiVASgBMAE..i&w=1440&h=900&itg=1&safe=strict&bih=662&biw=1366&q=floresta%20fundo&ved=0ahUKEwisgYKJp5LdAhWITZAKHfLHBpcQMwiVASgBMAE&iact=mrc&uact=8"
TARZAN = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjfhfDYp5LdAhUDI5AKHTNoDFoQjRx6BAgBEAU&url=http%3A%2F%2Fvsdebating.wikia.com%2Fwiki%2FTarzan_(Disney)&psig=AOvVaw3N3AmgwwSndi1yDrWDerwj&ust=1535633667279982"
HOMEM_ARANHA = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiZjs38p5LdAhVEF5AKHY6ICK8QjRx6BAgBEAU&url=https%3A%2F%2Fwww.impaktovisual.com.br%2Fhomem-aranha-%2F7009-display-homem-aranha.html&psig=AOvVaw183OAvPWYcvmktJRnkuiKB&ust=1535633804494163"
CIDADE = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwilmPrYqJLdAhXFFpAKHZPOB3MQjRx6BAgBEAU&url=https%3A%2F%2Fpt.depositphotos.com%2F78304622%2Fstock-photo-the-central-park.html&psig=AOvVaw2LYDmac_O_MvFtc7rrveES&ust=1535633989036610"
CINDERELA = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwietp6OqZLdAhWDFpAKHUd2DLsQjRx6BAgBEAU&url=http%3A%2F%2Foliveirafashionando.blogspot.com%2F2016%2F11%2Fcinderela-png.html&psig=AOvVaw3_7DY1D6lzhJPvG58B-aKo&ust=1535634077959445"
ALICE = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiw3fSsqZLdAhUDIJAKHYx2BMsQjRx6BAgBEAU&url=http%3A%2F%2Ftvnewsclips.info%2Fpages%2Fd%2Fdisney-png-files-16%2F&psig=AOvVaw2cLEAGupwu0ztt3W_KStDe&ust=1535634188075739"
CASTELO = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwio9PPLqZLdAhWDS5AKHX6rAMsQjRx6BAgBEAU&url=https%3A%2F%2Fwww.elo7.com.br%2Fpainel-castelo-com-flores-x2-8m%2Fdp%2FA9C711&psig=AOvVaw0xLHxXxPSpF-CZHzmMXsHS&ust=1535634243209969"
YODA = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjOutjvqZLdAhVLhpAKHcFWDUQQjRx6BAgBEAU&url=http%3A%2F%2Fpgnsmundo.blogspot.com%2F2016%2F06%2Fpng-yoda.html&psig=AOvVaw1d7YpX7yyXQWtXOsPq8FMM&ust=1535634316808987"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    cidade = Cena(img=CIDADE)
    floresta.direita = cidade
    
    
    barbie = Elemento(img=BARBIE,tit="Barbie", style=dict(left="100px", top="160px", width="60px", height="200px"))
    barbie.entra(floresta)
    ebarbie = Texto (floresta, "Que floresta feia")
    barbie.vai = ebarbie.vai
    
    castelo = Cena(img=CASTELO)
    cidade.direita = castelo
    
    tarzan = Elemento(img=TARZAN,tit="Tarzan", style=dict(left="100px", top="160px", width="60px", height="200px"))
    tarzan.entra(floresta)
    etarzan = Texto (floresta, "Olá!!!!")
    tarzan.vai = etarzan.vai
    
    homem_aranha = Elemento(img=HOMEM_ARANHA,tit="homem_aranha", style=dict(left="100px", top="160px", width="60px", height="200px"))
    homem_aranha.entra(cidade)
    ehomem_aranha = Texto (cidade, "o que que ta acontecendo aqui bb?")
    homem_aranha.vai = ehomem_aranha.vai
    
    cinderela = Elemento(img=CINDERELA,tit="cinderela", style=dict(left="100px", top="160px", width="60px", height="200px"))
    cinderela.entra(cidade)
    ecinderela = Texto (cidade, "A BARBIE SO FAZ BESTEIRINHAAAAA SOS")
    cinderela.vai = ecinderela.vai
    
    alice = Elemento(img=ALICE,tit="Alice", style=dict(left="100px", top="160px", width="60px", height="200px"))
    alice.entra(castelo)
    ealice = Texto (castelo, "Vou ter que interromper meu momento de descanso, triste")
    alice.vai = ealice.vai
    
    yoda = Elemento(img=YODA,tit="Yoda", style=dict(left="100px", top="160px", width="60px", height="200px"))
    yoda.entra(castelo)
    eyoda = Texto (castelo, "SEMPRE SOBRA PARA MIM!!!!")
    yoda.vai = eyoda.vai
    

   floresta.vai()
criarcenas()