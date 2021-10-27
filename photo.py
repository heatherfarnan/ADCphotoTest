from PCF8591 import PCF8591

class photo:

  def __init__ (self, address):
    self.PCF = PCF8591(address)

  def readPhoto(self):
    return self.PCF.read(0)
  