# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-13T08:31:46.215953+00:00
**Duration:** 73.69s
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
| Unique to single source | 58,871 |
| Found in multiple sources | 45,662 |
| Max source overlap | 9 |
| Avg sources per IP | 1.89 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,534 | 25,649 | 55.1% |
| SGB (Turkiye) | 9,777 | 223 | 97.8% |
| Stamparm IPsum | 7,124 | 31,599 | 18.4% |
| CINS Army | 5,653 | 9,347 | 37.7% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,125 | 3,639 | 23.6% |
| AbuseIPDB | 744 | 9,256 | 7.4% |
| Tor Exit Nodes | 618 | 645 | 48.9% |
| GreenSnow | 300 | 5,764 | 4.9% |
| AlienVault OTX | 155 | 23 | 87.1% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 25 | 21,656 | 0.1% |
| Emerging Threats | 17 | 511 | 3.2% |
| Blocklist.de (strongips) | 7 | 330 | 2.1% |
| Blocklist.de (apache) | 1 | 8,980 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,669 | 0.0% |
| Blocklist.de (mail) | 0 | 12,841 | 0.0% |
| Blocklist.de (bots) | 0 | 1,682 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 824 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,298 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,841 |
| Blocklist.de (all) & Stamparm IPsum | 9,949 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,977 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,817 |
| Stamparm IPsum & AbuseIPDB | 8,419 |
| CINS Army & Stamparm IPsum | 8,374 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 7,139 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,669 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 70 | 2026-06-13 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,183 | OK |
| Stamparm IPsum | 38,723 | OK |
| Blocklist.de (all) | 21,681 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,841 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,981 | OK |
| GreenSnow | 6,064 | OK |
| Blocklist.de (ssh) | 5,669 | OK |
| BinaryDefense | 4,764 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,682 | OK |
| Tor Exit Nodes | 1,263 | OK |
| Blocklist.de (bruteforcelogin) | 824 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 337 | OK |
| AlienVault OTX | 178 | OK |
| Spamhaus DROPv6 | 94 | OK |
