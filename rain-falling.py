import sys, math

SURFACE_OF_HEAD = .5   # square feet

def calculate_amount_of_rain(rainfall):
   if rainfall == 1:
      return 1
   elif rainfall == 2:
      return 5
   elif rainfall == 3:
      return 10
   elif rainfall == 4:
      return 15
   elif rainfall == 5:
      return 20
   else:
      return 0
   
def calculate_time_to_destination(speed, distance):
   return math.ceil(distance / speed)   # return time to destination in seconds

def calculate_rain_falling_per_second(height, speed, amount_of_rain):
   return 0.5 * ((height ** 2 + speed ** 2) / height + SURFACE_OF_HEAD) * amount_of_rain
   
def main():
   while True:
      print("\n\n\n\n\n\nThis program calculates the total number of rain drops that will hit you based on a number of factors.")
      print("\n\nWould you like to make another calculation? (y or n)")
      response = input()
      if response == 'n':
         break

      print("What is your height in feet?")
      height = int(input())

      print("How fast are you walking / running in feet per second?")
      speed = int(input())

      print("How hard is it raining on a scale of 1-5? (1=light sprinkling, 5=downpour)")
      rainfall = int(input())

      print("How many feet are you away from shelter from the rain?")
      distance = int(input())

      time_to_destination = calculate_time_to_destination(speed, distance)
      total_rain_fallen = 0

      while time_to_destination > 0:
         total_rain_fallen += calculate_rain_falling_per_second(height, speed, calculate_amount_of_rain(rainfall))
         time_to_destination -= 1

      print(f"\n\nRESULT: If you're walking/running at {speed} feet per second, and it is raining at a scale of {rainfall}, and you are {calculate_time_to_destination(speed, distance)} seconds away from shelter, "
            f"then the total number of raindrops that would hit you is: \n{math.ceil(total_rain_fallen)}")
      
   print("\nThank you for processing rain drops hitting you. Have a nice day! ;)\n\n\n\n\n\n\n")
   sys.exit()
   
main()