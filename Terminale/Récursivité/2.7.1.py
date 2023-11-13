def palindrome(chaine) :
    if len(chaine) <= 1 :
        return True
    else :
        return chaine[0] == chaine[len(chaine) - 1] and palindrome(chaine[1:len(chaine) -1])
    
chaine = int(input("Entrez une chaine de caractères : "))
print("La chaine de caractères",chaine,"est un palindrome", palindrome(chaine))

chaine1 = ""
chaine2 = "e"
chaine3 = "nsi"
chaine4 = "ELLE"

print("La chaine de caractère", chaine1, "est un paldindrome :", palindrome(chaine1))
print("La chaine de caractère", chaine2, "est un paldindrome :", palindrome(chaine2))
print("La chaine de caractère", chaine3, "est un paldindrome :", palindrome(chaine3))
print("La chaine de caractère", chaine4, "est un paldindrome :", palindrome(chaine4))

assert palindrome(chaine1) == True
assert palindrome(chaine2) == True
assert palindrome(chaine3) == False
assert palindrome(chaine4) == True

