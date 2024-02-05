import csv
class chif:
    def chiffrementcsv(self,file):
        dictionnaire=csv.DictReader(open(file,'r'),delimiter=';')
        dict1 = [dict(ligne) for ligne in dictionnaire ] 
        return dict1
    
def chiffrementrafine(c):
    f=[]
    for i in range(len(c)):
        dictio={}           
        dictio  ['nom']=c[i].get('nom')
        dictio['email']=c[i].get('email')
        dictio['total']=c[i].get('total')
        dictio['pourcentage']=c[i].get('pourcentage')
        dictio['mention']=c[i].get('mention')
        cours=[]
        for a in c[i].keys():
            if not a  in dictio.keys():
                fg={}
                fg[a]=c[i].get(a)
                cours.append(fg)
        dictio['cours']=cours
        f.append(dictio)
    return f


def cote_obtenu(cote,ponderation):
    point=cote*ponderation
    return point
def calcul_point(cours:list,pond:list):
    cour_new=[]
    for a in range(len(cours)):
        f={}
        cle=cours[a].keys()
        f[cle]=cours[a][cle]*pond[a]
        
    return cour_new

