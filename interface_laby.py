def get_random_item_in(my_list):
    item = my_list[0]
    return item 

quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

characters = {(1, 4) : "M", (2, 4) : " ", (3, 4) : " ", (4, 4) : " ", (5, 4) : " "}

a = input("Appuyer sur la touche 'W' pour aller en haut : ")
if a == "W":
	if characters[(1, 4)] != characters[(2, 4)]:
		characters[(1, 4)] = characters[(2, 4)]		
print(characters)
