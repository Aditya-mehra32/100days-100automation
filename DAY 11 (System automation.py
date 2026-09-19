import time

def washing_machine():
    print("=== Haier Washing Machine Simulator ===")

    print("\n1. Door check")
    door_closed = True

    if not door_closed:
        print("ERROR: Door is open!")
        return

    print("Door locked.")

    print("\n2. Filling water...")
    time.sleep(2)
    print("Water level OK")

    print("\n3. Washing...")
    for i in range(5):
        print(f"Washing: {i + 1}/5")
        time.sleep(1)

    print("\n4. Draining water...")
    time.sleep(2)
    print("Water drained.")

    print("\n5. Spinning...")
    for speed in [500, 800, 1000, 1200]:
        print(f"Spin speed: {speed} RPM")
        time.sleep(1)

    print("\n6. Cycle complete!")
    print("Door can now be unlocked.")


washing_machine()
