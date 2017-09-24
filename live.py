import time
class LivingCreature ():
  def __init__ (self):
    self.newl()
  def newl (self):
    self.setEn(100)
    self.genome = {}
    self.x = 0
    self.y = 0

  def setEn (self,en):
    if en <= 100:
      if en >= 0:
        self.en = en
      else:
        self.en = 0
    else:
      self.en = 100

  def changeEn(dEn):
      self.setEn(self.en+dEn)


class Gen ():
  info = "Описание гена"
  needEn = 0
  def __init__ (self):
    self.amount = 0

class GenSolarEnergy(Gen):
  info = "Способность усваивать солнечную энергию"
  def __init__(self):
    super().__init__()

class GenMoving (Gen):
  info = "Способность двигатся"
  needEn = 10
  def __init__(self):
    super().__init__()

class GenFeel (Gen):
  info = "Способность чувствовать добычу"
  needEn = 1
  def __init__(self):
    super().__init__()

class GenEat (Gen):
  info = "Способность есть"
  needEn = 1
  def __init__(self):
    super().__init__()

class GenDigestPlant (Gen):
  info = "Способность переваривать растения"
  needEn = 1
  def __init__(self):
    super().__init__()

class GenProtection (Gen):
  info = "Способность защищаться"
  needEn = 10
  def __init__(self):
    super().__init__()

