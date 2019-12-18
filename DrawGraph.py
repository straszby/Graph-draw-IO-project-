#funkcja rysujaca graf, przyjmuje liste z listami
# nalezy zainsatalowac biblioteke Graphviz 2.38 i dodac .../Graphviz 2.38/bin do zmiennych srodowiskowych
def draw_graph(data):
	from graphviz import Digraph
	graph = Digraph(comment='Program Dependences Diagram')
	graph.attr('node', shape='box', style='filled', fillcolor='lightblue')

	for x in data:
		vertex1 = x[0] + "\n" + str(x[1])
		vertex2 = x[2] + "\n" + str(x[3])
		edge = str(x[4])
		graph.edge(vertex2, vertex1, edge)

	graph.render('graph', view=True, format='svg')