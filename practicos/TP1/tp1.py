import os, argparse

class TextInverter():
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(
            prog = "Text Inverter", 
            description = ("This program inverts the words and their"+
            "order in every line found on the input text file"))
        parser.add_argument("-f", "--file", action = "store", default = "/", 
                            required = True, type = str, help = "Relative file path")
        parser.add_argument("-a", "--absolute", action = "store_true", type = bool, 
                            help = "Use this argument if you want to insert an absolute file path")
        self.args = parser.parse_args()

    def run(self):
        pass

    def mksubp(self):
        pass

    def inverter(self, text):
        pass

if __name__ == "__main__":
    app = TextInverter()
    app.run()
