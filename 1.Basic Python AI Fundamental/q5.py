class AI:
    def check(self, temperature):
        if temperature > 30:
            return "AI Agent: Turn ON the Air Conditioner"
        elif temperature < 20:
            return "AI Agent: Turn ON the Heater"
        else:
            return "AI Agent: Temperature is Normal"


# Usage
temp = int(input("Enter room temperature: "))
obj = AI()
result = obj.check(temp)
print(result)