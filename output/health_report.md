# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-04T12:19:19.584861+00:00
**Duration:** 35.62s
**Successful:** 17/19

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
| Unique to single source | 53,711 |
| Found in multiple sources | 41,934 |
| Max source overlap | 8 |
| Avg sources per IP | 1.88 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 29,634 | 26,920 | 52.4% |
| SGB (Turkiye) | 9,735 | 265 | 97.4% |
| Stamparm IPsum | 9,283 | 26,002 | 26.3% |
| AbuseIPDB | 1,674 | 8,326 | 16.7% |
| Spamhaus DROP | 1,641 | 0 | 100.0% |
| Tor Exit Nodes | 652 | 602 | 52.0% |
| GreenSnow | 523 | 4,430 | 10.6% |
| BinaryDefense | 253 | 1,860 | 12.0% |
| AlienVault OTX | 117 | 48 | 70.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 85 | 24,348 | 0.3% |
| Emerging Threats | 10 | 515 | 1.9% |
| Blocklist.de (strongips) | 7 | 317 | 2.2% |
| Blocklist.de (bruteforcelogin) | 3 | 916 | 0.3% |
| Blocklist.de (mail) | 1 | 12,616 | 0.0% |
| Blocklist.de (ssh) | 0 | 7,550 | 0.0% |
| Blocklist.de (apache) | 0 | 9,120 | 0.0% |
| Blocklist.de (bots) | 0 | 2,388 | 0.0% |
| CINS Army | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,580 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,616 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,967 |
| Blocklist.de (all) & Stamparm IPsum | 11,157 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,120 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,550 |
| Stamparm IPsum & AbuseIPDB | 7,061 |
| RTBH (Turkiye) & AbuseIPDB | 6,776 |
| Blocklist.de (ssh) & Stamparm IPsum | 6,571 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 2 | 2026-06-04 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,554 | OK |
| Stamparm IPsum | 35,285 | OK |
| Blocklist.de (all) | 24,433 | OK |
| Blocklist.de (mail) | 12,617 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,120 | OK |
| Blocklist.de (ssh) | 7,550 | OK |
| GreenSnow | 4,953 | OK |
| Blocklist.de (bots) | 2,388 | OK |
| BinaryDefense | 2,113 | OK |
| Spamhaus DROP | 1,641 | OK |
| Tor Exit Nodes | 1,254 | OK |
| Blocklist.de (bruteforcelogin) | 919 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 324 | OK |
| AlienVault OTX | 165 | OK |
| Spamhaus DROPv6 | 93 | OK |
| CINS Army | 0 | EMPTY |
