if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initializing secure vault access...")
    try:
        with open("classified_data.txt") as data:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(data.read()a)
        with open("security_protocols.txt") as protocols:
            print("\nSECURITY PROTOCOLS:")
            print(protocols.read())
        print("Vault automatically sealed upon completetion.")
    except FileNotFoundError as Error:
        print(f"Error: Vault access failed. {Error}")
    finally:
        print("\nAll vault operations completed with maximum security.")