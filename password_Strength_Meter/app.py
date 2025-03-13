import streamlit as st
import re
import random

st.title("🔐 Password Security Meter")
st.subheader("Fortify your passwords and secure your digital world! 🔐💪")

# Blacklist of common weak passwords
weak_passwords = ["password", "123456", "qwerty", "letmein", "abc123", "password123", "admin", "12345678"]

password=st.text_input("",placeholder="Enter your secret key... 🔑",type="password")


#checking password strength
def check_pass_strength(password):
    strength = 0
    message =[]
    if len(password) >= 8:
        strength += 1
    else:
        message.append("❌ Password should be at least 8 characters long.")    

#upper and lower case
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        strength += 1
    else:
        message.append("Include  both upper and lower case")

#Digits
    if re.search(r"[0-9]",password):
        strength += 1
    else:
        message.append("Include at least one digit")

#Symbols
    if re.search(r"[!@#$%^&*]",password):
        strength += 1
    else:
        message.append("Have one special character (!@#$%^&*)")     

#Scoring system
    if strength == 4:
        message.append("Strong password")   
    elif strength == 3:
       message.append("⚠️ Moderate Password - Consider adding more security features.")    
    else:
        message.append("❌ Weak Password - Improve it using the suggestions above.")  

    return message

#feedback
if password:    
  feedback = check_pass_strength(password) 
  for msg in feedback:
   st.write(msg)       

expander = st.expander("⚡PassGuard Analyzer")

expander.write("Set Password Length")
pass_len = expander.slider("", min_value=8, max_value=32, value=16)
expander.write("Character Types:")
lower_case = expander.checkbox("Lowercase (a-z)")
upper_case = expander.checkbox("Uppercase (A-Z)")
num = expander.checkbox("Numbers (0-9)")
symbols = expander.checkbox("Symbols (!@#$%^&*)")


#password generator
def pass_generate(length):
    pass_characters = ""
    if lower_case:
        pass_characters += "abcdefghijklmnopqrstuvwxyz"
    if upper_case:
        pass_characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num:
        pass_characters += "0123456789"   
    if symbols:
        pass_characters += "!@#$%^&*"    
    if not pass_characters:
        return"❌ Please select at least one character type" 
    return "".join(random.choice(pass_characters) for _ in range(length))  
    
if expander.button("Generate Strong Password"):
    new_pass = pass_generate(pass_len)
    expander.write(f"🎉 Your Secure Password: `{new_pass}`")