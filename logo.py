def logo():
    return (str('''
    ____  ________        ________    ____
   / __ \/  _/ __ \      / ____/ /   /  _/
  / /_/ // // /_/ /_____/ /   / /    / /
 / ____// // ____/_____/ /___/ /____/ /
/_/   /___/_/          \____/_____/___/'''))


def credits():
    return str(('''
      Made by eat my nuts#4595
        Credits to 4ce#6574
'''))


def full_logo():
    return str(logo() + credits())


def ascii_add_blue_color(message):
    blue_opening = '''\033[34m'''
    blue_closing = '''\033[0m '''
    return blue_opening + message + blue_closing


def display_message():
    return ascii_add_blue_color(full_logo())
