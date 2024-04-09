
is_engine_running = bool(int(input("Enter 1 if engine is running and 0 if engine is not running:")))

engine_temp = int(input("Enter engine temperature:"))


print("Engine temperature: ", engine_temp, "Grades")


if engine_temp > 80 and is_engine_running is True:
    print("Tunr off the engine")
else :
    print("tunr on the engine")
   
