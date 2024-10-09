import streamlit as st


st.set_page_config(page_title="Custom Styles - Streamlit Flow", layout="wide")

st.title("Custom Styles Flow Demo")
st.markdown("""Nodes and Edge labels can be lightly customized using the `style` property of the `StreamlitFlowNode` and `StreamlitFlowEdge` classes.
The specific values to be set in the `style` dictionary are governed by CSS style properties. You can read more about them [here](https://www.w3schools.com/cssref/default.asp).
An important note here is that while in traditional CSS, you would use kebab case (`kebab-case`), in these dictionaries you must use lower camel case (`lowerCamelCase`) for the property names,
so `background-color` becomes `backgroundColor`. Here's an example of how to manipulate the styles of the nodes and edges in a flow diagram.""")


with st.echo('below'):
	from streamlit_flow import streamlit_flow
	from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
	from streamlit_flow.state import StreamlitFlowState


	nodes = [StreamlitFlowNode('1', (100, 100), {'content': 'Green Node'}, 'input', 'right', draggable=False, style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'}),
			StreamlitFlowNode('2', (350, 25), {'content': 'Smol Node'}, 'output', 'right', 'left', draggable=False, style={'fontSize': '8px', 'padding': 0, 'width': '40px'}),
			StreamlitFlowNode('3', (350, 175), {'content': 'Regular Node'}, 'output', 'right', 'left', draggable=False)]

	edges = [StreamlitFlowEdge('1-2', '1', '2', animated=True, label="edge", label_show_bg=True, label_bg_style={'stroke': 'red', 'fill': 'gray'}),
			StreamlitFlowEdge('1-3', '1', '3', animated=True)]
	
	state = StreamlitFlowState(nodes, edges)

	streamlit_flow('custom_style_flow',
					state,
					fit_view=True,
					show_minimap=False,
					show_controls=False,
					pan_on_drag=False,
					allow_zoom=False)
