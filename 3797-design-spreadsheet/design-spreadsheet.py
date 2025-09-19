# How is this considered a medium?
class Spreadsheet:
    def __init__(self, rows: int):
        self.cells = {}
        
    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def referenceToVal(self, x):
        if 65 <= ord(x[0]) <= 90:
            return self.cells.get(x, 0)
        return int(x)

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split("+")
        return self.referenceToVal(x) + self.referenceToVal(y)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)