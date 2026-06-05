# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-05T21:45:08.793658+00:00
**Duration:** 32.95s
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
| Unique to single source | 55,542 |
| Found in multiple sources | 44,435 |
| Max source overlap | 9 |
| Avg sources per IP | 1.88 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,669 | 27,700 | 50.0% |
| SGB (Turkiye) | 9,758 | 242 | 97.6% |
| CINS Army | 7,332 | 7,668 | 48.9% |
| Stamparm IPsum | 6,641 | 27,770 | 19.3% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 859 | 9,141 | 8.6% |
| Tor Exit Nodes | 681 | 566 | 54.6% |
| BinaryDefense | 335 | 2,061 | 14.0% |
| GreenSnow | 327 | 4,695 | 6.5% |
| AlienVault OTX | 113 | 33 | 77.4% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 71 | 21,882 | 0.3% |
| Blocklist.de (strongips) | 8 | 320 | 2.4% |
| Emerging Threats | 8 | 517 | 1.5% |
| Blocklist.de (ssh) | 3 | 5,133 | 0.1% |
| Blocklist.de (bots) | 1 | 2,662 | 0.0% |
| Blocklist.de (bruteforcelogin) | 1 | 761 | 0.1% |
| Blocklist.de (mail) | 0 | 12,351 | 0.0% |
| Blocklist.de (apache) | 0 | 8,959 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,462 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,351 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,213 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,959 |
| Blocklist.de (all) & Stamparm IPsum | 8,805 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,386 |
| RTBH (Turkiye) & AbuseIPDB | 7,047 |
| CINS Army & Stamparm IPsum | 5,675 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,132 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 13 | 2026-06-05 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,369 | OK |
| Stamparm IPsum | 34,411 | OK |
| Blocklist.de (all) | 21,953 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,351 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,959 | OK |
| Blocklist.de (ssh) | 5,136 | OK |
| GreenSnow | 5,022 | OK |
| Blocklist.de (bots) | 2,663 | OK |
| BinaryDefense | 2,396 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,247 | OK |
| Blocklist.de (bruteforcelogin) | 762 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 146 | OK |
| Spamhaus DROPv6 | 93 | OK |
