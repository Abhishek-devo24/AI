# Graph representation for practicals
dict_gn = {
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},  # Add connections for Fagaras
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101},
    'Bucharest': {}  # No outgoing connections from Bucharest
}

dict_hn = {
    'Arad': 366, 
    'Zerind': 374, 
    'Timisoara': 329, 
    'Sibiu': 253, 
    'Bucharest': 0, 
    'Oradea': 380, 
    'Fagaras': 176, 
    'Rimnicu Vilcea': 193, 
    'Pitesti': 100
}
