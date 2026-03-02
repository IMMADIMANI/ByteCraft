class Movie:
    lang = "Teugu"
    def __init__(self,director,hero,tp):
        self.director = director
        self.hero = hero
        self.ticket_price = tp
    def collection(self,tickets):
        return self.ticket_price*tickets
    def Dub(self,new__lang):
        self.lang=new__lang
bahubali=Movie("SSR","PB",350)
bahubali.lang
bahubali.Dub("Hindi")
bahubali.lang
spirit = Movie("SRV","PB","500")