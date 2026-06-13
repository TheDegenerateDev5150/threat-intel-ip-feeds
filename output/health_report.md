# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-13T16:46:22.841577+00:00
**Duration:** 36.36s
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
| Unique to single source | 60,380 |
| Found in multiple sources | 45,415 |
| Max source overlap | 9 |
| Avg sources per IP | 1.86 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 32,471 | 25,440 | 56.1% |
| SGB (Turkiye) | 9,778 | 222 | 97.8% |
| Stamparm IPsum | 7,310 | 31,413 | 18.9% |
| CINS Army | 5,938 | 9,062 | 39.6% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,118 | 3,646 | 23.5% |
| AbuseIPDB | 768 | 9,232 | 7.7% |
| Tor Exit Nodes | 616 | 646 | 48.8% |
| GreenSnow | 364 | 4,951 | 6.8% |
| AlienVault OTX | 155 | 23 | 87.1% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 43 | 21,478 | 0.2% |
| Emerging Threats | 17 | 511 | 3.2% |
| Blocklist.de (strongips) | 7 | 330 | 2.1% |
| Blocklist.de (mail) | 4 | 12,736 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,690 | 0.0% |
| Blocklist.de (apache) | 0 | 8,981 | 0.0% |
| Blocklist.de (bots) | 0 | 1,618 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 815 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,427 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,732 |
| Blocklist.de (all) & Stamparm IPsum | 9,711 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,980 |
| Stamparm IPsum & AbuseIPDB | 8,419 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,369 |
| CINS Army & Stamparm IPsum | 8,063 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 7,172 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,690 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 73 | 2026-06-13 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,911 | OK |
| Stamparm IPsum | 38,723 | OK |
| Blocklist.de (all) | 21,521 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,740 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,981 | OK |
| Blocklist.de (ssh) | 5,690 | OK |
| GreenSnow | 5,315 | OK |
| BinaryDefense | 4,764 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,618 | OK |
| Tor Exit Nodes | 1,262 | OK |
| Blocklist.de (bruteforcelogin) | 815 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 337 | OK |
| AlienVault OTX | 178 | OK |
| Spamhaus DROPv6 | 94 | OK |
