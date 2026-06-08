# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-08T12:09:13.055112+00:00
**Duration:** 86.89s
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
| Unique to single source | 58,316 |
| Found in multiple sources | 46,220 |
| Max source overlap | 8 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,061 | 25,456 | 54.1% |
| SGB (Turkiye) | 9,762 | 238 | 97.6% |
| Stamparm IPsum | 7,908 | 29,967 | 20.9% |
| CINS Army | 6,172 | 8,828 | 41.1% |
| Spamhaus DROP | 1,621 | 0 | 100.0% |
| AbuseIPDB | 996 | 9,004 | 10.0% |
| Tor Exit Nodes | 655 | 606 | 51.9% |
| BinaryDefense | 540 | 2,817 | 16.1% |
| GreenSnow | 284 | 3,946 | 6.7% |
| AlienVault OTX | 130 | 30 | 81.2% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 41 | 484 | 7.8% |
| Blocklist.de (all) | 33 | 22,553 | 0.1% |
| Blocklist.de (strongips) | 20 | 315 | 6.0% |
| Blocklist.de (ssh) | 0 | 4,922 | 0.0% |
| Blocklist.de (mail) | 0 | 12,473 | 0.0% |
| Blocklist.de (apache) | 0 | 8,796 | 0.0% |
| Blocklist.de (bots) | 0 | 3,741 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 613 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,852 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,473 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,796 |
| Blocklist.de (all) & Stamparm IPsum | 8,657 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,457 |
| Stamparm IPsum & AbuseIPDB | 8,212 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,861 |
| RTBH (Turkiye) & AbuseIPDB | 6,695 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,922 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 36 | 2026-06-08 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,517 | OK |
| Stamparm IPsum | 37,875 | OK |
| Blocklist.de (all) | 22,586 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,473 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,796 | OK |
| Blocklist.de (ssh) | 4,922 | OK |
| GreenSnow | 4,230 | OK |
| Blocklist.de (bots) | 3,741 | OK |
| BinaryDefense | 3,357 | OK |
| Spamhaus DROP | 1,621 | OK |
| Tor Exit Nodes | 1,261 | OK |
| Blocklist.de (bruteforcelogin) | 613 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 335 | OK |
| AlienVault OTX | 160 | OK |
| Spamhaus DROPv6 | 93 | OK |
