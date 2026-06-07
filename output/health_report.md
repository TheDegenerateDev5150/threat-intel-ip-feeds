# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-07T16:44:41.682509+00:00
**Duration:** 33.51s
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
| Unique to single source | 58,613 |
| Found in multiple sources | 47,611 |
| Max source overlap | 9 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,121 | 26,032 | 54.5% |
| SGB (Turkiye) | 9,765 | 235 | 97.7% |
| Stamparm IPsum | 7,517 | 30,151 | 20.0% |
| CINS Army | 6,235 | 8,765 | 41.6% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 678 | 9,322 | 6.8% |
| Tor Exit Nodes | 629 | 628 | 50.0% |
| BinaryDefense | 468 | 2,572 | 15.4% |
| GreenSnow | 267 | 4,043 | 6.2% |
| AlienVault OTX | 104 | 28 | 78.8% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 40 | 23,573 | 0.2% |
| Emerging Threats | 30 | 495 | 5.7% |
| Blocklist.de (strongips) | 24 | 305 | 7.3% |
| Blocklist.de (ssh) | 0 | 4,843 | 0.0% |
| Blocklist.de (mail) | 0 | 12,680 | 0.0% |
| Blocklist.de (apache) | 0 | 8,780 | 0.0% |
| Blocklist.de (bots) | 0 | 4,655 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 545 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,284 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,680 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,780 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,677 |
| Blocklist.de (all) & Stamparm IPsum | 8,381 |
| Stamparm IPsum & AbuseIPDB | 8,284 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,812 |
| RTBH (Turkiye) & AbuseIPDB | 7,080 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,843 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 30 | 2026-06-07 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,153 | OK |
| Stamparm IPsum | 37,668 | OK |
| Blocklist.de (all) | 23,613 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,680 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,780 | OK |
| Blocklist.de (ssh) | 4,843 | OK |
| Blocklist.de (bots) | 4,655 | OK |
| GreenSnow | 4,310 | OK |
| BinaryDefense | 3,040 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,257 | OK |
| Blocklist.de (bruteforcelogin) | 545 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 329 | OK |
| AlienVault OTX | 132 | OK |
| Spamhaus DROPv6 | 93 | OK |
