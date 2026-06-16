# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-16T05:33:55.236212+00:00
**Duration:** 147.23s
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
| Unique to single source | 55,831 |
| Found in multiple sources | 50,416 |
| Max source overlap | 9 |
| Avg sources per IP | 1.94 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 28,129 | 27,527 | 50.5% |
| SGB (Turkiye) | 9,791 | 209 | 97.9% |
| Stamparm IPsum | 7,477 | 30,440 | 19.7% |
| CINS Army | 5,147 | 9,853 | 34.3% |
| Spamhaus DROP | 1,705 | 0 | 100.0% |
| BinaryDefense | 1,384 | 4,048 | 25.5% |
| AbuseIPDB | 907 | 9,093 | 9.1% |
| Tor Exit Nodes | 615 | 630 | 49.4% |
| GreenSnow | 328 | 5,917 | 5.3% |
| AlienVault OTX | 186 | 24 | 88.6% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 29 | 26,800 | 0.1% |
| Blocklist.de (strongips) | 21 | 320 | 6.2% |
| Emerging Threats | 18 | 539 | 3.2% |
| Blocklist.de (ssh) | 0 | 5,348 | 0.0% |
| Blocklist.de (mail) | 0 | 13,874 | 0.0% |
| Blocklist.de (apache) | 0 | 9,155 | 0.0% |
| Blocklist.de (bots) | 0 | 5,874 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 895 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,241 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,874 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,928 |
| Blocklist.de (all) & Stamparm IPsum | 9,612 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,155 |
| CINS Army & Stamparm IPsum | 8,695 |
| Stamparm IPsum & AbuseIPDB | 8,010 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,916 |
| Blocklist.de (all) & Blocklist.de (bots) | 5,874 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 91 | 2026-06-16 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,656 | OK |
| Stamparm IPsum | 37,917 | OK |
| Blocklist.de (all) | 26,829 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,874 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,155 | OK |
| GreenSnow | 6,245 | OK |
| Blocklist.de (bots) | 5,874 | OK |
| BinaryDefense | 5,432 | OK |
| Blocklist.de (ssh) | 5,348 | OK |
| Spamhaus DROP | 1,705 | OK |
| Tor Exit Nodes | 1,245 | OK |
| Blocklist.de (bruteforcelogin) | 895 | OK |
| Emerging Threats | 557 | OK |
| Blocklist.de (strongips) | 341 | OK |
| AlienVault OTX | 210 | OK |
| Spamhaus DROPv6 | 94 | OK |
