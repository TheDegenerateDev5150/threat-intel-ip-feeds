# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-12T22:00:56.865889+00:00
**Duration:** 100.05s
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
| Unique to single source | 56,073 |
| Found in multiple sources | 46,871 |
| Max source overlap | 9 |
| Avg sources per IP | 1.93 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,632 | 28,469 | 49.3% |
| SGB (Turkiye) | 9,777 | 223 | 97.8% |
| Stamparm IPsum | 7,465 | 30,059 | 19.9% |
| CINS Army | 6,296 | 8,704 | 42.0% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,015 | 3,492 | 22.5% |
| AbuseIPDB | 832 | 9,168 | 8.3% |
| Tor Exit Nodes | 659 | 604 | 52.2% |
| GreenSnow | 390 | 4,742 | 7.6% |
| AlienVault OTX | 155 | 23 | 87.1% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 42 | 24,248 | 0.2% |
| Blocklist.de (strongips) | 13 | 329 | 3.8% |
| Emerging Threats | 6 | 522 | 1.1% |
| Blocklist.de (ssh) | 0 | 8,154 | 0.0% |
| Blocklist.de (mail) | 0 | 12,983 | 0.0% |
| Blocklist.de (apache) | 0 | 8,927 | 0.0% |
| Blocklist.de (bots) | 0 | 1,712 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 756 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,736 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,983 |
| Blocklist.de (all) & RTBH (Turkiye) | 12,438 |
| Blocklist.de (all) & Stamparm IPsum | 9,772 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,927 |
| Stamparm IPsum & AbuseIPDB | 8,281 |
| Blocklist.de (all) & Blocklist.de (ssh) | 8,154 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,693 |
| RTBH (Turkiye) & AbuseIPDB | 7,073 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 67 | 2026-06-12 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,101 | OK |
| Stamparm IPsum | 37,524 | OK |
| Blocklist.de (all) | 24,290 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,983 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,927 | OK |
| Blocklist.de (ssh) | 8,154 | OK |
| GreenSnow | 5,132 | OK |
| BinaryDefense | 4,507 | OK |
| Blocklist.de (bots) | 1,712 | OK |
| Spamhaus DROP | 1,697 | OK |
| Tor Exit Nodes | 1,263 | OK |
| Blocklist.de (bruteforcelogin) | 756 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 178 | OK |
| Spamhaus DROPv6 | 94 | OK |
