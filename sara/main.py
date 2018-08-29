# evelyn.sara.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv



CITY = "http://1.bp.blogspot.com/-WGbHYROaBjg/VhWGBcvfw9I/AAAAAAAAJRE/MdLFeGT6Gf4/s1600/the%2Bflash%2B2x01%2Bb.jpg"
FLASH = "https://icon2.kisspng.com/20180423/cie/kisspng-justice-league-heroes-the-flash-wonder-woman-supe-background-flashing-5ade6c7b2c2cd5.388088061524526203181.jpg"
GOTHAM = "http://pixelartmaker.com/art/5c64e7bf2ab64a7.png"


def criarcenas ():
    City = Cena(img=CITY)
    wonderland = Cena(img=GOTHAM)
    City.direita = wonderland

    flash = Elemento(img=FLASH, tit="Flash", style=dict(left=150, top=160, width=60, height=200))
    flash.entra(wonderland)
    falaflash = Texto(wonderland, "Meu nome é Barry Allen")
    flash.vai = falaflash.vai
    
    
    
    City.vai
    
criarcenas ()