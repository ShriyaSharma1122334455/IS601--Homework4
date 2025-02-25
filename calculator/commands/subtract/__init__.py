from calculator.commands import Command
from decimal import Decimal, InvalidOperation

class SubtractCommand(Command):
    """
    SubtractCommand class for subtracting two numbers.

    This class inherits from the Command class and implements the execute method
    to subtract two numerical arguments.
    """

    def execute(self, *args):
        """
        Executes the subtract command.

        This method takes two arguments, subtracts them, and prints the result. If
        the inputs are invalid, an error message is displayed.
        """
        try:
            a, b = map(Decimal, args)
            difference = a - b
            print(f"The solution of subtraction is {difference}")
        except InvalidOperation:
            print("Error: Invalid input. Please enter valid numbers.")

# Expose the SubtractCommand class for external use
__all__ = ["SubtractCommand"]
