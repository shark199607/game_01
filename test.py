def aplusb(self, a, b):
    # write your code here
    self.a=a
    self.b=b
    if self.a == 0:
        return b
    if self.b == 0:
        return a

    x1 = int(a ^ b)
    x2 = int((a & b) << 1)

    aplusb(x1, x2)


aplusb(4,4,7)
