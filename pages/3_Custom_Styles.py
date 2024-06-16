import streamlit as st
from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge


st.set_page_config(page_title="Custom Styles - Streamlit Flow", layout="wide")

st.title("Custom Styles Flow Demo")
st.markdown("""Nodes and Edge labels can be lightly customized using the `style` property of the `StreamlitFlowNode` and `StreamlitFlowEdge` classes.
The specific values to be set in the `style` dictionary are governed by CSS style properties. You can read more about them [here](https://www.w3schools.com/cssref/default.asp).
An important note here is that while in traditional CSS, you would use kebab case (`kebab-case`), in these dictionaries you must use lower camel case (`lowerCamelCase`) for the property names,
so `background-color` becomes `backgroundColor`. Here's an example of how to manipulate the styles of the nodes and edges in a flow diagram.""")



nodes = [StreamlitFlowNode('1', (100, 100), {'label': 'Green Node'}, 'input', 'right', draggable=False, style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'}),
        StreamlitFlowNode('2', (300, 25), {'label': 'Smol Node'}, 'output', 'right', 'left', draggable=False, style={'width': '50px', 'height': '40px', 'fontSize': '8px'}),
        StreamlitFlowNode('3', (300, 175), {'label': 'Regular Node'}, 'output', 'right', 'left', draggable=False)]

edges = [StreamlitFlowEdge('1-2', '1', '2', animated=True, 
                            label="edge", 
                            label_show_bg=True, 
                            label_bg_style={'stroke': 'red', 'fill': 'gray'}
                            ),
        StreamlitFlowEdge('1-3', '1', '3', animated=True)]

streamlit_flow('static_flow',
                nodes,
                edges,
                fit_view=True,
                show_minimap=False,
                show_controls=False,
                pan_on_drag=False,
                allow_zoom=False)

st.divider()

with st.expander("Spolier"):
    st.code("""
from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
        
nodes = [StreamlitFlowNode('1', (100, 100), {'label': 'Green Node'}, 'input', 'right', draggable=False, 
                            style={'color': 'white', 'backgroundColor': '#00c04b', 'border': '2px solid white'}),
        StreamlitFlowNode('2', (300, 25), {'label': 'Smol Node'}, 'output', 'right', 'left', draggable=False, 
                            style={'width': '50px', 'height': '40px', 'fontSize': '8px'}),
        StreamlitFlowNode('3', (300, 175), {'label': 'Regular Node'}, 'output', 'right', 'left', draggable=False)]

edges = [StreamlitFlowEdge('1-2', '1', '2', animated=True, 
                            label="edge", 
                            label_show_bg=True, 
                            label_bg_style={'stroke': 'red', 'fill': 'gray'}
                            ),
        StreamlitFlowEdge('1-3', '1', '3', animated=True)]

streamlit_flow('static_flow',
                nodes,
                edges,
                fit_view=True,
                show_minimap=False,
                show_controls=False,
                pan_on_drag=False,
                allow_zoom=False)
""")