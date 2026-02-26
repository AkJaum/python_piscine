import sys


if __name__ == "__main__":
   print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
   id = input("Input Stream active. Enter archivist ID: ")
   report = input("Input Stream active. Enter status report: ")
   sys.stdout.write(f"\n[STANDARD] Archive status from {id}: {report}")
   sys.stderr.write(f"\n[ALERT] System diagnostic: Communication channels verified")
   sys.stdout.write(f"\n[STANDARD] Data transmission complete.\n")
   print("\nThree-channel communication test successful.")