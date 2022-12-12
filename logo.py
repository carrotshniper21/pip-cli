def pip_logo():
    return (str('''
    ____  ________        ________    ____
   / __ \/  _/ __ \      / ____/ /   /  _/
  / /_/ // // /_/ /_____/ /   / /    / /
 / ____// // ____/_____/ /___/ /____/ /
/_/   /___/_/          \____/_____/___/'''))


def pip_credits():
    return str(('''
    Made by eat my nuts#4595
      Credits to 4ce#6574
'''))


def full_pip_logo():
    return str(pip_logo() + pip_credits())


def ascii_add_blue_color(message):
    blue_opening = '''\033[34m'''
    blue_closing = '''\033[0m '''
    return blue_opening + message + blue_closing


def display_prettier_logo():
    return ascii_add_blue_color(full_pip_logo())
