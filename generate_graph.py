from graph import app_graph

graph = app_graph.get_graph()

mermaid = graph.draw_mermaid()

with open("graph.md", "w") as f:
    f.write(mermaid)
