print("Runner1 : ")
name_runner1 =input("Name: ")
time_runner1 =input("Time (in seconds): ")
print("\nRunner2 : ")
name_runner2 =input("Name: ")
time_runner2 =input("Time (in seconds): ")

if(int(time_runner1) < int(time_runner2)):
    print(f"The faster runner is {name_runner1}")
elif(int(time_runner1) == int(time_runner2)):
    print(f"{name_runner1} and {name_runner2} have the same time")
else:
    print(f"The faster runner is {name_runner2}")