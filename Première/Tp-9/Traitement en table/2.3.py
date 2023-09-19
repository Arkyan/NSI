list_dico = [{"Nom":"Baron","Prenom":"Paul","NSI":18,"Physique":16,"Maths":15},{"Nom":"Taillant","Prenom":"Greg","NSI":1,"Physique":3,"Maths":5},{"Nom":"Gourdy","Prenom":"Zoé","NSI":14,"Physique":13,"Maths":16}]
listtriée = sorted(list_dico , key = lambda lyceen:lyceen["NSI"])
print(listtriée)
print(sorted(list_dico , key = lambda lyceen:lyceen["Nom"]))
print(sorted(list_dico , key = lambda lyceen:lyceen["Prenom"]))
print(sorted(list_dico , key = lambda lyceen:lyceen["NSI"]))
print(sorted(list_dico , key = lambda lyceen:lyceen["Maths"]))
print(sorted(list_dico , key = lambda lyceen:lyceen["Physique"]))