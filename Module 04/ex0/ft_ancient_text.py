if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        fd = open("ancient_fragment.txt", "r")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(fd.read())
        fd.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError as e:
        print("Error: Storage vault not found")
