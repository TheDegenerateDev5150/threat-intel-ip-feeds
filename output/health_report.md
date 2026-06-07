# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-07T11:16:42.851890+00:00
**Duration:** 34.9s
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
| Unique to single source | 57,896 |
| Found in multiple sources | 47,599 |
| Max source overlap | 9 |
| Avg sources per IP | 1.86 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,700 | 26,070 | 54.1% |
| SGB (Turkiye) | 9,764 | 236 | 97.6% |
| Stamparm IPsum | 7,282 | 30,386 | 19.3% |
| CINS Army | 6,192 | 8,808 | 41.3% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 680 | 9,320 | 6.8% |
| Tor Exit Nodes | 628 | 627 | 50.0% |
| BinaryDefense | 475 | 2,565 | 15.6% |
| GreenSnow | 234 | 3,908 | 5.6% |
| AlienVault OTX | 104 | 29 | 78.2% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 40 | 23,571 | 0.2% |
| Emerging Threats | 30 | 495 | 5.7% |
| Blocklist.de (strongips) | 25 | 303 | 7.6% |
| Blocklist.de (ssh) | 6 | 4,812 | 0.1% |
| Blocklist.de (bruteforcelogin) | 1 | 548 | 0.2% |
| Blocklist.de (mail) | 0 | 12,690 | 0.0% |
| Blocklist.de (apache) | 0 | 8,777 | 0.0% |
| Blocklist.de (bots) | 0 | 4,690 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,188 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,690 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,026 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,776 |
| Blocklist.de (all) & Stamparm IPsum | 8,615 |
| Stamparm IPsum & AbuseIPDB | 8,385 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,896 |
| RTBH (Turkiye) & AbuseIPDB | 6,843 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,803 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 27 | 2026-06-07 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,770 | OK |
| Stamparm IPsum | 37,668 | OK |
| Blocklist.de (all) | 23,611 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,690 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,777 | OK |
| Blocklist.de (ssh) | 4,818 | OK |
| Blocklist.de (bots) | 4,690 | OK |
| GreenSnow | 4,142 | OK |
| BinaryDefense | 3,040 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,255 | OK |
| Blocklist.de (bruteforcelogin) | 549 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 133 | OK |
| Spamhaus DROPv6 | 93 | OK |
