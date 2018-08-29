# evelyn.stacy.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv

ALICE ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj9sKDTqJLdAhVFh5AKHf9rBfIQjRx6BAgBEAU&url=http%3A%2F%2Ffabricadesonhosfsa.blogspot.com%2F2016%2F06%2Fpng-alice-no-pais-das-maravilhas.html&psig=AOvVaw0Fkq-N9nsM7TJB0ucAB0ic&ust=1535633979340667"
TARZAN ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiL6qncppLdAhXCH5AKHZAyBUMQjRx6BAgBEAU&url=http%3A%2F%2Fhero.wikia.com%2Fwiki%2FFile%3ATarzan_Character.png&psig=AOvVaw2Frm4u_vk1-RCkiipJI9_5&ust=1535633480343303"
FLORESTA ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwiCzvyAq5LdAhXBFJAKHeuDBh8QjRx6BAgBEAU&url=https%3A%2F%2Falgarve-saibamais.blogspot.com%2F2016%2F03%2Fcomo-o-vento-na-floresta-poema-de.html&psig=AOvVaw392PmZLmsaLorhggTmv0pB&ust=1535634513603880"
CASTELO ="https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjdwPnPq5LdAhVGmJAKHUF6BQ0QjRx6BAgBEAU&url=http%3A%2F%2Fwww.fazarte.com.br%2Fhome%2Fproduto%2F60-Castelo-Da-Floresta.html&psig=AOvVaw1JIb2JL8P5HQ8KN0n-ZF1h&ust=1535634776117423"

def criarcenas():
    floresta = Cena(img=FLORESTA)
    castelo = Cena(img=CASTELO)