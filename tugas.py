ada_family = { 
    'Rofi': ['Anik', 'Lies', 'Fendi'],
    'Setya': ['Anik', 'Lies', 'Fendi'],
    'Didik': ['Lutfi', 'Andin'],
    'Anik': ['Lutfi', 'Andin'],
    'Lies': ['Hanan'],
    'Fendi': ['Lia', 'Vano'],
    'Ita': ['Lia', 'Vano'],
    'Lutfi': ['Farhan', 'Arfan'],
    'Andin': ['Naura']
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
print(ancestors(ada_family, 'Fendi'))
# 2nd printing
print("2nd printing")
print(ancestors(ada_family, 'Setya'))
# 3rd printing
print("3rd printing")
print(ancestors(ada_family, 'Test Doank'))