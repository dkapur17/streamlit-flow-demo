import streamlit as st
from streamlit_flow import streamlit_flow


st.set_page_config(page_title="Interactions - Streamlit Flow", layout="wide")

st.title("Interactions")


st.markdown("This example demonstrates how the two types of interactions supported by Streamlit Flow.")

st.markdown("### 1. Getting Interaction Element")

st.markdown("We can set the `get_node_on_click` and the `get_edge_on_click` parameters to `True` to get the id of the element that was clicked on. This is stored within the `StreamlitFlowState.selected_id` attribute. Try clicking on any of the nodes or edges in the flow below.")


with st.echo('below'):
	import streamlit as st
	from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
	from streamlit_flow.state import StreamlitFlowState
	from streamlit_flow.layouts import TreeLayout

	nodes = [StreamlitFlowNode(id='1', pos=(100, 100), data={'content': 'Node 1'}, node_type='input', source_position='right', draggable=False),
			StreamlitFlowNode('2', (350, 50), {'content': 'Node 2'}, 'default', 'right', 'left', draggable=False),
			StreamlitFlowNode('3', (350, 150), {'content': 'Node 3'}, 'default', 'right', 'left', draggable=False),
			StreamlitFlowNode('4', (600, 100), {'content': 'Node 4'}, 'output', target_position='left', draggable=False)]

	edges = [StreamlitFlowEdge('1-2', '1', '2', animated=True),
			StreamlitFlowEdge('1-3', '1', '3', animated=True),
			StreamlitFlowEdge('2-4', '2', '4', animated=True),
			StreamlitFlowEdge('3-4', '3', '4', animated=True)]

	if 'click_interact_state' not in st.session_state:
		st.session_state.click_interact_state = StreamlitFlowState(nodes, edges)

	updated_state = streamlit_flow('ret_val_flow',
					st.session_state.click_interact_state,
					fit_view=True,
					get_node_on_click=True,
					get_edge_on_click=True)

	st.write(f"Clicked on: {updated_state.selected_id}")


st.markdown("### 2. Creating flows within the Canvas")

st.markdown("""The Streamlit Flow component can be set to become a fully interactive flow diagram builder. 
Right click either on the pane, a node or an edge to see the relevant context-aware menu. 
New edges can be created by dragging from one node's source to another node's target.
You can access the updated flow through the return value of the component.
Try it yourself! Start by right-clicking on the canvas to create a new node.""")

with st.echo('below'):

	if 'canvas_state' not in st.session_state:
		st.session_state.canvas_state = StreamlitFlowState([], [])
		
	st.session_state.canvas_state = streamlit_flow('fully_interactive_flow', 
                    st.session_state.canvas_state, # Start with an empty state, or with some pre-initialized state
                    fit_view=True,
                    show_controls=True,
                    allow_new_edges=True,
                    animate_new_edges=True,
                    layout=TreeLayout("right"),
                    enable_pane_menu=True,
                    enable_edge_menu=True,
                    enable_node_menu=True,
	)
	col1, col2 = st.columns(2)
	col1.metric("Nodes", len(st.session_state.canvas_state.nodes))
	col2.metric("Edges", len(st.session_state.canvas_state.edges))
