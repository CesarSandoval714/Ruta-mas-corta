from collections import deque
from timeit import default_timer


class Graph:
    adjac_lis = {}
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    # Esta es una función heurística que tiene valores para cada nodo .
    #  Valor heuristico que representa la ruta de costo real desde el nodo actual al nodo objetivo. 
    def h(self, n):
        H = {
            'A': 9,
            'B': 4,
            'C': 2,
            'D': 5,
            'E': 3,
            'S': 7,
            'G': 0
        }
             

            
        
 
        return H[n]
 
    def a_star_algorithm(self, start, stop):  #Funcion de A* con dos parametros el nodo inicial y el nodo objetivo
        # En este open_lst hay una lista de nodos que han sido visitados,
        # cuyos vecinos no han sido siempre inspeccionados. Comienza con el nodo inicial.
  
        # Y closed_lst es una lista de nodos generados que se han visitado
        # y cuyos vecinos siempre han sido inspeccionados.
        open_lst = set([start]) #OpenList esta igualada a una lista vacia de nodos
        closed_lst = set([])  #ClosedList esta igualada a una lista vacia de nodos 
 
        # poo tiene distancias presentes desde el inicio hasta todos los demás nodos
        poo = {} #Va guardando distancia desde el nodo inicial hacia los nodos recorridos g(n)
        poo[start] = 0 #Aqui es como tener f=0 
 
        # par contiene un mapeo adjac de todos los nodos
        par = {} 
        par[start] = start
 
        while len(open_lst) > 0:  #Mientras que OpenList no este vacia 
            n = None

            #Colocar el nodo inicial en OpenList     
            # encontrará un nodo con el valor más bajo de f(n)
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n): 
                    n = v;  
 
            if n == None:
                print('¡El camino no existe!')
                return None
 
            # si el nodo actual es la parada encontramos la ruta
            # luego comenzamos de nuevo desde el principio
            if n == stop:
                reconst_path = []
 
                while par[n] != n: 
                    reconst_path.append(n) # 
                    n = par[n]  
 
                reconst_path.append(start) #Agremos los nodos que forman el camino 
 
                reconst_path.reverse() #Funcion para revertir la lista local 
 
                print('Ruta encontrada: {}'.format(reconst_path))
                return reconst_path
 
            #Funcion para buscar nodos
            # para todos los nodos adyacentes del nodo actual
            for (m, weight) in self.get_neighbors(n): 
              # si el nodo actual no está presente tanto en la list abierta como en la lst cerrada
                # se agrega a OpenList y tenga en cuenta n como es par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m) 
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                # de lo contrario, compruebe si es más rápido visitar primero n, luego m
                # y si es así, actualice los datos par y poo
                # y si el nodo estaba en closed_lst, muévelo a open_lst
                else:
                    if poo[m] > poo[n] + weight: 
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # eliminar n de open_lst y agregarlo a closed_lst
            #Porque todos sus vecinos fueron inspeccionados
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('El camino no existe!')
 

        return None
 
adjac_lis = {
     'A': [('B', 5), ('C', 3), ('G', 10)], #Aqui aplica lo de si no esta en la lista abierta ni cerrada, agregar G 
    'B': [('C', 2), ('E', 1)],
    'C': [('G', 4)],
    'D': [('B', 1), ('E', 4)],
    'E': [('G', 3)],
    'S': [('A', 3), ('D', 2)]
}

 
graph1 = Graph(adjac_lis)
inicio = default_timer()
graph1.a_star_algorithm('S', 'G')
fin = default_timer()
print('El tiempo de ejecución es de :', fin - inicio)


        









