# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-12T09:13:22.990612+00:00
**Duration:** 44.14s
**Successful:** 18/19

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| SGB (Turkiye) | HttpError: HTTP 429: <html>
<head><title>429 Too Many Requests</title></head>
<body>
<center><h1>429 Too Many Requests</h1></center>
<hr><center>nginx</center>
</body>
</html>
 | 10,000 IPs from cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 57,954 |
| Found in multiple sources | 46,700 |
| Max source overlap | 9 |
| Avg sources per IP | 1.92 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,705 | 27,242 | 53.0% |
| SGB (Turkiye) | 9,782 | 218 | 97.8% |
| Stamparm IPsum | 6,804 | 30,720 | 18.1% |
| CINS Army | 5,826 | 9,174 | 38.8% |
| Spamhaus DROP | 1,698 | 0 | 100.0% |
| BinaryDefense | 1,009 | 3,498 | 22.4% |
| AbuseIPDB | 817 | 9,183 | 8.2% |
| Tor Exit Nodes | 659 | 604 | 52.2% |
| GreenSnow | 346 | 5,066 | 6.4% |
| AlienVault OTX | 163 | 23 | 87.6% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 20 | 23,796 | 0.1% |
| Blocklist.de (strongips) | 18 | 321 | 5.3% |
| Emerging Threats | 13 | 513 | 2.5% |
| Blocklist.de (ssh) | 0 | 7,566 | 0.0% |
| Blocklist.de (mail) | 0 | 12,918 | 0.0% |
| Blocklist.de (apache) | 0 | 9,027 | 0.0% |
| Blocklist.de (bots) | 0 | 1,814 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 851 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,271 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,918 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,274 |
| Blocklist.de (all) & Stamparm IPsum | 10,222 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,027 |
| Stamparm IPsum & AbuseIPDB | 8,281 |
| CINS Army & Stamparm IPsum | 8,184 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,566 |
| RTBH (Turkiye) & AbuseIPDB | 6,917 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 63 | 2026-06-12 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,947 | OK |
| Stamparm IPsum | 37,524 | OK |
| Blocklist.de (all) | 23,816 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,918 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,027 | OK |
| Blocklist.de (ssh) | 7,566 | OK |
| GreenSnow | 5,412 | OK |
| BinaryDefense | 4,507 | OK |
| Blocklist.de (bots) | 1,814 | OK |
| Spamhaus DROP | 1,698 | OK |
| Tor Exit Nodes | 1,263 | OK |
| Blocklist.de (bruteforcelogin) | 851 | OK |
| Emerging Threats | 526 | OK |
| Blocklist.de (strongips) | 339 | OK |
| AlienVault OTX | 186 | OK |
| Spamhaus DROPv6 | 94 | OK |
