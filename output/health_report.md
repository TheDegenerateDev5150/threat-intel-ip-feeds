# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-15T05:28:01.832483+00:00
**Duration:** 106.7s
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
| Unique to single source | 56,069 |
| Found in multiple sources | 46,649 |
| Max source overlap | 9 |
| Avg sources per IP | 1.94 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 29,416 | 26,211 | 52.9% |
| SGB (Turkiye) | 9,784 | 216 | 97.8% |
| Stamparm IPsum | 7,150 | 31,432 | 18.5% |
| CINS Army | 4,612 | 10,388 | 30.7% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,283 | 3,913 | 24.7% |
| AbuseIPDB | 905 | 9,095 | 9.0% |
| Tor Exit Nodes | 620 | 633 | 49.5% |
| GreenSnow | 258 | 5,966 | 4.1% |
| AlienVault OTX | 145 | 22 | 86.8% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Emerging Threats | 47 | 481 | 8.9% |
| Blocklist.de (strongips) | 23 | 319 | 6.7% |
| Blocklist.de (all) | 18 | 22,891 | 0.1% |
| Blocklist.de (mail) | 10 | 12,878 | 0.1% |
| Blocklist.de (apache) | 7 | 9,166 | 0.1% |
| Blocklist.de (ssh) | 0 | 5,524 | 0.0% |
| Blocklist.de (bots) | 0 | 2,753 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 885 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,598 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,873 |
| Blocklist.de (all) & Stamparm IPsum | 10,264 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,683 |
| CINS Army & Stamparm IPsum | 9,235 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,164 |
| Stamparm IPsum & AbuseIPDB | 8,080 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,891 |
| CINS Army & RTBH (Turkiye) | 5,887 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 86 | 2026-06-15 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,627 | OK |
| Stamparm IPsum | 38,582 | OK |
| Blocklist.de (all) | 22,909 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,888 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,173 | OK |
| GreenSnow | 6,224 | OK |
| Blocklist.de (ssh) | 5,524 | OK |
| BinaryDefense | 5,196 | OK |
| Blocklist.de (bots) | 2,753 | OK |
| Spamhaus DROP | 1,697 | OK |
| Tor Exit Nodes | 1,253 | OK |
| Blocklist.de (bruteforcelogin) | 885 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 167 | OK |
| Spamhaus DROPv6 | 94 | OK |
