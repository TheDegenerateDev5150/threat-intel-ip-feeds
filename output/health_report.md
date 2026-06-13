# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-13T18:44:22.828417+00:00
**Duration:** 38.86s
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
| Unique to single source | 60,698 |
| Found in multiple sources | 45,355 |
| Max source overlap | 9 |
| Avg sources per IP | 1.86 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 32,647 | 25,427 | 56.2% |
| SGB (Turkiye) | 9,778 | 222 | 97.8% |
| Stamparm IPsum | 7,354 | 31,369 | 19.0% |
| CINS Army | 5,993 | 9,007 | 40.0% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,118 | 3,646 | 23.5% |
| AbuseIPDB | 770 | 9,230 | 7.7% |
| Tor Exit Nodes | 615 | 646 | 48.8% |
| GreenSnow | 408 | 5,005 | 7.5% |
| AlienVault OTX | 155 | 23 | 87.1% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 45 | 21,358 | 0.2% |
| Emerging Threats | 17 | 511 | 3.2% |
| Blocklist.de (strongips) | 7 | 331 | 2.1% |
| Blocklist.de (ssh) | 0 | 5,670 | 0.0% |
| Blocklist.de (mail) | 0 | 12,720 | 0.0% |
| Blocklist.de (apache) | 0 | 8,955 | 0.0% |
| Blocklist.de (bots) | 0 | 1,554 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 789 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,454 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,720 |
| Blocklist.de (all) & Stamparm IPsum | 9,652 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,955 |
| Stamparm IPsum & AbuseIPDB | 8,419 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,232 |
| CINS Army & Stamparm IPsum | 7,980 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 7,181 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,670 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 74 | 2026-06-13 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 58,074 | OK |
| Stamparm IPsum | 38,723 | OK |
| Blocklist.de (all) | 21,403 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,720 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,955 | OK |
| Blocklist.de (ssh) | 5,670 | OK |
| GreenSnow | 5,413 | OK |
| BinaryDefense | 4,764 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,554 | OK |
| Tor Exit Nodes | 1,261 | OK |
| Blocklist.de (bruteforcelogin) | 789 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 338 | OK |
| AlienVault OTX | 178 | OK |
| Spamhaus DROPv6 | 94 | OK |
