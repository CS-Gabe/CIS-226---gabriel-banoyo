import nmap3
import json


def main():
    
    #Propmpt user for input
    print("Nmap Interactive Scanner")
    print("Should be run with elevated privileges (e.g., administration both for power shell and command line, as sudo, or as root) "
    "for certain scans.")
    host = input("Enter target host IP: ")
    print("\nChoose scan type:")
    print("1. Top 10 Ports Scan")
    print("2. Stealth Scan")
    print("3. OS Detection")
    choice = input("\nEnter choice (1/2/3): ")
    
    # Initialize Nmap based on user choice
    nmap = nmap3.Nmap()
    if choice == '1':
        scan_results = nmap.scan_top_ports(host)
        print("Top 10 Ports Scan Results:")
        print(json.dumps(scan_results, indent=4))
    elif choice == '2':
        scan_results = nmap.nmap_stealth_scan(host)
        print("Stealth Scan Results:")
        print(json.dumps(scan_results, indent=4))
    elif choice == '3':
        scan_results = nmap.nmap_os_detection(host)
        print("OS Detection Results:")
        print(json.dumps(scan_results, indent=4))
    else:
        print("Invalid choice. Please run the script again.")

# Run the main function in a loop to allow multiple scans
if __name__ == "__main__":
    while True:
        main()
        again = input("Scan another host? (y/n): ")
        if again.lower() != 'y':
            print("Exiting Nmap Scanner.")
            break
