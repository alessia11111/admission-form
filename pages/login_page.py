import streamlit as st
user_pass = {'cool_coder':'redhouse123','hhihiuhiuj':'gghgggggggggggggggggggggg','hiugluhiouh':'abcdefghijklmnopqrstuvwxyz'}
st.title('LOGIN PAGE')
st.write('already a member? login with your credentials')
if 'logged_in' not in st.session_state:
	st.session_state.logged_in = False
user_name = st.text_input("enter your user name")
user_password = st.text_input("enter your user password")

if st.button("hello, press me to sign in"):
	if user_name in user_pass.keys():
		if user_password == user_pass.get(user_name):
			st.success("you haved logged in succsessfully")
			st.session_state.logged_in = True
			st.switch_page('home.py')
		else:
			st.error('wrong password, try again')
	else:
		st.error('username not in the database, try again')
