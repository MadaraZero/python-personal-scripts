"""
Below are some pieces of code that allow for basic physics calculations.
"""

print # for tab
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# Convert fahrenheit to celsius:
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print("100 celsius is {} fahrenheit.".format(f100_in_celsius))

# Convert celsius to fahrenheit:
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print("0 fahrenheit is {} celsius.".format(c0_in_fahrenheit))

# Returns force in Newtons:
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train suppleis %d Newtons of force.") % train_force
print("The GE train supplies {} Newtons of force.".format(train_force))

# Calculating energy:
CONSTANT = 3* 10**8
def get_energy(mass, c):
  return mass * c**2

bomb_energy = get_energy(bomb_mass, CONSTANT)
print("A 1kg bomb supplies {} of Joules.".format(bomb_energy))

# Calculating work:
def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration) * distance
  return work

work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does {} Joules of work over {} meters.".format(work, train_distance))