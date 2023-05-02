import os, argparse, sys

class TextInverter():
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(
            description = "This program inverts the words and their "+
            "order in every line found on the input text file")
        parser.add_argument("-f", "--file", action = "store", required = True, 
                            type = str, help = "Relative file path")
        self.args = parser.parse_args()

    def run(self):
        try:
            file = os.open(self.args.file, os.O_RDONLY)
            lines = os.read(file, 2048).decode().split("\n")
        except FileNotFoundError:
            sys.stdout.write("The file doesn't exist\n")
            sys.exit()
        except IsADirectoryError:
            sys.stdout.write("Must select a file not a directory\n")
            sys.exit()
        pipes = {}
        for child in range(0, len(lines)):
                pipes[child] = os.pipe()
                line = lines[child]
                if line == "":
                    line = "\n"
                os.write(pipes[child][1], line.encode())
                pid = os.fork()
                if pid == 0:
                    line = os.read(pipes[child][0], 2048).decode()
                    os.close(pipes[child][0])
                    line = line[::-1]
                    os.write(pipes[child][1], line.encode())
                    sys.exit()     
        try:        
            while True:
                os.wait()
        except ChildProcessError:
            for pipe in pipes.values():
                line = os.read(pipe[0], 2048).decode()
                if line == "\n":
                    line = ""
                sys.stdout.write(line+"\n")


if __name__ == "__main__":
    app = TextInverter()
    app.run()
