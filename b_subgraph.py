from langgraph.graph import StateGraph, START, END

from state import State


def node_b1(state: State) -> State:
    print("Node B1 (subgraph)")
    return state


def node_b2(state: State) -> State:
    print("Node B2 (subgraph)")
    return state


def build_b_subgraph():
    builder = StateGraph(State)
    builder.add_node("B1", node_b1)
    builder.add_node("B2", node_b2)

    builder.add_edge(START, "B1")
    builder.add_edge("B1", "B2")
    builder.add_edge("B2", END)

    return builder.compile()
