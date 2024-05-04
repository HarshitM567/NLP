import re

def process_input(user_input):
    # Define regular expressions to match different user inputs
    name_pattern = r'my\s+name\s+is\s+(\w+)'
    order_pattern = r'(?:order\s+#?|order\s+number\s+is\s+)(\d{10})'
    mobile_email_pattern = r'(?:mobile\s+(?:#\s+)?(\+\d{12})|email\s+id\s+(\S+@\S+\.\w+))'
    otp_pattern = r'(\d{4})\s+(\d{5})'
    complain_pattern = r'complain\s*[:\-\s]+(.+)'

    # Match user input with regular expressions
    name_match = re.search(name_pattern, user_input, re.IGNORECASE)
    order_match = re.search(order_pattern, user_input, re.IGNORECASE)
    mobile_email_match = re.search(mobile_email_pattern, user_input, re.IGNORECASE)
    otp_match = re.search(otp_pattern, user_input)
    complain_match = re.search(complain_pattern, user_input, re.IGNORECASE)

    # Process user input based on matched patterns
    if name_match:
        name = name_match.group(1)
        return f"Hi {name}. Can I get your order number?"
    elif order_match:
        order_number = order_match.group(1)
        return f"Your order is {order_number}. Enter your registered mobile number and mail id for OTP."
    elif mobile_email_match:
        mobile = mobile_email_match.group(1)
        email = mobile_email_match.group(2)
        return f"Enter the 4-digit mobile OTP and 5-digit email OTP for {mobile} and {email}."
    elif otp_match:
        mobile_otp = otp_match.group(1)
        email_otp = otp_match.group(2)
        return f"Thanks for user verification. Please enter your complain."
    elif complain_match:
        complain = complain_match.group(1)
        return f"We have registered your complain. Thanks."
    else:
        return "I'm sorry, I couldn't understand that. Please provide valid input."

# Test the chatbot
conversation = [
    "hi",
    "my name is John",
    "order #0987654321",
    "mobile +917654321576 email abc@mye.com",
    "4444 88888",
    "the product overheated after continuous usage of four hours"
]

for utterance in conversation:
    bot_response = process_input(utterance)
    print(f"User: {utterance}")
    print(f"Bot: {bot_response}\n")