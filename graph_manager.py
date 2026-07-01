from langgraph.graph import StateGraph, START, END

from state import State
from node import node_a, node_b, node_c


def build_graph():
    graph_builder = StateGraph(State)
    graph_builder.add_node("A", node_a)
    graph_builder.add_node("B", node_b)
    graph_builder.add_node("C", node_c)

    graph_builder.add_edge(START, "A")
    graph_builder.add_edge("A", "B")
    graph_builder.add_edge("B", "C")
    graph_builder.add_edge("C", END)

    return graph_builder.compile()


if __name__ == "__main__":
    graph = build_graph()
    graph.invoke({"message": "start"})
