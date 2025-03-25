import streamlit as st

st.title("My first webapp")


criteria_annual_salary = 50000
criteria_year_of_work = 5

annual_salary = st.number_input("Please enter your annual salary:")
work_year = st.number_input("Please enter your work year:")

if st.button("Submit"):
    if annual_salary >= criteria_annual_salary:
        if work_year >= criteria_year_of_work:
            st.write(f"Congratulations, your application has accepted!")
        else:
            work_year_need = criteria_year_of_work - work_year
            st.write(f"Sorry, your application has been rejected! You need {work_year_need:,.2f} year more to be accepted.")
    else:
        if work_year >= criteria_year_of_work:
            annual_salary_need = criteria_annual_salary - annual_salary
            st.write(f"Sorry, your application has been rejected! You need {annual_salary_need:,.2f} more to be accepted.")
        else:
            annual_salary_need = criteria_annual_salary - annual_salary
            work_year_need = criteria_year_of_work - work_year
            st.write(f"Sorry, your application has been rejected! You need {annual_salary_need:,.2f} yuan and {work_year_need:,.2f} year more to be accepted.")

