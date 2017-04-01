class Connect4:
    def __init__(self, width=7, height=6, connect=4):
        self.width = width
        self.height = height
        self.connect = connect
        self.mainArray = []
        self.initMainArray()

    def initMainArray(self):
        if self.connect <= self.width < 100 and self.connect <= self.height < 100:
            self.mainArray = [['.' for _ in range(self.width)] for _ in range(self.height)]
        else:
            raise ValueError

    def display(self):
        for j in range(self.height-1, -1, -1):
            print('|', ' | '.join([str(self.mainArray[j][i]) for i in range(self.width)]), '|')
        print('|', ' - '.join(['-' for _ in range(self.width)]), '|')
        print('|', ' | '.join([str(i) for i in range(self.width)]), '|')

    def setPoint(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.mainArray[x][y] = value
            return True
        else:
            return False

    def getPoint(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.mainArray[x][y] if self.mainArray[x][y] != '.' else None
        else:
            return None


# Initialize connect4 class
connect4 = Connect4(4, 4, 3)

# Update connect4 data
connect4.setPoint(0, 0, 'o')
connect4.setPoint(0, 2, 'x')
connect4.display()
