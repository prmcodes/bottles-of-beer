# Start with 99 bottles of beer
bottles_of_beer = 99

# while loop 'sings' song from 99 bottles to 0 bottles. Edge case of "1 bottles"  needs to be dealt with.
while bottles_of_beer > 0:
  print("{0} bottles of beer on the wall, {0} bottles of beer! Take one down! pass it around! {1} bottles of beer on the wall!".format(bottles_of_beer, (bottles_of_beer-1)))
  bottles_of_beer-=1
