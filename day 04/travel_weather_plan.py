destination = input("Enter your travel destination: ")
temperature = float(input("Enter the expected temperature (°C): "))
is_raining = input("Is it expected to rain? (yes/no): ").lower() == "yes"

print("\n--- Travel Weather Planner ---")
print(f"Destination: {destination}")

if temperature >= 30:
    print("Weather: Hot")
    print("Recommendation: Pack light clothes, sunglasses, and stay hydrated.")
elif temperature >= 20:
    print("Weather: Pleasant")
    print("Recommendation: Great weather! Pack comfortable clothes.")
else:
    print("Weather: Cold")
    print("Recommendation: Carry a jacket or warm clothes.")

if is_raining:
    print("Don't forget to carry an umbrella or raincoat.")
else:
    print("No rain expected. Enjoy your trip!")

print("Have a safe journey!")