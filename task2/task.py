from io import StringIO
import csv

class GraphAnalyzer:
    def __init__(self, csvString):
        self.graph = dict()
        self.nodes = set()
        self.starts = set()
        self.not_starts = set()
        self.result = None

        self.build_graph(csvString)

    def build_graph(self, csvString):
        f = StringIO(csvString)
        reader = csv.reader(f, delimiter=',')

        for row in reader:
            a, b = row[0], row[1]

            if a in self.graph:
                self.graph[a].append(b)
            else:
                self.graph[a] = [b]

            self.nodes.add(a)
            self.nodes.add(b)
            self.not_starts.add(b)

        for node in self.nodes:
            if node not in self.graph:
                self.graph[node] = []
            if node not in self.not_starts:
                self.starts.add(node)

    def bfs(self, cur, prev, neighbours):
        parent = 1 if (prev > 0) else 0

        self.result[cur][1] += parent
        self.result[cur][3] += prev - parent
        self.result[cur][0] = len(self.graph[cur])
        self.result[cur][4] = neighbours

        for child in self.graph[cur]:
            self.result[cur][2] += self.bfs(child, prev + 1, len(self.graph[cur]) - 1)

        self.result[cur][2] -= self.result[cur][0]

        return self.result[cur][2] + self.result[cur][0] + 1

    def analyze_graph(self):
        self.result = {node: [0, 0, 0, 0, 0] for node in self.nodes}

        for start in self.starts:
            self.bfs(start, 0, 0)

        keys = sorted(self.result.keys())
        values = [self.result[key] for key in keys]

        return '\n'.join([",".join(str(el) for el in value) for value in values])


def task(csvString):
    analyzer = GraphAnalyzer(csvString)
    return analyzer.analyze_graph()

print(task("1,2\n2,3\n2,4\n3,5\n3,6"))
