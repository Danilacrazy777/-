class Field:
    def __init__(self, size, ships):
      self.size = size
      self.grid = []
      for _ in range(size):
            self.grid.append([None] * size)
      self.ships_alive = ships
