# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-12T12:32:09.691452+00:00
**Duration:** 35.64s
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
| Unique to single source | 58,538 |
| Found in multiple sources | 46,403 |
| Max source overlap | 8 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,205 | 27,059 | 53.6% |
| SGB (Turkiye) | 9,781 | 219 | 97.8% |
| Stamparm IPsum | 7,036 | 30,488 | 18.8% |
| CINS Army | 5,678 | 9,322 | 37.9% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,010 | 3,497 | 22.4% |
| AbuseIPDB | 808 | 9,192 | 8.1% |
| Tor Exit Nodes | 658 | 605 | 52.1% |
| GreenSnow | 357 | 4,115 | 8.0% |
| AlienVault OTX | 163 | 23 | 87.6% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 20 | 23,705 | 0.1% |
| Blocklist.de (strongips) | 18 | 321 | 5.3% |
| Emerging Threats | 13 | 513 | 2.5% |
| Blocklist.de (ssh) | 0 | 7,532 | 0.0% |
| Blocklist.de (mail) | 0 | 12,912 | 0.0% |
| Blocklist.de (apache) | 0 | 9,023 | 0.0% |
| Blocklist.de (bots) | 0 | 1,767 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 845 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,316 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,912 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,059 |
| Blocklist.de (all) & Stamparm IPsum | 10,093 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,023 |
| CINS Army & Stamparm IPsum | 8,284 |
| Stamparm IPsum & AbuseIPDB | 8,281 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,532 |
| RTBH (Turkiye) & AbuseIPDB | 6,930 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 64 | 2026-06-12 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 58,264 | OK |
| Stamparm IPsum | 37,524 | OK |
| Blocklist.de (all) | 23,725 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,912 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,023 | OK |
| Blocklist.de (ssh) | 7,532 | OK |
| BinaryDefense | 4,507 | OK |
| GreenSnow | 4,472 | OK |
| Blocklist.de (bots) | 1,767 | OK |
| Spamhaus DROP | 1,697 | OK |
| Tor Exit Nodes | 1,263 | OK |
| Blocklist.de (bruteforcelogin) | 845 | OK |
| Emerging Threats | 526 | OK |
| Blocklist.de (strongips) | 339 | OK |
| AlienVault OTX | 186 | OK |
| Spamhaus DROPv6 | 94 | OK |
