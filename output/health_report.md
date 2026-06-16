# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-16T11:34:28.154808+00:00
**Duration:** 116.08s
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
| Unique to single source | 58,050 |
| Found in multiple sources | 50,942 |
| Max source overlap | 9 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 28,888 | 27,434 | 51.3% |
| SGB (Turkiye) | 9,790 | 210 | 97.9% |
| Stamparm IPsum | 7,514 | 30,403 | 19.8% |
| CINS Army | 6,454 | 8,546 | 43.0% |
| Spamhaus DROP | 1,707 | 0 | 100.0% |
| BinaryDefense | 1,376 | 4,056 | 25.3% |
| AbuseIPDB | 935 | 9,065 | 9.3% |
| Tor Exit Nodes | 613 | 631 | 49.3% |
| GreenSnow | 389 | 4,668 | 7.7% |
| AlienVault OTX | 195 | 25 | 88.6% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 45 | 27,235 | 0.2% |
| Blocklist.de (strongips) | 20 | 321 | 5.9% |
| Emerging Threats | 18 | 539 | 3.2% |
| Blocklist.de (mail) | 12 | 13,790 | 0.1% |
| Blocklist.de (ssh) | 0 | 5,269 | 0.0% |
| Blocklist.de (apache) | 0 | 9,141 | 0.0% |
| Blocklist.de (bots) | 0 | 6,521 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 897 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,302 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,778 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,641 |
| Blocklist.de (all) & Stamparm IPsum | 9,335 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,138 |
| Stamparm IPsum & AbuseIPDB | 8,010 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,467 |
| RTBH (Turkiye) & AbuseIPDB | 6,937 |
| Blocklist.de (all) & Blocklist.de (bots) | 6,521 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 92 | 2026-06-16 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,322 | OK |
| Stamparm IPsum | 37,917 | OK |
| Blocklist.de (all) | 27,280 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,802 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,141 | OK |
| Blocklist.de (bots) | 6,521 | OK |
| BinaryDefense | 5,432 | OK |
| Blocklist.de (ssh) | 5,269 | OK |
| GreenSnow | 5,057 | OK |
| Spamhaus DROP | 1,707 | OK |
| Tor Exit Nodes | 1,244 | OK |
| Blocklist.de (bruteforcelogin) | 897 | OK |
| Emerging Threats | 557 | OK |
| Blocklist.de (strongips) | 341 | OK |
| AlienVault OTX | 220 | OK |
| Spamhaus DROPv6 | 94 | OK |
