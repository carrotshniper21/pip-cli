import npyscreen
import argparse
import subprocess
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    "--view", action="store_true", help="view the output of predator.sh"
)
parser.add_argument(
    "--download",
    action="store_true",
    help="download subtitles using subscene_downloader.py",
)

args = parser.parse_args()

if args.view:
    output = subprocess.check_output(["bash", "predator.sh"])
    values = output.decode("utf-8")
    with open(values, "r") as f:
        lines = f.readlines()

if args.download:
    print("Enter a movie/tv show name: ")
    output = os.popen("python subtitle_downloader.py").read()
    pattern = re.compile(r"\.+[^\n]*\.srt")
    match = pattern.search(output)
    if match:
        subtitle = match.group()
        cleaned_subtitle = subtitle.replace("...", "")
        with open(cleaned_subtitle, "r") as f:
            lines = f.readlines()


class ActionControllerSearch(npyscreen.ActionControllerSimple):
    def create(self):
        self.add_action("^:.*", self.set_search, True)
        self.add_action("^:quit$", self.quit, True)

    def set_search(self, command_line, widget_proxy, live):
        self.parent.value.set_filter(command_line[1:])
        self.parent.wMain.values = self.parent.value.get()
        self.parent.wMain.display()

    def quit(self, command_line, widget_proxy, live):
        exit()

class FmSearchActive(npyscreen.FormMuttActiveTraditional):
    ACTION_CONTROLLER = ActionControllerSearch


for i in range(10):
    try:

        class TestApp(npyscreen.NPSApp):
            def main(self):

                F = FmSearchActive()
                F.wStatus1.value = "Status Line "
                F.wStatus2.value = "Second Status Line "

                F.value.set_values(lines)
                F.wMain.values = F.value.get()

                F.edit()

        if __name__ == "__main__":
            App = TestApp()
            App.run()
    except KeyboardInterrupt:
        break
