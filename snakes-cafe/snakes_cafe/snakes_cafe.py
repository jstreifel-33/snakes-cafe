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

def border_print(message):
  msg_list = message.splitlines()
  msg_width = 0

  for line in msg_list:
    if len(line) > msg_width:
      msg_width = len(line)

  for idx, line in enumerate(msg_list):
    msg_list[idx] = line.center(msg_width + 2, ' ')
  msg_list.insert(0,'')
  msg_list.insert(len(msg_list), '')
  for line in msg_list:
    print(line.center(msg_width + 6, '*'))

border_print(greeting)

border_print(ask_order)

