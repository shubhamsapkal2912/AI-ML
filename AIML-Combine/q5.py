#5

# Simple AI Agent (Temperature Control)

temperature = int(input("Enter room temperature: "))

if temperature > 30:
    print("AI Agent: Turn ON the Air Conditioner")

elif temperature < 20:
    print("AI Agent: Turn ON the Heater")

else:
    print("AI Agent: Temperature is Normal")