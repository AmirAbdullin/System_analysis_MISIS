import json

def parse_graph(filename):
    with open(filename, 'r') as file:
        graph = json.load(file)
        nodes = list(graph.keys())
        edges = [f"{node}: {', '.join(graph[node])}" for node in nodes]
        return nodes, edges

if __name__ == "__main__":
    filename = input("Введите путь к файлу: ")
    nodes, edges = parse_graph(filename)
    
    print("Узлы:")
    print(' '.join(nodes))
    
    print("Связанные узлы:")
    print('\n'.join(edges))