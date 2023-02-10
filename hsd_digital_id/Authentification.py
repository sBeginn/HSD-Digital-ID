#Implementation
import streamlit as st
import streamlit_authenticator as stauth

#Help: https://towardsdatascience.com/how-to-add-a-user-authentication-service-in-streamlit-a8b93bf02031

#1. Hashing passwords
credentials:
  usernames:
    jsmith:
      email: jsmith@gmail.com
      name: John Smith
      password: '123' # To be replaced with hashed password
    rbriggs:
      email: rbriggs@gmail.com
      name: Rebecca Briggs
      password: '456' # To be replaced with hashed password
cookie:
  expiry_days: 30
  key: some_signature_key
  name: some_cookie_name
preauthorized:
  emails:
  - melsby@gmail.com
  
#use the Hasher module to convert the plain text passwords into hashed passwords.  
hashed_passwords = stauth.Hasher(['123', '456']).generate()

#2. Creating a login widget
with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

#inally render the login widget as follows
#provide a name for the login form
name, authentication_status, username = authenticator.login('Login', 'main')

#3. Authenticating users
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password') #-> successful Log-In
    
#prompt an unverified user to enter the correct username and password.   
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')
    
#4. Creating a password reset widget
if authentication_status:
    try:
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

#5. Creating a new user registration widget
try:
    if authenticator.register_user('Register user', preauthorization=False):
        st.success('User registered successfully')
except Exception as e:
    st.error(e)   

#6. Creating a forgot password widget
try:
    username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
    if username_forgot_pw:
        st.success('New password sent securely')
        # Random password to be transferred to user securely
    elif username_forgot_pw == False:
        st.error('Username not found')
except Exception as e:
    st.error(e)

#7. Creating a forgot username widget
try:
    username_forgot_username, email_forgot_username = authenticator.forgot_username('Forgot username')
    if username_forgot_username:
        st.success('Username sent securely')
        # Username to be transferred to user securely
    elif username_forgot_username == False:
        st.error('Email not found')
except Exception as e:
    st.error(e)
    
#8. Creating an update user details widget
if authentication_status:
    try:
        if authenticator.update_user_details(username, 'Update user details'):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)
        
#9. Updating the configuration file
with open('../config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)