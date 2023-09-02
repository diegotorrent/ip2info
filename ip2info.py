# Author: DFT
# Creation Date: 2023-09-01
# ip2info.py

from builtins import Exception
from myIp import SearchIp, InfoIo

LOG_FILE = "log.txt"


def main():
    try:
        ips = []
        while True:
            print("IPs: ", len(ips))
            op = input("~#: ")

            if op.lower() == "n":
                nil = SearchIp(input("New IP Address: "))
                nil.reverse_ip()
                ips.append(nil)
            if op.lower() == "q":
                break
            if op.lower() == "s":
                for ip in ips:
                    print(ip.show_ip())
            if op == "W":
                print("Saving...")
                with open(LOG_FILE, "a") as fp:
                    for ip in ips:
                        fp.write(str(ip.get_ip()) + "\n")

                print("Data saved.")
            if op.lower() == "c":
                ip = InfoIo(input("New IP Address: "))
                ip.show_ipinfo()
                ips.append(ip)

    except Exception as e:
        print("Exception at main()", e)


if __name__ == "__main__":
    main()

