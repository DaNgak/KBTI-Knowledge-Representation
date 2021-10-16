ada_family = { 
    'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
    'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
    'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
    'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
    'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
    'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
    'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
    'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] 
}

def ancestors(genealogy, person):
    list_of_ancestors = []

    if person in genealogy:
        list_of_ancestors = genealogy[person]
        for e in genealogy[person]:
            for i in ancestors(genealogy, e):
                if i not in list_of_ancestors:
                    list_of_ancestors += ancestors(genealogy, e)
        
    else :
        list_of_ancestors += []
    
    return list_of_ancestors

# 1st printing
print("1st printing")
print(ancestors(ada_family, 'Augusta Ada King'))
# 2nd printing
print("2nd printing")
print(ancestors(ada_family, 'Judith Blunt-Lytton'))
# 3rd printing
print("3rd printing")
print(ancestors(ada_family, 'Dave'))