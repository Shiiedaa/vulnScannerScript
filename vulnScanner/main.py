import argparse
from vulnScanner import scanner, checks, report, utils

# main function for argument parsing and running the scanner
def main():
    # set up argument parser with description
    parser = argparse.ArgumentParser(description="Simple Vulnerability Scanner")

    # add --target argument (required)
    parser.add_argument("--target", required=True, help="Target IP or hostname")

    # add --ports argument (optional, with default ports list)
    parser.add_argument("--ports", default="21,22,23,80,443,8080",
                        help="Comma-separated list of ports to scan")

    # parse the arguments
    args = parser.parse_args()

    # extract target and ports from args
    target = args.target
    ports = [int(p.strip()) for p in args.ports.split(",")]

    # Validate IP or resolve hostname
    if not utils.is_ip_valid(target):
        try:
            import socket
            # try to resolve hostname to IP
            target = socket.gethostbyname(target)
        except socket.gaierror:
            print(f"Could not resolve hostname: {args.target}")
            return

    print(f"Scanning {target} on ports: {ports}")

    # scan the ports
    open_ports = scanner.scan_ports(target, ports)

    # run vulnerability checks for each open port
    vuln_results = {}
    for port in open_ports:
        if port == 21:
            vuln_results[port] = checks.check_ftp_anonymous(target, port)
        elif port == 23:
            vuln_results[port] = checks.check_telnet(target, port)
        elif port in [80, 8080]:
            vuln_results[port] = checks.check_http_banner(target, port)
        else:
            vuln_results[port] = "No vulnerability checks implemented"

    # print results to console
    report.print_report(open_ports, vuln_results)

    # generate JSON report file
    report.report(target, open_ports, vuln_results)

# standard Python entry point
if __name__ == "__main__":
    main()

