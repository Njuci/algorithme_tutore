"""
j'ai  les points obtenue dans une liste des dictionnaires
    et les pondérations aussi
    """
def calcul_p(po:list,pond:list):
    new_cours=[]
    
    for i in  po:
        f={}
        for p in i.keys():            
             for j in pond:
                 for u in j.keys():
                     if u==p:
                         f[u]=i[p]*j[u]
        new_cours.append(f)
    return new_cours
def total_cours_credit(cours:list):
    total=0
    for i in cours:
        for u in i.keys():
            total+=i[u]
    return total
def calcul_point_dict(ligne:dict,pond:list):
    ligne['cours']=calcul_p(ligne['cours'],pond)
    return ligne
def pourcentage(point:float,total:float):
    return 100*point/total
def calcul_point_list(list_etudiant:list,pond:list):
    new_list=[]                                                                 
    for i in list_etudiant:
        new_list.append(calcul_point_dict(i,pond))
    return new_list
