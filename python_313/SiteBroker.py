from python_313.insides.colors import b, r, y, g, c, w
from python_313.insides.footer import footer
from python_313.insides.functions import addHTTP, write
from python_313.modules.adminpanel import findAdminPanel
from python_313.modules.banner import grabBanner
from python_313.modules.browserspy import browserspyRep
from python_313.modules.cloudflare import cloudflare
from python_313.modules.crawler import googleCrawl, bingCrawl, manualCrawl
from python_313.modules.nameservers import nameServers
from python_313.modules.reverseip import reverseViaYGS, reverseViaHT
from python_313.modules.shells import findShells
from python_313.modules.subdomains import findSubdomains
from python_313.modules.webspeed import websiteSpeed
from python_313.modules.whois import whoIS

line = "-" * 256

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"

header = {"User-Agent": user_agent}

val_select = f"\t{r}[$] Please Use The Index From The List\n\t\t[+] Not By Your Choice :/\n\n"

str_index = f"\n{r}[-] Please Input an Integer (e.g., 1, 2, 3):\n\n"


def get_index() -> int:
    """Prompts user for an integer index."""
    try:
        index = input(f"{c}[-] Select an Option (e.g., 1, 2, 3): ")
        return int(index)
    except ValueError:
        raise ValueError(str_index)


def print_heading(heading: str, website: str, color: str, after_web_head: str) -> None:
    """Prints a formatted heading for the scan."""
    var = f" {heading} '{website}'{after_web_head} ..."
    length = len(var) + 1
    print(f"\n{w}{'-' * length}")
    print(f"{color}{var}")
    print(f"{w}{'-' * length}\n")

try:
    # print(Banner)  # Ensure Banner is defined in insides
    website = input(
        "\n{blue}[$] Please Enter The Website You Want To Scan {red}(i.e, hackthissite.org, hack.me): {none}".format(
            blue=b, red=r, none=y))
    website = addHTTP(website)

    print(
        "\n{green}[@] What You Wanna Do With The Given Website ? \n\n1). Cloudflare Check / Bypass. \n2). Website Crawler.\n3). Reverse IP.\n4). Information Gathering.\n5). Nameservers.\n6). WebSite Speed.\n7). Subdomains Scanner.\n8). Shell Finder.\n9). Admin Panel Finder.\n10). Grab Banner.\n11). All Things.\n".format(
            green=g))

    index = get_index()

    if index == 1:
        print_heading(heading="Checking For Cloudflare Bypass Of", website=website, after_web_head="", color=c)
        cloudflare(website, _verbose=True)

    elif index == 2:
        print(
            "\n{}[$] With Which Method You Wanna Crawl ?\n\n{}1). Google Based Crawler. \n{}2). Bing Based Crawler.\n{}3). Manual Crawler.\n{}4). All Things.\n".format(
                b, g, y, c, r))
        _index = get_index()

        if _index == 1:
            print_heading(heading="Crawling", website=website, after_web_head=" Via Google", color=c)
            googleCrawl(website)

        elif _index == 2:
            print_heading(heading="Crawling", website=website, after_web_head=" Via Bing (might take some time)", color=b)
            bingCrawl(website)

        elif _index == 3:
            print_heading(heading="Crawling", website=website, after_web_head=" Manually :)", color=c)
            manualCrawl(website)

        elif _index == 4:
            print_heading(heading="Crawling", website=website, after_web_head=" Via Google", color=c)
            googleCrawl(website)

            print_heading(heading="Crawling", website=website, after_web_head=" Via Bing (might take some time)", color=b)
            bingCrawl(website)

            print_heading(heading="Crawling", website=website, after_web_head=" Manually :)", color=c)
            manualCrawl(website)

        else:
            raise ValueError(val_select)

    elif index == 3:
        print(
            "\n{}[$] With Which Method You Wanna Do Reverse IP ?\n\n{}1). Hacker Target Based. \n{}2). YouGetSignal Based.\n{}3). All Things.\n".format(
                b, g, y, c))
        _index = get_index()

        if _index == 1:
            print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via HT <3", color=g)
            reverseViaHT(website)

        elif _index == 2:
            print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via YGS!", color=c)
            reverseViaYGS(website)

        elif _index == 3:
            print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via HT <3", color=g)
            reverseViaHT(website)

            print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via YGS!", color=c)
            reverseViaYGS(website)

        else:
            raise ValueError(val_select)

    elif index == 4:
        print(
            "\n{}[$] With Which Method You Wanna Do Information Gathering ?\n\n{}1). Whois Lookup. \n{}2). BrowserSpy Report.\n{}3). All Things.\n".format(
                g, b, y, c))
        _index = get_index()

        if _index == 1:
            print_heading(heading="Doing Whois Lookup OF", website=website, after_web_head="", color=w)
            whoIS(website)

        elif _index == 2:
            print_heading(heading="Generating BrowserSpyReport Of", website=website, after_web_head="", color=w)
            browserspyRep(website)

        elif _index == 3:
            print_heading(heading="Doing Whois Lookup OF", website=website, after_web_head="", color=w)
            whoIS(website)

            print_heading(heading="Generating BrowserSpyReport Of", website=website, after_web_head="", color=w)
            browserspyRep(website)

        else:
            raise ValueError(val_select)

    elif index == 5:
        print_heading(heading="Finding Nameservers Of", website=website, after_web_head="", color=w)
        nameServers(website)

    elif index == 6:
        print_heading(heading="Finding Loading Speed Of", website=website, after_web_head="", color=r)
        websiteSpeed(website)

    elif index == 7:
        print_heading(heading="Finding SubDomains Of", website=website, after_web_head="", color=c)
        findSubdomains(website)

    elif index == 8:
        print_heading(heading="Finding Shells Of", website=website, after_web_head="", color=c)
        findShells(website)

    elif index == 9:
        print_heading(heading="Finding Admin Panel Of", website=website, after_web_head="", color=c)
        findAdminPanel(website)

    elif index == 10:
        print_heading(heading="Grabbing Banner Of", website=website, after_web_head="", color=g)
        grabBanner(website)

    elif index == 11:
        print_heading(heading="Checking For Cloudflare Bypass Of", website=website, after_web_head="", color=y)
        cloudflare(website, _verbose=True)

        print_heading(heading="Crawling", website=website, after_web_head=" Via Google", color=c)
        googleCrawl(website)

        print_heading(heading="Crawling", website=website, after_web_head=" Via Bing (might take some time)", color=b)
        bingCrawl(website)

        print_heading(heading="Crawling", website=website, after_web_head=" Manually :)", color=c)
        manualCrawl(website)

        print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via HT <3", color=g)
        reverseViaHT(website)

        print_heading(heading="Doing Reverse IP OF", website=website, after_web_head=" Via YGS!", color=c)
        reverseViaYGS(website)

        print_heading(heading="Doing Whois Lookup OF", website=website, after_web_head=" Via WApi", color=w)
        whoIS(website)

        print_heading(heading="Generating BrowserSpyReport Of", website=website, after_web_head="", color=w)
        browserspyRep(website)

        print_heading(heading="Finding Nameservers Of", website=website, after_web_head="", color=w)
        nameServers(website)

        print_heading(heading="Finding Loading Speed Of", website=website, after_web_head="", color=r)
        websiteSpeed(website)

        print_heading(heading="Finding SubDomains Of", website=website, after_web_head="", color=c)
        findSubdomains(website)

        print_heading(heading="Finding Shells Of", website=website, after_web_head="", color=c)
        findShells(website)

        print_heading(heading="Finding Admin Panel Of", website=website, after_web_head="", color=c)
        findAdminPanel(website)

        print_heading(heading="Grabbing Banner Of", website=website, after_web_head="", color=g)
        grabBanner(website)

    else:
        raise ValueError(val_select)

except KeyboardInterrupt:
    write(var="~", color=w, data="Err0r: User Interrupted!")
except Exception as e:
    write(var="#", color=r,
          data=f"Err0r: Kindly Report the err0r below to An0n 3xPloiTeR :) (If Your Internet's Working ;)\n\"\"\"\n{str(e)}\n\"\"\"")

print(footer)  # Ensure Footer is defined in insides
