# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-06T12:18:38.937724+00:00
**Duration:** 37.82s
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
| Unique to single source | 57,881 |
| Found in multiple sources | 46,688 |
| Max source overlap | 9 |
| Avg sources per IP | 1.86 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,499 | 26,124 | 53.9% |
| SGB (Turkiye) | 9,760 | 240 | 97.6% |
| Stamparm IPsum | 7,375 | 30,581 | 19.4% |
| CINS Army | 6,175 | 8,825 | 41.2% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 742 | 9,258 | 7.4% |
| Tor Exit Nodes | 621 | 621 | 50.0% |
| BinaryDefense | 414 | 2,330 | 15.1% |
| GreenSnow | 329 | 4,254 | 7.2% |
| AlienVault OTX | 112 | 30 | 78.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 90 | 22,848 | 0.4% |
| Blocklist.de (strongips) | 18 | 310 | 5.5% |
| Emerging Threats | 11 | 514 | 2.1% |
| Blocklist.de (ssh) | 0 | 4,974 | 0.0% |
| Blocklist.de (mail) | 0 | 12,486 | 0.0% |
| Blocklist.de (apache) | 0 | 8,877 | 0.0% |
| Blocklist.de (bots) | 0 | 3,755 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 652 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,454 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,474 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,028 |
| Blocklist.de (all) & Stamparm IPsum | 8,991 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,877 |
| Stamparm IPsum & AbuseIPDB | 8,369 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,957 |
| RTBH (Turkiye) & AbuseIPDB | 6,904 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,974 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 18 | 2026-06-06 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,623 | OK |
| Stamparm IPsum | 37,956 | OK |
| Blocklist.de (all) | 22,938 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,486 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,877 | OK |
| Blocklist.de (ssh) | 4,974 | OK |
| GreenSnow | 4,583 | OK |
| Blocklist.de (bots) | 3,755 | OK |
| BinaryDefense | 2,744 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,242 | OK |
| Blocklist.de (bruteforcelogin) | 652 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 142 | OK |
| Spamhaus DROPv6 | 93 | OK |
