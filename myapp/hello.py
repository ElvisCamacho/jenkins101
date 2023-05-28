import fire

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        """Add two numbers"""
        self.result = x + y
        return self.result

    def divide(self, x, y):
        """Divide two numbers"""
        if y == 0:
            print("Error: Division by zero!")
        else:
            self.result = x / y
            return self.result

if __name__ == '__main__':
    fire.Fire(Calculator)

#import fire

#def hello(name="World"):
#  return "Hello %s!" % name
#
#if __name__ == '__main__':
#  fire.Fire(hello)
