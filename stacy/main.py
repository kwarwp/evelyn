# evelyn.stacy.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv

ALICE ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjllMvasZLdAhWBxpAKHYALBP4QjRx6BAgBEAU&url=http%3A%2F%2Ftatycasarino.blogspot.com%2F2016%2F06%2F&psig=AOvVaw39ug6JEo1KVFHlwO6ANPFt&ust=1535636245345380"
TARZAN ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiL6qncppLdAhXCH5AKHZAyBUMQjRx6BAgBEAU&url=http%3A%2F%2Fhero.wikia.com%2Fwiki%2FFile%3ATarzan_Character.png&psig=AOvVaw2Frm4u_vk1-RCkiipJI9_5&ust=1535633480343303"
FLORESTA ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwiCzvyAq5LdAhXBFJAKHeuDBh8QjRx6BAgBEAU&url=https%3A%2F%2Falgarve-saibamais.blogspot.com%2F2016%2F03%2Fcomo-o-vento-na-floresta-poema-de.html&psig=AOvVaw392PmZLmsaLorhggTmv0pB&ust=1535634513603880"
CASTELO ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjdwPnPq5LdAhVGmJAKHUF6BQ0QjRx6BAgBEAU&url=http%3A%2F%2Fwww.fazarte.com.br%2Fhome%2Fproduto%2F60-Castelo-Da-Floresta.html&psig=AOvVaw1JIb2JL8P5HQ8KN0n-ZF1h&ust=1535634776117423"
PIANO ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi2sMu_sJLdAhVEFJAKHUOmDeoQjRx6BAgBEAU&url=http%3A%2F%2Fescolademusicalumiere.blogspot.com%2Fp%2Fcursos.html&psig=AOvVaw0MVfMyD7JnHHYzMU9nzCv-&ust=1535636086717191"
BEIJO ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj75eOfsZLdAhUIipAKHVb4AjkQjRx6BAgBEAU&url=http%3A%2F%2Farimaamtricaapoesia.blogspot.com%2F&psig=AOvVaw0y0toAjNn_zRqdMviDkuyV&ust=1535636286353318"
FIM = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwivw4acuJLdAhUFjpAKHUB3DesQjRx6BAgBEAU&url=http%3A%2F%2Fmagnitudesdomundo.blogspot.com%2F2013%2F06%2Fdia-dos-namorados-12-de-junho.html&psig=AOvVaw04zkigDpwUyOfML9dxkeyn&ust=1535638097834402"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    castelo = Cena(img=CASTELO)
    floresta.direita = castelo
    
    alice = Elemento(img=ALICE, tit="Alice", style=dict(left="100px",top="160",width="60px",heigth="200px"))
    alice.entra(floresta)
    ealice = Texto(floresta, "Alice passeava pela floresta e, de repente,deparou-se com um lindo castelo.")
    alice.vai = ealice.vai
    
    alice = Elemento(img=ALICE, tit="Alice", style=dict(left="100px",top="160",width="60px",heigth="200px"))
    alice.entra(castelo)
    ealice = Texto(castelo, "Oh, que lindo! Quem será que mora aqui?")
    alice.vai = ealice.vai    
    
    piano = Elemento(img=PIANO, tit="Alice", style=dict(left="100px",top="160",width="60px",heigth="200px"))
    piano.entra(castelo)
    epiano = Texto(castelo, "O piano é mágico e toca uma linda valsa!")
    piano.vai = epiano.vai
    
    tarzan = Elemento(img=TARZAN, tit="Tarzan", style=dict(left="100px",top="160",width="60px",heigth="200px"))
    tarzan.entra(castelo)
    tarzan = Texto(castelo, "Surge um lindo príncipe que tira Alice para dançar...")
    tarzan.vai = etarzan.vai
    
    beijo = Elemento(img=BEIJO, tit="Beijo", style=dict(left="100px",top="160",width="60px",heigth="200px"))
    beijo.entra(castelo)
    beijo = Texto(castelo, "Os dois se apaixonam e...")
    beijo.vai = ebeijo.vai
    
    fim = Elemento(img=FIM, tit="Fim", style=dict(left="100px",top="160",width="60px",heigth="200px"))
    fim.entra(castelo)
    fim.vai = efim.vai
    
    