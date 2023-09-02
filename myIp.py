# Author: DFT
# Creation Date: 2023-09-01
# myIp.py

import socket
import requests


class MyIp:
    def __init__(self, ip=None, hostname=None, asn=None, city=None, region=None, country=None, loc=None, org=None, postal=None, timezone=None):
        self.ip = ip
        self.hostname = hostname
        self.asn = asn
        self.city = city
        self.region = region
        self.country = country
        self.loc = loc
        self.org = org
        self.postal = postal
        self.timezone = timezone

    def show_ip(self):
        try:
            print(
                "IP INFO\nip", self.ip, "\n",
                "hostname", self.hostname, "\n",
                "asn", self.asn, "\n",
                "city", self.city, "\n",
                "region", self.region, "\n",
                "country", self.country, "\n",
                "loc", self.loc, "\n",
                "org", self.org, "\n",
                "postal", self.postal, "\n",
                "timezone", self.timezone, "\n")
        except Exception as e:
            print("Exception at show_ip()", e)
        pass

    def get_ip(self):
        try:
            return (
                "ip", self.ip,
                "hostname", self.hostname,
                "asn", self.asn,
                "city", self.city,
                "region", self.region,
                "country", self.country,
                "loc", self.loc,
                "org", self.org,
                "postal", self.postal,
                "timezone", self.timezone)
        except Exception as e:
            print("Exception at get_ip()", e)
        pass


class SearchIp(MyIp):
    def __init__(self, ip=None, hostname=None, asn=None, city=None, region=None, country=None, loc=None, org=None, postal=None, timezone=None):
        super().__init__(ip, hostname, asn, city, region, country, loc, org, postal, timezone)

    def reverse_ip(self):
        try:
            print("Checking the reverse IP of ", self.ip)
            s = socket.gethostbyaddr(self.ip)
            if self.hostname is not None:
                print("The actual hostname is: ", self.hostname)
                if len(s) and input("Replace with: " + str(s[0]) + " [Y/n] ").upper() == "Y":
                    self.hostname = str(s[0])
            elif len(s):
                self.hostname = str(s[0])
            else:
                self.hostname = "?"
            print("The actual hostname is: ", self.hostname)

        except Exception as e:
            print("Exception at reverseIp()", e)
        pass


class InfoIo(MyIp):
    def __init__(self, ip=None, hostname=None, asn=None, city=None, region=None, country=None, loc=None, org=None, postal=None, timezone=None):
        super().__init__(ip, hostname, asn, city, region, country, loc, org, postal, timezone)

    def show_ipinfo(self):
        # https://ipinfo.io/IP/json
        print("Checking https://ipinfo.io/", self.ip)
        try:
            response = requests.request("GET", "https://ipinfo.io/"+str(self.ip)+"/json")
            result = response.json()
            if len(result):
                self.hostname = result.get("hostname", None)
                self.city = result.get("city", None)
                self.region = result.get("region", None)
                self.country = result.get("country", None)
                self.loc = result.get("loc", None)
                self.org = result.get("org", None)
                self.postal = result.get("postal", None)
                self.timezone = result.get("timezone", None)
        except Exception as e:
            print("Exception at show_ipinfo()", e)
        pass
