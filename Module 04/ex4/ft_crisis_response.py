if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        with open("lost_archive.txt") as archive:
            print("")
    except FileNotFoundError:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    try:
        with open("classified_vault.txt") as archive:
            print("")
    except PermissionError:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, system secure\n")
    try:
        with open("standard_archive.txt") as archive:
            print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'")
            print(f"SUCCESS: Archive recovered - ``{archive.read()}''")
            print("STATUS: Normal operations resumed\n")
    finally:
        print("All crisis scenarios handled successfully. Archives secure.")