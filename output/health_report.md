# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-11T22:16:30.040761+00:00
**Duration:** 75.88s
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
| Unique to single source | 57,594 |
| Found in multiple sources | 47,485 |
| Max source overlap | 9 |
| Avg sources per IP | 1.92 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,547 | 29,155 | 48.6% |
| SGB (Turkiye) | 9,768 | 232 | 97.7% |
| Stamparm IPsum | 8,539 | 31,588 | 21.3% |
| CINS Army | 6,595 | 8,405 | 44.0% |
| Spamhaus DROP | 1,698 | 0 | 100.0% |
| AbuseIPDB | 1,322 | 8,678 | 13.2% |
| BinaryDefense | 878 | 3,390 | 20.6% |
| Tor Exit Nodes | 622 | 639 | 49.3% |
| GreenSnow | 314 | 4,303 | 6.8% |
| AlienVault OTX | 163 | 25 | 86.7% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 25 | 24,022 | 0.1% |
| Blocklist.de (strongips) | 20 | 321 | 5.9% |
| Emerging Threats | 9 | 517 | 1.7% |
| Blocklist.de (ssh) | 0 | 7,677 | 0.0% |
| Blocklist.de (mail) | 0 | 12,971 | 0.0% |
| Blocklist.de (apache) | 0 | 9,165 | 0.0% |
| Blocklist.de (bots) | 0 | 1,787 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 976 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 24,023 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,971 |
| Blocklist.de (all) & RTBH (Turkiye) | 12,343 |
| Blocklist.de (all) & Stamparm IPsum | 10,321 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,165 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,900 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,677 |
| CINS Army & Stamparm IPsum | 7,481 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 6,767 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 60 | 2026-06-11 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,702 | OK |
| Stamparm IPsum | 40,127 | OK |
| Blocklist.de (all) | 24,047 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,971 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,165 | OK |
| Blocklist.de (ssh) | 7,677 | OK |
| GreenSnow | 4,617 | OK |
| BinaryDefense | 4,268 | OK |
| Blocklist.de (bots) | 1,787 | OK |
| Spamhaus DROP | 1,698 | OK |
| Tor Exit Nodes | 1,261 | OK |
| Blocklist.de (bruteforcelogin) | 976 | OK |
| Emerging Threats | 526 | OK |
| Blocklist.de (strongips) | 341 | OK |
| AlienVault OTX | 188 | OK |
| Spamhaus DROPv6 | 94 | OK |
