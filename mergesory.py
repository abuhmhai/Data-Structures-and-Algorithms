def Mergesort(first_element,second_element):
    i=j=0;
    merge_list=[]
    while i<len(first_element) and j<len(second_element):
        if first_element[i]<second_element[j]:
            merge_list.append(first_element[i])
            i+=1
        else:
            merge_list.append(second_element[j])
            j+=1
    while i<len(first_element):
        merge_list.append(first_element[i])
        i+=1
    while j<len(second_element):
        merge_list.append(second_element[j])
        j+=1
    return merge_list

a=[51, 82, 20, 96, 44, 15, 68, 73, 39]
sorted_a = Mergesort(a[:len(a)//2], a[len(a)//2:])
print(sorted_a)