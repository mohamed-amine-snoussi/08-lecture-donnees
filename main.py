#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>"""
    with open(filename, "r", encoding="utf8") as f:
        lines = f.readlines()

    # conversion en liste de listes d'entiers
    l = [[int(x) for x in line.strip().split(";")] for line in lines if line.strip()]
    return l



def get_list_k(data, k):
    """retourne la k-ième liste de data"""
    l = data[k]
    return l

def get_first(l):
    """retourne le premier élément d'une liste"""
    return l[0]

def get_last(l):
    """retourne le dernier élément d'une liste"""
    return l[-1]

def get_max(l):
    """retourne le maximum d'une liste"""
    return max(l)

def get_min(l):
    """retourne le minimum d'une liste"""
    return min(l)

def get_sum(l):
    """retourne la somme des éléments d'une liste"""
    return sum(l)

#### Fonction principale


def main():
    data = read_data(FILENAME)
    for i, l in enumerate(data[:5]):  # affiche les 5 premières lignes pour test
        print(i, l)
    k = 0
    print(k, get_list_k(data, k))
    print("Premier élément :", get_first(data[k]))
    print("Dernier élément :", get_last(data[k]))
    print("Max :", get_max(data[k]))
    print("Min :", get_min(data[k]))
    print("Somme :", get_sum(data[k]))

if __name__ == "__main__":
    main()
