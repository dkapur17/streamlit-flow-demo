import streamlit as st

st.set_page_config(page_title="Minimap and Controls Demo - Streamlit Flow", layout="wide")

st.title("Minimap and Controls Demo")
st.markdown("""The `streamlit_flow` component comes with a few features that can be enabled or disabled as needed.
Take for example the Controls Bar and Mini-map - they make navigating the flow canvas much simpler.
Here is a minimally interactive flow diagram with both the Controls Bar and Mini-map enabled. Futher, one can even hide the React Flow watermark.""")


with st.echo('below'):
	import streamlit as st
	from streamlit_flow import streamlit_flow
	from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge
	from streamlit_flow.state import StreamlitFlowState

	nodes = [StreamlitFlowNode(id='1', pos=(100, 100), data={'content': 'Node 1'}, node_type='input', source_position='right'),
		StreamlitFlowNode('2', (350, 50), {'content': 'Node 2'}, 'default', 'right', 'left'),
		StreamlitFlowNode('3', (350, 150), {'content': 'Node 3'}, 'default', 'right', 'left'),
		StreamlitFlowNode('4', (600, 100), {'content': 'Node 4'}, 'output', target_position='left')]

	edges = [StreamlitFlowEdge('1-2', '1', '2', animated=True),
		StreamlitFlowEdge('1-3', '1', '3', animated=True),
		StreamlitFlowEdge('2-4', '2', '4', animated=True),
		StreamlitFlowEdge('3-4', '3', '4', animated=True)]

	if 'minimap_controls_state' not in st.session_state:
		st.session_state.minimap_controls_state = StreamlitFlowState(nodes, edges)

	streamlit_flow('minimap_controls_flow',
			st.session_state.minimap_controls_state,
			fit_view=True,
			show_minimap=True,
			show_controls=True,
			hide_watermark=True)

