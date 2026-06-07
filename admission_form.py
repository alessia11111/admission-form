import streamlit as st
def app():
	st.image('latymer-upper-school-logo.png')
	st.subheader('Admission Form')
	col1, col2 = st.columns(2)

	with col1:
	    st.text_input("what is the student's name: ")

	with col2:
	    st.text_input("what is the student's last name: ")

	st.radio("select student's age",[11,12,13,14,15,16,17,18])

	st.radio('select gender', ['female', 'male'])

	st.selectbox('select the class you are applying for', ['year 7', 'year 8','year 9','year 10','year 11','lower sixth','upper sixth'])

	st.text_input("student's DoB (mm/dd/yyyy): ")

	col3, col4 = st.columns(2)
	with col3:
	    st.text_input("what is the parent's name: ")

	with col4:
	    st.text_input("what is the parent's last name: ")

	st.text_input("address, street address: ")
	st.text_input("address, street address line 2: ")
	st.text_input("address, city: ")
	st.text_input("address, region: ")
	st.text_input("address, postal / zip code: ")
	st.text_input("address, country: ")
	st.text_input("phone number: ")
	st.text_input("email (for confirmation): ")

	if st.button('click me to submit'):
	    st.success('you have submitted me successfully')