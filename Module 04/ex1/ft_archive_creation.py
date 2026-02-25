if __name__ == "__main__":
    content = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist trainee\n"
    ]
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    
    print("Initializing new storage unit: new_discovery.txt")
    file = open("new_discovery.txt", "w")
    print("\nInscribing preservation data...")
    for entry in content:
        file.write(entry)
        print(entry, end="")
    print("\nData inscription complete. Storage unit sealed.")
    file.close()
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
