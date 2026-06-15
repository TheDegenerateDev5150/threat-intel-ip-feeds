# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-15T21:22:02.445451+00:00
**Duration:** 49.18s
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
| Unique to single source | 55,824 |
| Found in multiple sources | 49,266 |
| Max source overlap | 9 |
| Avg sources per IP | 1.93 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 26,623 | 28,450 | 48.3% |
| SGB (Turkiye) | 9,788 | 212 | 97.9% |
| Stamparm IPsum | 7,768 | 30,814 | 20.1% |
| CINS Army | 6,409 | 8,591 | 42.7% |
| Spamhaus DROP | 1,705 | 0 | 100.0% |
| BinaryDefense | 1,280 | 3,916 | 24.6% |
| AbuseIPDB | 946 | 9,054 | 9.5% |
| Tor Exit Nodes | 615 | 625 | 49.6% |
| GreenSnow | 349 | 5,081 | 6.4% |
| AlienVault OTX | 186 | 24 | 88.6% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 30 | 25,446 | 0.1% |
| Blocklist.de (strongips) | 21 | 321 | 6.1% |
| Emerging Threats | 9 | 548 | 1.6% |
| Blocklist.de (bots) | 1 | 4,604 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,341 | 0.0% |
| Blocklist.de (mail) | 0 | 13,728 | 0.0% |
| Blocklist.de (apache) | 0 | 9,232 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 945 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,216 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,728 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,369 |
| Blocklist.de (all) & Stamparm IPsum | 9,642 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,232 |
| Stamparm IPsum & AbuseIPDB | 8,080 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,521 |
| RTBH (Turkiye) & AbuseIPDB | 7,006 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,341 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 89 | 2026-06-15 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,073 | OK |
| Stamparm IPsum | 38,582 | OK |
| Blocklist.de (all) | 25,476 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,728 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,232 | OK |
| GreenSnow | 5,430 | OK |
| Blocklist.de (ssh) | 5,341 | OK |
| BinaryDefense | 5,196 | OK |
| Blocklist.de (bots) | 4,605 | OK |
| Spamhaus DROP | 1,705 | OK |
| Tor Exit Nodes | 1,240 | OK |
| Blocklist.de (bruteforcelogin) | 945 | OK |
| Emerging Threats | 557 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 210 | OK |
| Spamhaus DROPv6 | 94 | OK |
