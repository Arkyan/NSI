def fusion(list1, list2) :
    if len(list1) == 0 :
        return list2
    if len(list2) == 0 :
        return list1
    if list1[0] < list2[0] :
        return [list1[0]] + fusion(list1[1:], list2)
    else :
        return [list2[0]] + fusion(list1, list2[1:])

def tri_fusion(list) :
    if len(list) <= 1 :
        return list
    else :
        middle = len(list) // 2
        left = tri_fusion(list[:middle])
        right = tri_fusion(list[middle:])
        return fusion(left, right)
    
list1 = [35, 13, 4, 22, 7, 17, 3]
list2 = [39, 28, 44, 4, 10, 80, 11] 
list3 = [22, 11, 3, 55, 37, 30, 44, 59, 2]
list4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print ("La liste", list1, "triée par tri fusion est : ", tri_fusion(list1))
print ("La liste", list2, "triée par tri fusion est : ", tri_fusion(list2))
print ("La liste", list3, "triée par tri fusion est : ", tri_fusion(list3))
print ("La liste", list4, "triée par tri fusion est : ", tri_fusion(list4)) 
