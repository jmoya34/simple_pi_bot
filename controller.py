import inputs #pip install inputs

devices = inputs.devices
print("Connected devices:", devices)

# Read controller events (e.g., button press, axis move)
try:
    while True:
        events = inputs.get_key()
        for event in events:
            print(f"Event: {event.ev_type}, Value: {event.ev_value}")
            
except KeyboardInterrupt:
    print("Exiting...")
