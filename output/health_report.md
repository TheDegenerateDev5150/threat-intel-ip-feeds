# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-14T19:58:09.065925+00:00
**Duration:** 84.03s
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
| Unique to single source | 59,875 |
| Found in multiple sources | 45,837 |
| Max source overlap | 8 |
| Avg sources per IP | 1.86 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,828 | 25,889 | 55.1% |
| SGB (Turkiye) | 9,780 | 220 | 97.8% |
| Stamparm IPsum | 7,257 | 30,970 | 19.0% |
| CINS Army | 6,149 | 8,851 | 41.0% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,173 | 3,810 | 23.5% |
| AbuseIPDB | 681 | 9,319 | 6.8% |
| Tor Exit Nodes | 613 | 644 | 48.8% |
| GreenSnow | 375 | 4,986 | 7.0% |
| AlienVault OTX | 145 | 22 | 86.8% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 32 | 21,606 | 0.1% |
| Emerging Threats | 31 | 497 | 5.9% |
| Blocklist.de (strongips) | 20 | 322 | 5.8% |
| Blocklist.de (ssh) | 0 | 5,484 | 0.0% |
| Blocklist.de (mail) | 0 | 12,628 | 0.0% |
| Blocklist.de (apache) | 0 | 9,152 | 0.0% |
| Blocklist.de (bots) | 0 | 1,806 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 929 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,694 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,628 |
| Blocklist.de (all) & Stamparm IPsum | 9,160 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,152 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,597 |
| Stamparm IPsum & AbuseIPDB | 8,217 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,787 |
| RTBH (Turkiye) & AbuseIPDB | 6,973 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,484 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 83 | 2026-06-14 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,717 | OK |
| Stamparm IPsum | 38,227 | OK |
| Blocklist.de (all) | 21,638 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,628 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,152 | OK |
| Blocklist.de (ssh) | 5,484 | OK |
| GreenSnow | 5,361 | OK |
| BinaryDefense | 4,983 | OK |
| Blocklist.de (bots) | 1,806 | OK |
| Spamhaus DROP | 1,697 | OK |
| Tor Exit Nodes | 1,257 | OK |
| Blocklist.de (bruteforcelogin) | 929 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 167 | OK |
| Spamhaus DROPv6 | 94 | OK |
