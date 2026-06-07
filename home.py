import streamlit as st
import admission_form
import school_info
if not st.session_state.get('logged_in',False):
	st.switch_page('pages/login_page.py')
pages_dict = {
	'Form': admission_form,
	'Info': school_info,

}
st.sidebar.title('navigation')
user = st.sidebar.radio(' go to',tuple(pages_dict.keys()))
if user =='Form':
	admission_form.app()
else:
	school_info.app()