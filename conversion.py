def conversion_string_float(a:str):
    if "," in a:
        b=a.replace(",",".") 
    else:
        b=a
    return float(b)
def conservision_cours(cours:list):
    new_cours=[]
    for a in cours:
        f={}
        for i in a.keys():
                f[i]=conversion_string_float(a[i])
        #on a pas fait append là haut parce que         
        new_cours.append(f)
        
    return new_cours
def conservion_dict_cours(ligne:dict):
    ligne['cours']=conservision_cours(ligne.get('cours'))
    return ligne
def conversion(tab:list):
    new_file=[]
    for i in range(len(tab)):
        a=conservion_dict_cours(tab[i])
        new_file.append(a)
    return new_file

            
def dict_to_list(diction:dict):
    liste=[]
    for d in diction.keys():
        f={}
        f[d]=diction[d]
        liste.append(f)
    return liste    
    