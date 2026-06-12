# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-12T05:03:57.037368+00:00
**Duration:** 50.1s
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
| Unique to single source | 56,457 |
| Found in multiple sources | 46,556 |
| Max source overlap | 9 |
| Avg sources per IP | 1.94 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,006 | 27,398 | 52.3% |
| SGB (Turkiye) | 9,780 | 220 | 97.8% |
| Stamparm IPsum | 6,921 | 30,603 | 18.4% |
| CINS Army | 4,966 | 10,034 | 33.1% |
| Spamhaus DROP | 1,698 | 0 | 100.0% |
| BinaryDefense | 1,013 | 3,494 | 22.5% |
| AbuseIPDB | 805 | 9,195 | 8.1% |
| Tor Exit Nodes | 659 | 604 | 52.2% |
| GreenSnow | 284 | 5,138 | 5.2% |
| AlienVault OTX | 164 | 24 | 87.2% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 35 | 23,906 | 0.1% |
| Blocklist.de (strongips) | 19 | 321 | 5.6% |
| Emerging Threats | 13 | 513 | 2.5% |
| Blocklist.de (ssh) | 0 | 7,662 | 0.0% |
| Blocklist.de (mail) | 0 | 12,918 | 0.0% |
| Blocklist.de (apache) | 0 | 9,121 | 0.0% |
| Blocklist.de (bots) | 0 | 1,794 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 941 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,184 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,894 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,677 |
| Blocklist.de (all) & Stamparm IPsum | 10,387 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,112 |
| CINS Army & Stamparm IPsum | 9,032 |
| Stamparm IPsum & AbuseIPDB | 8,281 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,651 |
| RTBH (Turkiye) & AbuseIPDB | 6,871 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 62 | 2026-06-12 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,404 | OK |
| Stamparm IPsum | 37,524 | OK |
| Blocklist.de (all) | 23,941 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,918 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,121 | OK |
| Blocklist.de (ssh) | 7,662 | OK |
| GreenSnow | 5,422 | OK |
| BinaryDefense | 4,507 | OK |
| Blocklist.de (bots) | 1,794 | OK |
| Spamhaus DROP | 1,698 | OK |
| Tor Exit Nodes | 1,263 | OK |
| Blocklist.de (bruteforcelogin) | 941 | OK |
| Emerging Threats | 526 | OK |
| Blocklist.de (strongips) | 340 | OK |
| AlienVault OTX | 188 | OK |
| Spamhaus DROPv6 | 94 | OK |
