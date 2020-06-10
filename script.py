class Business:
  def __init__ (self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address + "is a Franchise location"
  
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return self.name + " is available from " + str(self.start_time) + " to " + str(self.end_time)
  
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

brunch1 = Menu("Brunch Menu", brunch, 11, 16)
early_bird1 = Menu("Early Bird Menu", early_bird, 15, 18)
dinner1 = Menu("Dinner Menu", dinner, 17, 23)
kids1 = Menu("Kids Menu", kids, 11, 22)

menus = [brunch1, early_bird1, dinner1, kids1]


flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
franchises = [flagship_store, new_installment]

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu1 = Menu("Take a' Arepa", arepas_menu, 10, 20)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu1)
Take_a_arepa = Business("Basta Fazoolin' with my Heart", franchises)


print(brunch1)
print(brunch1.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird1.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))


