#user input seconds 
user_seconds = input("please enter number of seconds you wish to convertt") 
num_seconds =  int(user_seconds) 
#calculating the number of hourse 
num_hourse = num_seconds//3600 
num_seconds_left = num_seconds % 3600 
#calculating the number of minutes 
num_minutes = num_seconds_left // 60 
final_seconds = num_seconds_left % 60 
print("hourse=", num_hourse , "minutes = ", num_minutes, "seconds =", final_seconds) 

