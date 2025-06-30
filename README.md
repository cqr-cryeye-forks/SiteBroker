# SiteBroker

SiteBroker is a console‑based passive reconnaissance tool that supports **Python 3.13+**. It collects publicly available information about a target domain—from sub‑domain enumeration and reverse‑IP look‑ups to server banners and potential admin panels—and stores everything in a structured JSON report.

## Quick Start

```bash
git clone https://github.com/yourname/SiteBroker.git
cd SiteBroker
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Full Scan

```bash
python SiteBroker.py --target example.com --all --output report.json
```

## How It Works

SiteBroker performs a sequence of lightweight HTTP and DNS requests to gather as much open data as possible without noisy port scans or brute‑force techniques. Under the hood it uses:

* **Sub‑domain brute‑forcing** — a dictionary of thousands of common prefixes combined with direct HTTP requests; every live host is recorded with its status code.
* **Reverse‑IP look‑ups** — queries to the public HackerTarget and YouGetSignal APIs reveal other domains hosted on the same IP.
* **Cloudflare detection** — analysis of DNS answers and HTTP headers; if Cloudflare is present, the script attempts to uncover the real address via the CrimeFlare database.
* **WHOIS & BrowserSpy** — a standard WHOIS query plus parsing of server details (OS, software, modules) from browserspy.dk.
* **Banner grabbing** — collection of full HTTP header sets to identify technologies and versions.
* **Admin panels & web shells** — probing refined path lists pulled from GitHub Raw; 200/3xx/401 responses are flagged as interesting.
* **DNS diagnostics** — authoritative NS records fetched with dnspython.
* **Basic crawling** — manual link extraction via BeautifulSoup, or optional Google/Bing crawling.
* **Speed measurement** — simple timing of DNS resolution and full page load.

All findings are merged into a single JSON file where each category lives under its own key, ready for SIEM ingestion, graph databases or inclusion in a pentest report.

## Use Cases

* Rapid OSINT snapshot before a penetration test.
* Ongoing monitoring of an expanding attack surface during routine change management.
* Automated recon stage in a CI pipeline for periodic domain checks.


## JSON report format

```json
{
  "subdomains": {
    "subdomains": [
      {
        "url": "http://dima.com",
        "status": 200
      },
      {
        "url": "http://wdima.com",
        "status": 403
      }
    ]
  },
  "admin_panels": [
    {
      "url": "http://example.com/admin/",
      "status": 401
    },
    {
      "url": "http://example.com/wp-admin/",
      "status": 403
    }
  ],
  "reverse_ip": {
    "hacker_target": {
      "domains": [
        "cdh.ag",
        "cleankill.at",
        "www.cleankill.at",
        "max-award.at",
        "www.max-award.at",
        "metalux.at",
        "lass-dinge-entstehen.berlin",
        "tischler.berlin",
        "offroad24.bg",
        "shop.offroad24.bg",
        "www.offroad24.bg",
        "dima.com",
        "www.dima.com",
        "diroll-verpackungen.com",
        "drimhoff.com",
        "elkone.com",
        "ellner-shop24.com",
        "emmerich-brillen.com",
        "emmerich-exclusivbrillen.com",
        "shopware.emmerich-exclusivbrillen.com",
        "ukstructuredproducts.com",
        "ukstructuredproductsassociation.com",
        "ultimate-speaker.com",
        "vipscout.com",
        "vipshuttle.com",
        "voice4leaders.com",
        "wache.com",
        "weismainer.com",
        "welcome-oberfranken.com",
        "xn--orthopdieschfte-5kbg.com",
        "aachener-tischler.de",
        "reifendienst-kiefer.de",
        "reifendienstkiefer.de",
        "rf-fischer.de",
        "robl-cnc.de",
        "rickmers.de",
        "www.rickmers.de",
        "rollen.de",
        "xn--diebrne-d1a.de",
        "xn--bh-ro-kva.de",
        "xn--bhro-0ra.de",
        "xn--c-stber-d1a.de",
        "ichhabediewahl.info",
        "lagemeldung.info",
        "laura-baxter.info"
      ]
    },
    "speed": {
      "dns_time": 0.0003192424774169922,
      "load_time": 2.863710641860962,
      "without_dns": 2.863391399383545
    },
    "nameservers": {
      "nameservers": [
        "ns1.ngate.de.",
        "ns3.ngate.de.",
        "ns2.ngate.de."
      ]
    },
    "manual": {
      "links": [
        "http://dima.com/verband/partnerverbaende.html",
        "http://dima.com/branche/wettbewerbsrecht.html",
        "http://dima.com/mitglieder/ddv-marktplatz.html",
        "http://dima.com/impressum.html",
        "http://dima.com/branche.html",
        "http://dima.com/hans-robert-schmid-wird-ehrenbuerger-der-stadt-offenburg-printus-seit-40-jahren-sponsor-des-alfred-gerardi-gedaechtnispreises.html",
        "http://dima.com/branche/verbraucherdialog.html#c11797",
        "http://dima.com/branche/case-studies.html",
        "http://dima.com/mitglieder/mitglied-werden.html",
        "http://dima.com/events/dialogquartett.html",
        "http://dima.com/mitglieder/mitgliedersuche.html",
        "http://dima.com/verband/75-jahre-ddv.html",
        "http://dima.com/fileadmin/_processed_/e/f/csm_Florian_Vierke_2024_e74be9abf9.png",
        "http://dima.com/events/webcasts.html",
        "http://dima.com/verband/praesidium.html",
        "http://dima.com/fileadmin/_processed_/d/7/csm_ddv-dmv%C3%B6-sdv_9b4b14d985.png",
        "http://dima.com/fileadmin/_processed_/e/0/csm_2025_06_Barrierefreiheit_gkk_c82de02647.png",
        "http://dima.com/index.html",
        "http://dima.com/events/aggp.html",
        "http://dima.com/nachberichte-veranstaltungen/aufzeichnung-des-webcasts-dialogmarketing-neu-gedacht-individuell-orchestriert-wertstiftend.html",
        "http://dima.com/dialogmarketing-neu-gedacht-ddv-dmvoe-und-sdv-legen-neue-branchen-definition-vor.html",
        "http://dima.com/alle-veranstaltungen/webkonferenz-kc-anwender-von-dialogmarketing-im-juni-2025.html",
        "http://dima.com/mitglieder/premium-partner.html",
        "http://dima.com/verband/qualitaet/ddv-mustervertrag-auftragsverarbeitung-und-ddv-verpflichtungserklaerung.html",
        "http://dima.com/fileadmin/_processed_/f/4/csm_richter-grueske_post_5a46039316.jpg",
        "http://dima.com/events/max-award.html",
        "http://dima.com/typo3conf/ext/gojs_flowplayer/assets/gosign_customization.1573659235.css",
        "http://dima.com/neue-studie-e-mail-marketing-benchmarks-2025-technischer-fortschritt-trifft-auf-strategische-luecken.html",
        "http://dima.com/fileadmin/_processed_/8/6/csm_Grafik_KI-Schulung_ohneDatum_v2_5a1f4c5512.png",
        "http://dima.com/Templates/Stylesheets/main.1681388523.css",
        "http://dima.com/nachberichte-veranstaltungen/aufzeichnung-webcast-e-mail-marketing-2025.html",
        "http://dima.com/events/visionaere-im-dialog.html",
        "http://dima.com/verband/geschaeftsstellen.html",
        "http://dima.com/branchentrends-dialogmarketing-neu-gedacht.html",
        "http://dima.com/nachberichte-veranstaltungen/aufzeichnung-webcast-cmc-print-mailing-studie-2025.html",
        "http://dima.com/mitglieder.html",
        "http://dima.com/typo3conf/ext/gojs_jquery_fancybox/Resources/Public/Css/jquery.fancybox.1573659392.css",
        "http://dima.com/fileadmin/_processed_/4/7/csm_Printus-Logo-Footer_c522541f2e.png"
      ],
      "grab_banner": {
        "headers": {
          "Date": "Mon, 30 Jun 2025 07:19:20 GMT",
          "Server": "Apache",
          "Content-Language": "de",
          "Cache-Control": "private, no-store, max-age=0",
          "X-TYPO3-Parsetime": "0ms",
          "Content-Encoding": "gzip",
          "Vary": "Accept-Encoding,User-Agent",
          "Upgrade": "h2,h2c",
          "Connection": "Upgrade, Keep-Alive",
          "Expires": "Mon, 30 Jun 2025 07:19:20 GMT",
          "X-UA-Compatible": "IE=edge",
          "X-Content-Type-Options": "nosniff",
          "Keep-Alive": "timeout=5, max=100",
          "Transfer-Encoding": "chunked",
          "Content-Type": "text/html; charset=utf-8"
        }
      }
    }
  }
}

```
