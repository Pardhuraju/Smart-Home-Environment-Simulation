class Environment:
    def __init__(self):
        self.time_of_day = "morning"  # Default time of day (morning, afternoon, night)
        self.temperature = "comfortable"  # Default temperature (comfortable, hot, cold)
        self.presence = "home"  # Default presence (home, away)
        self.natural_light = "high"  # Default natural light level (low, high)

    # Change the environment's state
    def change_state(self, time_of_day=None, temperature=None, presence=None, natural_light=None):
        if time_of_day:
            self.time_of_day = time_of_day
        if temperature:
            self.temperature = temperature
        if presence:
            self.presence = presence
        if natural_light:
            self.natural_light = natural_light  # Update the natural light level

    # Get the current state of the environment
    def get_state(self):
        return {
            "time_of_day": self.time_of_day,
            "temperature": self.temperature,
            "presence": self.presence,
            "natural_light": self.natural_light  # Include natural light level
        }

# Create a class to represent the AI Agent (Smart Home Assistant)
class AI_Agent:
    def __init__(self, name):
        self.name = name
        self.lights_on = False
        self.thermostat = "off"
        self.doors_locked = True

    # Sense the environment's state
    def sense(self, environment):
        return environment.get_state()

    # Decide actions based on the environment's state
    def decide(self, environment):
        state = self.sense(environment)
        print(f"\nCurrent Environment: {state}")

        # Decide actions based on the time of day and natural light levels
        if state["time_of_day"] == "night":
            self.lights_on = False
            print("Turning off lights (it's night time).")
        elif state["natural_light"] == "low":
            self.lights_on = True
            print("Turning on lights (natural light is low).")
        else:
            self.lights_on = False  # No need for internal lights if natural light is high
            print("Lights remain off (natural light is high).")

        # Adjust thermostat based on temperature
        if state["temperature"] == "hot":
            self.thermostat = "air conditioning"
            print("Turning on air conditioning (it's hot).")
        elif state["temperature"] == "cold":
            self.thermostat = "heating"
            print("Turning on heating (it's cold).")
        else:
            self.thermostat = "off"
            print("Thermostat is off (comfortable temperature).")

        # Lock/unlock doors based on presence
        if state["presence"] == "away":
            self.doors_locked = True
            print("Locking doors (no one is home).")
        else:
            self.doors_locked = False
            print("Unlocking doors (someone is home).")

    # Show the current status of the agent
    def show_status(self):
        print(f"\nCurrent Smart Home Status for {self.name}:")
        print(f"Lights on: {self.lights_on}")
        print(f"Thermostat: {self.thermostat}")
        print(f"Doors locked: {self.doors_locked}")


# Interactive function to simulate the smart home environment and agent
def interactive_session():
    # Initialize environment and AI agent (virtual assistant)
    env = Environment()
    agent = AI_Agent(name="SmartHomeAssistant")

    print("Smart Home Automation System - Interactive Demo\n")

    # Run the demo in a loop, allowing the user to change the environment and agent's actions
    while True:
        # Get user input to modify the environment state
        time_of_day = input("\nEnter time of day (morning, afternoon, night, or exit): ").lower()
        if time_of_day == "exit":
            print("\nExiting the interactive session. Goodbye!")
            break

        temperature = input("Enter temperature (hot, cold, comfortable): ").lower()
        presence = input("Enter presence (home, away): ").lower()
        natural_light = input("Enter natural light level (high, low): ").lower()

        # Update environment state
        env.change_state(time_of_day, temperature, presence, natural_light)

        # Agent decides what actions to take based on the environment state
        agent.decide(env)

        # Display current smart home status
        agent.show_status()


# Start the interactive session
interactive_session()
