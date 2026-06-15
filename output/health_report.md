# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-15T12:43:24.859413+00:00
**Duration:** 37.63s
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
| Unique to single source | 58,637 |
| Found in multiple sources | 47,721 |
| Max source overlap | 9 |
| Avg sources per IP | 1.89 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,193 | 26,169 | 53.6% |
| SGB (Turkiye) | 9,785 | 215 | 97.9% |
| Stamparm IPsum | 7,417 | 31,165 | 19.2% |
| CINS Army | 6,027 | 8,973 | 40.2% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,273 | 3,923 | 24.5% |
| AbuseIPDB | 926 | 9,074 | 9.3% |
| Tor Exit Nodes | 619 | 633 | 49.4% |
| GreenSnow | 364 | 4,845 | 7.0% |
| AlienVault OTX | 145 | 22 | 86.8% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Emerging Threats | 47 | 481 | 8.9% |
| Blocklist.de (all) | 26 | 23,986 | 0.1% |
| Blocklist.de (strongips) | 23 | 320 | 6.7% |
| Blocklist.de (bots) | 1 | 3,377 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,459 | 0.0% |
| Blocklist.de (mail) | 0 | 13,490 | 0.0% |
| Blocklist.de (apache) | 0 | 9,133 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 852 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,668 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,490 |
| Blocklist.de (all) & Stamparm IPsum | 9,987 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,318 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,133 |
| Stamparm IPsum & AbuseIPDB | 8,080 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,811 |
| RTBH (Turkiye) & AbuseIPDB | 6,924 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,459 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 87 | 2026-06-15 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,362 | OK |
| Stamparm IPsum | 38,582 | OK |
| Blocklist.de (all) | 24,012 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,490 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,133 | OK |
| Blocklist.de (ssh) | 5,459 | OK |
| GreenSnow | 5,209 | OK |
| BinaryDefense | 5,196 | OK |
| Blocklist.de (bots) | 3,378 | OK |
| Spamhaus DROP | 1,697 | OK |
| Tor Exit Nodes | 1,252 | OK |
| Blocklist.de (bruteforcelogin) | 852 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 343 | OK |
| AlienVault OTX | 167 | OK |
| Spamhaus DROPv6 | 94 | OK |
