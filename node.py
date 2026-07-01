from state import State


def node_a(state: State) -> State:
    print("Node A")
    state["skip_b"] = "skip" in state.get("message", "")
    return state


def route_from_a(state: State) -> str:
    return "C" if state.get("skip_b") else "B"


def node_c(state: State) -> State:
    print("Node C")
    return state
