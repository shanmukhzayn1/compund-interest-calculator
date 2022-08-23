Principal = 10000
number_of_times = 12
rate = 0.08

time = int(input("Compound for how many years? "))

final = Principal * ( ((1 + (rate/number_of_times)) ** (number_of_times * time)) )

print ("The final amount after", t, "years is", final)
