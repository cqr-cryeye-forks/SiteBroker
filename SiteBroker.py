#####################################################################################################
        ################################   Importing Packages   ################################ 
#####################################################################################################

import argparse
import json

from insides.banner import banner
from insides.footer import footer
from insides.functions import addHTTP
from insides.colors import colors
from modules.adminpanel import findAdminPanel
from modules.grab_banner import grabBanner
from modules.browserspy import browserspyRep
from modules.cloudflare import cloudflare
from modules.crawler import googleCrawl, bingCrawl, manualCrawl
from modules.nameservers import nameServers
from modules.reverseip import reverseViaHT, reverseViaYGS
from modules.shells import findShells
from modules.subdomains import findSubdomains
from modules.webspeed import websiteSpeed
from modules.whois import whoIS

#####################################################################################################
        ################################   Some Variables!   ################################ 
#####################################################################################################

line = "-" * 256

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

header = {"User-Agent": user_agent}

val_select = f"\t{colors.r}[$] Please Use The Index From The List\n\t\t[+] Not By Your Choice :/\n\n"

str_index = f"\n{colors.r}[-] Please Input an Integer (e.g., 1, 2, 3):\n\n"

#####################################################################################################
        ################################   Built-IN Functions   ################################ 
#####################################################################################################

def print_heading(heading: str, website: str, color: str, after_web_head: str) -> None:
    """Prints a formatted heading for the scan."""
    var = f" {heading} '{website}'{after_web_head} ..."
    length = len(var) + 1
    print(f"\n{colors.w}{'-' * length}")
    print(f"{color}{var}")
    print(f"{colors.w}{'-' * length}\n")

#####################################################################################################
        ################################   Argument Parser Setup   ################################ 
#####################################################################################################

def parse_args() -> argparse.Namespace:
    """Parses command-line arguments for the SiteBroker tool."""
    parser = argparse.ArgumentParser(
        description="SiteBroker: A website scanning tool",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("website", help="Target website (e.g., google.com)")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--cloudflare", action="store_true", help="Check and bypass Cloudflare")
    group.add_argument("--crawler", choices=["google", "bing", "manual", "all"], 
                       help="Crawl website (google, bing, manual, or all)")
    group.add_argument("--reverse-ip", choices=["ht", "ygs", "all"], 
                       help="Perform reverse IP lookup (ht, ygs, or all)")
    group.add_argument("--info", choices=["whois", "browserspy", "all"], 
                       help="Gather information (whois, browserspy, or all)")
    group.add_argument("--nameservers", action="store_true", help="Find nameservers")
    group.add_argument("--speed", action="store_true", help="Measure website speed")
    group.add_argument("--subdomains", action="store_true", help="Scan for subdomains")
    group.add_argument("--shells", action="store_true", help="Find shells")
    group.add_argument("--admin", action="store_true", help="Find admin panel")
    group.add_argument("--banner", action="store_true", help="Grab server banner")
    group.add_argument("--all", action="store_true", help="Run all scans")

    return parser.parse_args()


def scan_website(target):
    return {
        "subdomains": findSubdomains(target),
        "whois": whoIS(target),
        "admin_panels": findAdminPanel(target),
        "reverse_ip": {
            "hacker_target": reverseViaHT(target),
            "you_get_signal": reverseViaYGS(target)
        },
        "speed": websiteSpeed(target),
        "server_info": browserspyRep(target),
        "shells": findShells(target),
        "cloudflare": cloudflare(target),
        "nameservers": nameServers(target),
        "crawling": {
            "google": googleCrawl(target),
            "bing": bingCrawl(target),
            "manual": manualCrawl(target),
        "grab_banner": grabBanner(target),
        }
    }


#####################################################################################################
        ################################   Main Function   ################################ 
#####################################################################################################

def main() -> None:
    """Main function to run the SiteBroker scanning tool."""
    try:
        # print(banner)  # Ensure Banner is defined in insides
        args = parse_args()
        website = addHTTP(args.website)

        if args.cloudflare:
            print_heading(heading="Checking For Cloudflare Bypass Of", website=website, after_web_head="", color=colors.c)
            cloudflare(website)

        elif args.crawler:
            if args.crawler == "google":
                print_heading(heading="Crawling", website=website, after_web_head=" Via Google", color=colors.c)
                googleCrawl(website)
            elif args.crawler == "bing":
                print_heading(heading="Crawling", website=website, after_web_head=" Via Bing (might take some time)", color=colors.b)
                bingCrawl(website)
            elif args.crawler == "manual":
                print_heading(heading="Crawling", website=website, after_web_head=" Manually", color=colors.c)
                manualCrawl(website)
            elif args.crawler == "all":
                print_heading(heading="Crawling", website=website, after_web_head=" Via Google", color=colors.c)
                googleCrawl(website)
                print_heading(heading="Crawling", website=website, after_web_head=" Via Bing (might take some time)", color=colors.b)
                bingCrawl(website)
                print_heading(heading="Crawling", website=website, after_web_head="Manually", color=colors.c)
                manualCrawl(website)

        elif args.reverse_ip:
            if args.reverse_ip == "ht":
                print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via HT", color=colors.g)
                reverseViaHT(website)
            elif args.reverse_ip == "ygs":
                print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via YGS", color=colors.c)
                reverseViaYGS(website)
            elif args.reverse_ip == "all":
                print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via HT", color=colors.g)
                reverseViaHT(website)
                print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via YGS", color=colors.c)
                reverseViaYGS(website)

        elif args.info:
            if args.info == "whois":
                print_heading(heading="Doing Whois Lookup Of", website=website, after_web_head="", color=colors.w)
                whoIS(website)
            elif args.info == "browserspy":
                print_heading(heading="Generating BrowserSpyReport Of", website=website, after_web_head="", color=colors.w)
                browserspyRep(website)
            elif args.info == "all":
                print_heading(heading="Doing Whois Lookup Of", website=website, after_web_head=" Via WApi", color=colors.w)
                whoIS(website)
                print_heading(heading="Generating BrowserSpyReport Of", website=website, after_web_head="", color=colors.w)
                browserspyRep(website)

        elif args.nameservers:
            print_heading(heading="Finding Nameservers Of", website=website, after_web_head="", color=colors.w)
            nameServers(website)

        elif args.speed:
            print_heading(heading="Finding Loading Speed Of", website=website, after_web_head="", color=colors.r)
            websiteSpeed(website)

        elif args.subdomains:
            print_heading(heading="Finding Subdomains Of", website=website, after_web_head="", color=colors.c)
            findSubdomains(website)

        elif args.shells:
            print_heading(heading="Finding Shells Of", website=website, after_web_head="", color=colors.c)
            findShells(website)

        elif args.admin:
            print_heading(heading="Finding Admin Panel Of", website=website, after_web_head="", color=colors.c)
            findAdminPanel(website)

        elif args.banner:
            print_heading(heading="Grabbing Banner Of", website=website, after_web_head="", color=colors.g)
            grabBanner(website)

        elif args.all:
            # print_heading(heading="Checking For Cloudflare Bypass Of", website=website, after_web_head="", color=colors.y)
            # cloudflare(website)
            # print_heading(heading="Crawling", website=website, after_web_head=" Via Google", color=colors.c)
            # googleCrawl(website)
            # print_heading(heading="Crawling", website=website, after_web_head=" Via Bing (might take some time)", color=colors.b)
            # bingCrawl(website)
            # print_heading(heading="Crawling", website=website, after_web_head=" Manually", color=colors.c)
            # manualCrawl(website)
            # print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via HT", color=colors.g)
            # reverseViaHT(website)
            # print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via YGS", color=colors.c)
            # reverseViaYGS(website)
            # print_heading(heading="Doing Whois Lookup Of", website=website, after_web_head=" Via WApi", color=colors.w)
            # whoIS(website)
            # print_heading(heading="Generating BrowserSpyReport Of", website=website, after_web_head="", color=colors.w)
            # browserspyRep(website)
            # print_heading(heading="Finding Nameservers Of", website=website, after_web_head="", color=colors.w)
            # nameServers(website)
            # print_heading(heading="Finding Loading Speed Of", website=website, after_web_head="", color=colors.r)
            # websiteSpeed(website)
            # print_heading(heading="Finding Subdomains Of", website=website, after_web_head="", color=colors.c)
            # findSubdomains(website)
            # print_heading(heading="Finding Shells Of", website=website, after_web_head="", color=colors.c)
            # findShells(website)
            # print_heading(heading="Finding Admin Panel Of", website=website, after_web_head="", color=colors.c)
            # findAdminPanel(website)
            # print_heading(heading="Grabbing Banner Of", website=website, after_web_head="", color=colors.g)
            # grabBanner(website)


            # Пример использования
            result = scan_website("dima.com")
            with open("scan_results.json", "w") as f:
                json.dump(result, f, indent=2)

        print(footer)

    except KeyboardInterrupt:
        print(f"{colors.w}[-] Err0r: User Interrupted!")

if __name__ == "__main__":
    main()