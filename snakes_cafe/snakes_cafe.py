# **************************************
# **    Welcome to the Snakes Cafe!   **
# **    Please see our menu below.    **
# **
# ** To quit at any time, type "quit" **
# **************************************

# Appetizers
# ----------
# Wings
# Cookies
# Spring Rolls

# Entrees
# -------
# Salmon
# Steak
# Meat Tornado
# A Literal Garden

# Desserts
# --------
# Ice Cream
# Cake
# Pie

# Drinks
# ------
# Coffee
# Tea
# Unicorn Tears

# ***********************************
# ** What would you like to order? **
# ***********************************
# >

# header = '''**************************************
# **    Welcome to the Snakes Cafe!   **
# **    Please see our menu below.    **
# **
# ** To quit at any time, type "quit" **
# **************************************
# '''

greeting = '''Welcome to the Snakes Cafe!
Please see our menu below. 

To quit at any time, type "quit"'''

ask_order = 'What would you like to order?'

order_confirm = '{} order of {} have been added to your meal'

menu={
  'Appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
  'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
  'Desserts': ['Ice Cream', 'Cake', 'Pie'],
  'Drinks': ['Coffee', 'Tea', 'Unicorn Tears'],
}

user_order={}



def border_print(message, top_bott_bord=True):
  msg_list = message.splitlines()
  msg_width = 0

  #Determine max width line in message
  for line in msg_list:
    if len(line) > msg_width:
      msg_width = len(line)

  #Center lines based on pax width with 2 char whitepace padding
  for idx, line in enumerate(msg_list):
    msg_list[idx] = line.center(msg_width + 2)

  #Insert blank strings to list if top/bottom border not set False
  if top_bott_bord:
    msg_list.insert(0,'')
    msg_list.insert(len(msg_list), '')

  #Print each line of message, with added stars on side borders
  for line in msg_list:
    print(line.center(msg_width + 6, '*'))
  
  #White space
  print('')

def show_menu():
  for category in menu:
    print(category)
    print(''.center(len(category), '-'))
    for item in menu[category]:
      print(item)
    print('')

border_print(greeting)
show_menu()
border_print(ask_order)
