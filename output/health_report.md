# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-16T00:02:22.252683+00:00
**Duration:** 38.62s
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
| Unique to single source | 56,086 |
| Found in multiple sources | 49,899 |
| Max source overlap | 9 |
| Avg sources per IP | 1.93 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 26,699 | 28,535 | 48.3% |
| SGB (Turkiye) | 9,789 | 211 | 97.9% |
| Stamparm IPsum | 7,751 | 30,831 | 20.1% |
| CINS Army | 6,482 | 8,518 | 43.2% |
| Spamhaus DROP | 1,705 | 0 | 100.0% |
| BinaryDefense | 1,369 | 4,063 | 25.2% |
| AbuseIPDB | 950 | 9,050 | 9.5% |
| Tor Exit Nodes | 613 | 627 | 49.4% |
| GreenSnow | 386 | 5,865 | 6.2% |
| AlienVault OTX | 186 | 24 | 88.6% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 30 | 25,722 | 0.1% |
| Blocklist.de (strongips) | 21 | 321 | 6.1% |
| Emerging Threats | 10 | 547 | 1.8% |
| Blocklist.de (bots) | 1 | 4,860 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,312 | 0.0% |
| Blocklist.de (mail) | 0 | 13,772 | 0.0% |
| Blocklist.de (apache) | 0 | 9,236 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 945 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,243 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,772 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,161 |
| Blocklist.de (all) & Stamparm IPsum | 9,519 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,236 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,966 |
| CINS Army & Stamparm IPsum | 7,324 |
| RTBH (Turkiye) & AbuseIPDB | 6,851 |
| GreenSnow & RTBH (Turkiye) | 5,479 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 90 | 2026-06-16 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,234 | OK |
| Stamparm IPsum | 38,582 | OK |
| Blocklist.de (all) | 25,752 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,772 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,236 | OK |
| GreenSnow | 6,251 | OK |
| BinaryDefense | 5,432 | OK |
| Blocklist.de (ssh) | 5,312 | OK |
| Blocklist.de (bots) | 4,861 | OK |
| Spamhaus DROP | 1,705 | OK |
| Tor Exit Nodes | 1,240 | OK |
| Blocklist.de (bruteforcelogin) | 945 | OK |
| Emerging Threats | 557 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 210 | OK |
| Spamhaus DROPv6 | 94 | OK |
