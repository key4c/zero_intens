# Найдите наименьшую обыкновенную дробь, равную вещественному числу 14.375, 
# и выведите ее на экран в формате '14.375 = числитель/знаменатель'

from fractions import Fraction

NUMBER = 14.375

fraction = Fraction(NUMBER).limit_denominator()

print(f"{NUMBER} = {fraction.numerator}/{fraction.denominator}")