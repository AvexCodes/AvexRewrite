import chalk
from datetime import datetime

time = datetime.now()

class Logger:
    def __init__(self, write: bool):
        self.write = write

    def log(self, name: str="Main Process", output: str=None):
        if output is None:
            return print(chalk.red(f"{time.strftime('%c')} - [{name}]: No output provided!"))

        print(chalk.white(f"{time.strftime('%c')} - [{name}]: {output}"))

    def success(self, name: str="Main Process", output: str=None):
        if output is None:
            return print(chalk.red(f"{time.strftime('%c')} - [{name}]: No output provided!"))

        print(chalk.green(f"{time.strftime('%c')} - [{name}]: {output}"))

    def error(self, name: str="Main Process", output: str=None):
        if output is None:
            return print(chalk.red(f"{time.strftime('%c')} - [{name}]: No output provided!"))

        print(chalk.red(f"{time.strftime('%c')} - [{name}]: {output}"))

    def warning(self, name: str="Main Process", output: str=None):
        if output is None:
            return print(chalk.red(f"{time.strftime('%c')} - [{name}]: No output provided!"))

        print(chalk.yellow(f"{time.strftime('%c')} - [{name}]: {output}"))