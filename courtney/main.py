# evelyn.courtney# hedy.courtney.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import Inventario as inv

TARZAN_NA_SELVA = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=2ahUKEwiSp_erqJLdAhUIG5AKHW_uCoUQjRx6BAgBEAU&url=http%3A%2F%2Fvsdebating.wikia.com%2Fwiki%2FTarzan_(Disney)&psig=AOvVaw0TVQpXwgWHWGPJzL7mNKuc&ust=1535633936363831"
TARZAN_EM_PE = "htps://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=2ahUKEwi-tuPUqJLdAhVBg5AKHZ5QCNUQjRx6BAgBEAU&url=http%3A%2F%2Fdisney.wikia.com%2Fwiki%2FFile%3ATarzan_Character.png&psig=AOvVaw25foqFTwYscJO-ZYF8nGqg&ust=1535634020674285"
SELVA = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=2ahUKEwiYxI_xqJLdAhWKkJAKHWzcASkQjRx6BAgBEAU&url=https%3A%2F%2Fpt.pngtree.com%2Ffreepng%2Fgreen-jungle-vector_3112050.html&psig=AOvVaw3biCw7HLOV7smsJHLUCyEw&ust=1535634081117719"
ALICE = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=2ahUKEwjpqYOnqZLdAhXJTZAKHVFTBZIQjRx6BAgBEAU&url=http%3A%2F%2Fpt-br.kingdomhearts.wikia.com%2Fwiki%2FFicheiro%3AAlice_KHREC.png&psig=AOvVaw08fewna7kgFYybCjqT1pLk&ust=1535634191838171"
PANTANO = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=imgres&cd=&cad=rja&uact=8&ved=2ahUKEwi9-sH3qZLdAhXDC5AKHTiNAy0QjRx6BAgBEAU&url=http%3A%2F%2Fpt-br.star-wars-the-force-unleashed.wikia.com%2Fwiki%2FLuke_Skywalker&psig=AOvVaw3mVpcTn4gX2ja0Qx9KLkr_&ust=1535634362903632"
MESA = "https://1.bp.blogspot.com/-8hu8fFASgiU/WT196QOBtdI/AAAAAAAAAaM/j5PPLpuWSj4_aMafNIj2t_8sMoyD7xh5ACLcB/s1600/primeiro_jantar_de%2B_dia_dos_namorados_meu_ape_34_mesa_posta.jpg"
CASTELO = "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjh2paUtZLdAhWFkpAKHb1ZAYUQjRx6BAgBEAU&url=https%3A%2F%2Fpt.pngtree.com%2Ffreepng%2Fcastle_2219608.html&psig=AOvVaw3ypoy85e5RDH-_cxE6fyjQ&ust=1535637347341413"

def criarcenas(): 
    selva = Cena(img=SELVA) 
    mesa = Cena(img=MESA)
    selva.direita = MESA
    
    tarzan = Elemento(img=TARZAN_NA_SELVA, tit="Tarzan", style=dict(left="150px", top="150px", width="150px", heigth="150px"))
    tarzan.entra(selva)
    etarzan = Texto (selva, "Tarzan, que foi criado na selva, quando chega na idade adulta, por conhecer a selva muito bem e se achar o rei dela se perde na floresta.")
    tarzan.vai = etarzan.vai
    
    selva.vai()
criarcenas()    