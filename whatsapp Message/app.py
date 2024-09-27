import pywhatkit as pwk

# Function to send WhatsApp message
def send_whatsapp_message(number, message, hour, minute):
    pwk.sendwhatmsg(number, message, hour, minute)

# Taking user input for the phone number, message, and time
def get_user_input():
    number = input("Enter the phone number (with country code): ")
    message = input("Enter the message: ")
    hour = int(input("Enter the hour (24-hour format): "))
    minute = int(input("Enter the minute: "))

    return number, message, hour, minute


# Main function to execute the process
def main():
    number, message, hour, minute = get_user_input()
    send_whatsapp_message(number, message, hour, minute)

if __name__ == "__main__":
    main()
