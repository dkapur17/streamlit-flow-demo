import streamlit as st

st.set_page_config(layout="wide", page_title="Streamlit Flow")



st.title("Streamlit Flow")
st.markdown("Streamlit Flow is a library for creating and visualizing flow diagrams in Streamlit. Powered by ReactFlow, Streamlit Flow provides an extensive wrapper over ReactFlow while also adding several quality of life features like Context Menus and a Layout Engine, all accessible through the simplicity of Streamlit.")

st.markdown("# Installation")
st.markdown("The library can be installed from PyPI using")
st.code("pip install streamlit-flow-component", 'bash')

st.markdown("# Usage")

st.markdown("There are four main components in Streamlit Flow:")
st.markdown("The component itself: `streamlit_flow`")
st.markdown("The component state: `StreamlitFlowState`")
st.markdown("The flow elements: `StreamlitFlowNode` and `StreamlitFlowEdge`")
st.markdown("The layouts: `ManualLayout`, `LayeredLayout`, `TreeLayout`, `RadialLayout`, `ForceLayout`, `StressLayout`, `RandomLayout`")

st.markdown("## Streamlit Flow Component")
st.markdown("The Streamlit Flow component is the main component that is used to render the flow diagram.")
st.code("""streamlit_flow(
    key:str,
    state:StreamlitFlowState,
    height:int=500,
    fit_view:bool=False,
    show_controls:bool=True,
    show_minimap:bool=False,
    allow_new_edges:bool=False,
    animate_new_edges:bool=False,
    style:dict={},
    layout:Layout=ManualLayout(),
    get_node_on_click:bool=False,
    get_edge_on_click:bool=False,
    pan_on_drag:bool=True,
    allow_zoom:bool=True,
    min_zoom:float=0.5,
    enable_pane_menu:bool=False,
    enable_node_menu:bool=False,
    enable_edge_menu:bool=False,
    hide_watermark:bool=False
)""")

st.divider()

st.markdown("## Streamlit Flow State")
st.markdown("The Streamlit Flow State maintains the state of the flow diagram and makes sure the UI and streamlit are in sync.")

st.code("""StreamlitFlowState(
    nodes:List[StreamlitFlowNode],
    edges:List[StreamlitFlowEdge],
    selected_id:str=None,
    timestamp:float=0.0
)""")

st.warning("Do not explicitly set `selected_id` or `timestamp` as they are used internally by the component.")

st.divider()

st.markdown("## Streamlit Flow Elements")
st.markdown("The Streamlit Flow elements are the nodes and edges that are used to create the flow diagram. Each has its own interface as described below.")


col1, col2 = st.columns(2)

with col1:
    st.markdown("### Streamlit Flow Node")
    st.code("""StreamlitFlowNode(
    id:str,
    pos: Tuple[float, float],
    data:Dict[str, any],
    node_type:Literal['default', 'input', 'output'] = 'default',
    source_position:Literal['bottom', 'top', 'left', 'right'] = 'bottom',
    target_position:Literal['bottom', 'top', 'left', 'right'] = 'top',
    hidden:bool=False,
    selected:bool=False,
    dragging:bool=False,
    draggable:bool=True,
    selectable:bool=False,
    connectable:bool=False,
    resizing:bool=False,
    deletable:bool=False,
    z_index:float=0,
    focusable:bool=True,
    style:Dict[str, any]={},
    **kwargs
)""")

    st.markdown("""* `style` is a CSS style dictionary. Eg. `{"backgroundColor": "green", "fontWeight": 900}`
* `**kwargs` can be any other attribute on a React Flow node that you wish to manually set (not recommended).
""")

with col2:
    st.markdown("### Streamlit Flow Edge")
    st.code("""StreamlitFlowEdge(
    id:str,
    source:str,
    target:str,
    edge_type:Literal['default', 'straight', 'step', "smoothstep", "simplebezier"]="default",
    marker_start:dict={},
    marker_end:dict={},
    hidden:bool=False,
    animated:bool=False,
    selected:bool=False,
    deletable:bool=False,
    focusable:bool=False,
    z_index:float=0,
    label:str="",
    label_style:Dict[str, any]={},
    label_show_bg:bool=False,
    label_bg_style:Dict[str, any]={},
    style:Dict[str, any]={}
    **kwargs
)""")

    st.markdown("""* `marker_start` and `marker_end` are dictionaries that can be used to style the start and end markers of the edge. Refer to the [React Flow documentation](https://reactflow.dev/api-reference/types/edge-marker) for more information.`
* `label_style`, `label_bg_style` and `style` are all a CSS style dictionaries. Eg. `{"backgroundColor": "green", "fontWeight": 900}`
* `**kwargs` can be any other attribute on a React Flow node that you wish to manually set (not recommended).
""")

st.divider()

st.markdown("## Streamlit Flow Layouts")

st.markdown("Streamlit flow provides easy to use layouts to automatically arrange the nodes in the flow diagram.")

tree_col, layered_col, radial_col = st.columns(3)
col4, col5, col6 = st.columns(3)



    
with tree_col:
    st.markdown("### Tree Layout")
    st.markdown("Arranges the nodes in a tree structure.")
    st.code("""TreeLayout(
    direction:Literal['up', 'down', 'left', 'right'], 
    node_node_spacing:float=75
)""")

with layered_col:
    st.markdown("### Layered Layout")
    st.markdown("Arranges the nodes in layers.")
    st.code("""LayeredLayout(
    direction:Literal['up', 'down', 'left', 'right'], 
    node_node_spacing:float=75, 
    node_layer_spacing:float=75
)""")
    


with radial_col:
    st.markdown("### Radial Layout")
    st.markdown("Arranges the nodes radially.")
    st.code("""RadialLayout(
    node_node_spacing:float=75
)""")

with col4:
    st.markdown("### Force Layout")
    st.markdown("Uses a force directed layout.")
    st.code("""ForceLayout(
    node_node_spacing:float=75
)""")
    
with col5:
    st.markdown("### Stress Layout")
    st.markdown("Uses a stress layout.")
    st.code("""StressLayout(
    node_node_spacing:float=75
)""")

with col6:
    st.markdown("### Random Layout")
    st.markdown("Arranges the nodes randomly.")
    st.code("""RandomLayout(
    node_node_spacing:float=75
)""")

st.markdown("The default layout is `ManualLayout()`, which uses the provided node positions without any automatic arrangement.")
st.markdown("""All layouts inherit from the `Layout` class and have a `__to_dict__` method that returns a dictionary contining the options for the layout engine.
One can also create a custom layout by inheriting from the `Layout` class and implementing the `__to_dict__` method.""")

st.code("""
from typing import Dict, Union
from streamlit.layouts import Layout
    
class CustomLayout(Layout):

    def __init__(self, elkOptions:Dict[str, Union[str, int]]) -> None:
        self.elkOptions = elkOptions

    def __to_dict__(self) -> Dict[str, any]:
        return {
            "elkOptions": self.elkOptions
        }
    
""")
st.markdown("The options to supply to `elkOptions` can be found in the [ELK documentation](https://eclipse.dev/elk/reference.html).")

st.divider()

st.markdown("# Demos")

st.markdown("Several demos, showcasing the various features can be found in the sidebar.")
