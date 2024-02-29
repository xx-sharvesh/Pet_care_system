import os
import streamlit as st

def display_pet_record():
    st.title("Pet Record")
    st.subheader("Pet Information")
    name = st.text_input("Name", "Buddy")
    age = st.number_input("Age (in months)", min_value=0, max_value=300, step=1, value=12)
    species = st.text_input("Species", "Dog")
    breed = st.text_input("Breed", "Golden Retriever")
    weight = st.text_input("Weight (in kg)", "20 kg")

    st.subheader("Medical History")
    vaccinations = st.text_area("Vaccinations", "1. Rabies - 12/01/2024\n2. Distemper - 02/15/2024")
    surgeries = st.text_area("Surgeries", "Neutering (2023)")
    allergies = st.text_area("Allergies", "None")

    st.subheader("Activity Log")
    activity_log = st.text_area("Activity Log", "Today, Buddy went for a walk in the park.")

    if st.button("Save"):
        # Save the updated pet record data
        save_pet_record(name, age, species, breed, weight, vaccinations, surgeries, allergies, activity_log)
        st.success("Pet Record Updated!")

def save_pet_record(name, age, species, breed, weight, vaccinations, surgeries, allergies, activity_log):
    # Here you can implement code to save the pet record data to a file named after the pet's name
    # For example, you can use a database or write to a file
    # This is a placeholder function for demonstration purposes
    filename = f"{name}_record.txt"
    with open(filename, "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age} months\n")
        file.write(f"Species: {species}\n")
        file.write(f"Breed: {breed}\n")
        file.write(f"Weight: {weight}\n")
        file.write(f"\nMedical History:\n{vaccinations}\n{surgeries}\n{allergies}\n")
        file.write(f"\nActivity Log:\n{activity_log}")

def signup():
    st.title("Signup")
    name = st.text_input("Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        # Here you can save the signup data to your data source
        st.success("Signup Successful!")

def set_reminders():
    st.title("Set Pet Reminders")
    st.subheader("Customize reminders for your pet")

    reminder_type = st.selectbox("Reminder Type", ["Feeding", "Vaccination", "Exercise", "Medication"])
    reminder_date = st.date_input("Date")
    reminder_time = st.time_input("Time")
    reminder_notes = st.text_area("Notes", "Don't forget to give treats!")

    if st.button("Set Reminder"):
        # Process the reminder and display it
        st.subheader("Your Pet Reminders:")
        st.write("Reminder: {} on {} at {}. Notes: {}".format(reminder_type, reminder_date.strftime('%B %d, %Y'), reminder_time.strftime('%I:%M %p'), reminder_notes))

def main():
    st.title("Pet Health Portal")

    page = st.sidebar.radio("Navigation", ["Login", "Signup", "Pet Record", "Set Reminders"])

    if page == "Login":
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            # Dummy authentication (no actual authentication)
            if username == "dummyuser" and password == "dummypassword":
                display_pet_record()
            else:
                st.error("Invalid Username or Password")

    elif page == "Signup":
        signup()

    elif page == "Pet Record":
        display_pet_record()

    elif page == "Set Reminders":
        set_reminders()

if __name__ == "__main__":
    main()
