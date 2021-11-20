
adjac_lis = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Oradea', 71)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Lugoj', 111)],
    'Oradea': [('Sibiu', 151)],
    'Lugoj': [('Mehadia', 70)],
    'Mehadia': [('Drobeta', 75)],
    'Drobeta': [('Craiova', 120)],
    'Craiova': [('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Fagaras' : [('Bucharest', 211)],
    'Rimnicu Vilcea' : [('Pitesti', 97)],
    'Pitesti' : [('Bucharest', 101)] 
}

H = {
            'Arad': 366,
            'Zerind': 374,
            'Sibiu': 253,
            'Timisoara': 329,
            'Oradea': 380,
            'Lugoj': 244,
            'Mehadia': 241,
            'Drobeta': 242,
            'Craiova': 160,
            'Fagaras': 176,
            'Rimnicu Vilcea' : 193,
            'Pitesti' : 400,
            'Bucharest' : 0

            
            }

adjac_lis = {

    'A': [('B', 11), ('C', 18), ('D', 14)],
    'B': [('D', 12), ('E', 14)],
    'C': [('D', 9), ('E', 20)],
    'D': [('E', 16)],
    'E': [('G', 19), ('D', 10), ('F', 18)],
    'F': [('D', 17), ('C', 12), ('G', 21)],
    'G': [('H', 16)],
    'H': [('I', 15), ('F',16), ('J', 12)],
    'I': [('G', 12), ('J', 19)]   
}   




pruebas_list = {

    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Oradea', 71)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Lugoj', 111)],
    'Oradea': [('Sibiu', 151)],
    'Lugoj': [('Mehadia', 70)],
    'Mehadia': [('Drobeta', 75)],
    'Drobeta': [('Craiova', 120)],
    'Craiova': [('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Fagaras' : [('Bucharest', 211)],
    'Rimnicu Vilcea' : [('Pitesti', 97)],
    'Pitesti' : [('Bucharest', 101)] 
}

H = {
            'Arad': 366,
            'Zerind': 374,
            'Sibiu': 253,
            'Timisoara': 329,
            'Oradea': 380,
            'Lugoj': 244,
            'Mehadia': 241,
            'Drobeta': 242,
            'Craiova': 160,
            'Fagaras': 176,
            'Rimnicu Vilcea' : 193,
            'Pitesti' : 100,
            'Bucharest' : 0

        }

adjac_lis = {
    'A': [('G', 3)],
    'S': [('A', 1)],
    'S': [('G', 5)]
}

adjac_lis = {
    'A': [('B', 5), ('C', 3), ('G', 10)], #Aqui aplica lo de si no esta en la lista abierta ni cerrada, agregar G 
    'B': [('C', 2), ('E', 1)],
    'C': [('G', 4)],
    'D': [('B', 1), ('E', 4)],
    'E': [('G', 3)],
    'S': [('A', 3), ('D', 2)]
    
}

H = {
            'A': 9,
            'B': 4,
            'C': 2,
            'D': 5,
            'E': 3,
            'S': 7,
            'G': 0
            

        }

adjac_lis = {
    'A': [('G', 2)],
    'B': [('G', 3)],
    'S': [('A', 2), ('B', 2)]


}

H = {
            'A': 2,
            'B': 1,
            'S': 3,
            'G': 0,
            
            }

