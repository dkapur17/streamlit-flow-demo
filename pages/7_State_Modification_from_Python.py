import streamlit as st
from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
import random

st.set_page_config(page_title="State Modification from Python - Streamlit Flow", layout="wide")

st.title("State Modification from Python Demo")

st.markdown("""Since `v1.5.0`, `streamlit_flow` allows for seamless state modification from python. This means that you can add, remove or update nodes and edges from the flow diagram without having to interact with the component itself. Below is an example of a flow diagram where nodes can be added dynamically.
While doing this, you are still fully able to make modification to the flow diagram through the UI, such as creating/editing/moving nodes and edges.
This new ability is brought to you by the new `StreamlitFlowState` class.""")

st.info("It's important to note here that you'll need to maintain the state of the flow in `session_state` to make it persist across reruns. Also notice that the same state is passed as an argument to the component, and is then updated by the return value of the component.")

st.divider()

with st.echo('below'):
    import streamlit as st
    from streamlit_flow import streamlit_flow
    from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
    from streamlit_flow.state import StreamlitFlowState
    from streamlit_flow.layouts import TreeLayout
    import random
    from uuid import uuid4


    if 'curr_state' not in st.session_state:
        nodes = [StreamlitFlowNode("1", (0, 0), {'content': 'Node 1'}, 'input', 'right'),
                StreamlitFlowNode("2", (1, 0), {'content': 'Node 2'}, 'default', 'right', 'left'),
                StreamlitFlowNode("3", (2, 0), {'content': 'Node 3'}, 'default', 'right', 'left'),
                ]

        edges = [StreamlitFlowEdge("1-2", "1", "2", animated=True),
                StreamlitFlowEdge("1-3", "1", "3", animated=True),
                ]
        
        st.session_state.curr_state = StreamlitFlowState(nodes, edges)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Add node"):
            new_node = StreamlitFlowNode(str(f"st-flow-node_{uuid4()}"), (0, 0), {'content': f'Node {len(st.session_state.curr_state.nodes) + 1}'}, 'default', 'right', 'left')
            st.session_state.curr_state.nodes.append(new_node)
            st.rerun()

    with col2:
        if st.button("Delete Random Node"):
            if len(st.session_state.curr_state.nodes) > 0:
                node_to_delete = random.choice(st.session_state.curr_state.nodes)
                st.session_state.curr_state.nodes = [node for node in st.session_state.curr_state.nodes if node.id != node_to_delete.id]
                st.session_state.curr_state.edges = [edge for edge in st.session_state.curr_state.edges if edge.source != node_to_delete.id and edge.target != node_to_delete.id]
                st.rerun()

    with col3:
        if st.button("Add Random Edge"):
            if len(st.session_state.curr_state.nodes) > 1:
                source = random.choice(st.session_state.curr_state.nodes)
                target = random.choice([node for node in st.session_state.curr_state.nodes if node.id != source.id])
                new_edge = StreamlitFlowEdge(f"{source.id}-{target.id}", source.id, target.id, animated=True)
                st.session_state.curr_state.edges.append(new_edge)
                st.rerun()
        
    with col4:
        if st.button("Delete Random Edge"):
            if len(st.session_state.curr_state.edges) > 0:
                edge_to_delete = random.choice(st.session_state.curr_state.edges)
                st.session_state.curr_state.edges = [edge for edge in st.session_state.curr_state.edges if edge.id != edge_to_delete.id]
                st.rerun()


    st.session_state.curr_state = streamlit_flow('example_flow', 
                                    st.session_state.curr_state, 
                                    layout=TreeLayout(direction='right'), 
                                    fit_view=True, 
                                    height=500, 
                                    enable_node_menu=True,
                                    enable_edge_menu=True,
                                    enable_pane_menu=True,
                                    get_edge_on_click=True,
                                    get_node_on_click=True, 
                                    show_minimap=True, 
                                    hide_watermark=True, 
                                    allow_new_edges=True,
                                    min_zoom=0.1)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Current Nodes")
        for node in st.session_state.curr_state.nodes:
            st.write(node)

    with col2:
        st.subheader("Current Edges")
        for edge in st.session_state.curr_state.edges:
            st.write(edge)

    with col3:
        st.subheader("Current Selected Element")
        st.write(st.session_state.curr_state.selected_id)