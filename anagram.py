def find_anagrams(word, candidates):
    list=[]
    lower_word = word.lower()
    for i in candidates:
        lower_i = i.lower()
        if lower_i != lower_word:
            sorted_i = sorted(lower_i)
            if sorted(lower_word) == sorted_i:
                list.append(i)
                
    return(list)