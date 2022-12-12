import getopt
import subprocess
from sys import argv, exit


def usage():
	print("test.py -h | --help")


def main():
	# get command line arguments
	try:
		opts, args = getopt.getopt(argv[1:], "h", ["help"])
	except getopt.GetoptError as err:
		print(err)
		usage()
		exit(2)
	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
			exit()
		else:
			assert False, "unhandled option"

	# check if user has pip installed
	if not subprocess.call("pip --version", shell=True):
		print("pip is not installed")
		exit(1)

	# check if user has virtualenv installed
	if not subprocess.call("virtualenv --version", shell=True):
		print("virtualenv is not installed")
		exit(1)

	# check if user has python3 installed
	if not subprocess.call("python3 --version", shell=True):
		print("python3 is not installed")
		exit(1)


if __name__ == "__main__":
	main()
