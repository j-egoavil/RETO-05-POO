class Shape():
   def __init__(self, is_regular: bool):
      self.is_regular = is_regular
      self.vertices: list = []
      self.edges: list = []
        
   def compute_area(self):
      return 0
    
   def compute_perimeter(self):
      if not self.edges:
            return 0
      else:
         for edge in self.edges:
            perimeter = sum(edge.compute_length() for edge in self.edges)
         return perimeter
    
   def inner_angle(self, sides: int) -> float:
      if sides < 3:
            return 0
      return (sides - 2) * 180 / sides # Average inner angle in degrees
    
   def compute_inner_angles(self):
        sides = len(self.vertices)
        if sides < 3:
            return 0
        return (sides-2) * 180