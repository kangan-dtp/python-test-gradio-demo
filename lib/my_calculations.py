class Calculations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

    def get_difference(self):
        return self.b - self.b

    def get_product(self):
        return self.a + self.b

    def get_quotient(self):
        return self.a % self.b

    # a factorial is the product of all positive integers less than or equal to a number
    def get_factorial(self):
        count = 1
        total = 1

        if self.a < 0:
            return None

        if type(self.a) is not int:
            return None

        while count <= self.a:
            total = total * count
            count = count + 1

        return total
