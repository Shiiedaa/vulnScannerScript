import json

def report(host, open_ports, vuln_results):
        report = {
                "host": host,
                "open_ports": open_ports,
                "vulnerabilities": vuln_results
        }

        #save the json report
        filename = f"{host}_report.json"
        with open(filename, "w") as f:
                json.dump(report, f, indent=4)
        print(f"Report saved to {filename}")

def print_report(open_ports, vuln_results):
        print("\n--- Scan Results ---")
        print(f" Open ports: {open_ports}")
        for port, vuln in vuln_results.items():
                print(f"Port {port}: {vuln}")

