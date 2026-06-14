# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-14T23:37:42.699160+00:00
**Duration:** 34.59s
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
| Unique to single source | 56,159 |
| Found in multiple sources | 46,522 |
| Max source overlap | 9 |
| Avg sources per IP | 1.91 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,586 | 27,602 | 50.0% |
| SGB (Turkiye) | 9,783 | 217 | 97.8% |
| Stamparm IPsum | 7,523 | 30,704 | 19.7% |
| CINS Army | 6,468 | 8,532 | 43.1% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,186 | 3,797 | 23.8% |
| AbuseIPDB | 691 | 9,309 | 6.9% |
| Tor Exit Nodes | 611 | 643 | 48.7% |
| GreenSnow | 292 | 5,865 | 4.7% |
| AlienVault OTX | 145 | 22 | 86.8% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Emerging Threats | 31 | 497 | 5.9% |
| Blocklist.de (all) | 29 | 22,200 | 0.1% |
| Blocklist.de (strongips) | 23 | 319 | 6.7% |
| Blocklist.de (ssh) | 0 | 5,488 | 0.0% |
| Blocklist.de (mail) | 0 | 12,662 | 0.0% |
| Blocklist.de (apache) | 0 | 9,172 | 0.0% |
| Blocklist.de (bots) | 0 | 2,312 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 924 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,199 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,662 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,183 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,172 |
| Blocklist.de (all) & Stamparm IPsum | 9,057 |
| Stamparm IPsum & AbuseIPDB | 8,217 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,462 |
| RTBH (Turkiye) & AbuseIPDB | 7,067 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,488 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 85 | 2026-06-14 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,188 | OK |
| Stamparm IPsum | 38,227 | OK |
| Blocklist.de (all) | 22,229 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,662 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,172 | OK |
| GreenSnow | 6,157 | OK |
| Blocklist.de (ssh) | 5,488 | OK |
| BinaryDefense | 4,983 | OK |
| Blocklist.de (bots) | 2,312 | OK |
| Spamhaus DROP | 1,697 | OK |
| Tor Exit Nodes | 1,254 | OK |
| Blocklist.de (bruteforcelogin) | 924 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 167 | OK |
| Spamhaus DROPv6 | 94 | OK |
