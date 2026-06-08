# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-08T22:01:23.396836+00:00
**Duration:** 37.92s
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
| Unique to single source | 56,670 |
| Found in multiple sources | 46,134 |
| Max source overlap | 9 |
| Avg sources per IP | 1.88 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,678 | 26,937 | 50.7% |
| SGB (Turkiye) | 9,764 | 236 | 97.6% |
| Stamparm IPsum | 8,375 | 29,500 | 22.1% |
| CINS Army | 6,385 | 8,615 | 42.6% |
| Spamhaus DROP | 1,621 | 0 | 100.0% |
| AbuseIPDB | 1,023 | 8,977 | 10.2% |
| Tor Exit Nodes | 660 | 599 | 52.4% |
| BinaryDefense | 544 | 2,813 | 16.2% |
| GreenSnow | 336 | 4,291 | 7.3% |
| AlienVault OTX | 130 | 30 | 81.2% |
| Spamhaus DROPv6 | 86 | 0 | 100.0% |
| Blocklist.de (all) | 33 | 22,737 | 0.1% |
| Blocklist.de (strongips) | 26 | 309 | 7.8% |
| Emerging Threats | 8 | 511 | 1.5% |
| Blocklist.de (bots) | 1 | 3,490 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,024 | 0.0% |
| Blocklist.de (mail) | 0 | 12,788 | 0.0% |
| Blocklist.de (apache) | 0 | 8,878 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 671 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,862 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,788 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,345 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,878 |
| Blocklist.de (all) & Stamparm IPsum | 8,573 |
| Stamparm IPsum & AbuseIPDB | 8,212 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,697 |
| RTBH (Turkiye) & AbuseIPDB | 6,797 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,024 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 39 | 2026-06-08 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 54,615 | OK |
| Stamparm IPsum | 37,875 | OK |
| Blocklist.de (all) | 22,770 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,788 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,878 | OK |
| Blocklist.de (ssh) | 5,024 | OK |
| GreenSnow | 4,627 | OK |
| Blocklist.de (bots) | 3,491 | OK |
| BinaryDefense | 3,357 | OK |
| Spamhaus DROP | 1,621 | OK |
| Tor Exit Nodes | 1,259 | OK |
| Blocklist.de (bruteforcelogin) | 671 | OK |
| Emerging Threats | 519 | OK |
| Blocklist.de (strongips) | 335 | OK |
| AlienVault OTX | 160 | OK |
| Spamhaus DROPv6 | 86 | OK |
