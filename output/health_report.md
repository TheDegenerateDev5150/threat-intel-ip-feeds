# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-14T10:32:25.021992+00:00
**Duration:** 34.77s
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
| Unique to single source | 59,177 |
| Found in multiple sources | 44,825 |
| Max source overlap | 9 |
| Avg sources per IP | 1.87 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,672 | 25,399 | 55.5% |
| SGB (Turkiye) | 9,780 | 220 | 97.8% |
| Stamparm IPsum | 7,056 | 31,171 | 18.5% |
| CINS Army | 5,826 | 9,174 | 38.8% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,177 | 3,806 | 23.6% |
| AbuseIPDB | 756 | 9,244 | 7.6% |
| Tor Exit Nodes | 622 | 638 | 49.4% |
| GreenSnow | 272 | 3,744 | 6.8% |
| AlienVault OTX | 146 | 22 | 86.9% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Emerging Threats | 30 | 498 | 5.7% |
| Blocklist.de (all) | 26 | 21,250 | 0.1% |
| Blocklist.de (strongips) | 20 | 319 | 5.9% |
| Blocklist.de (apache) | 3 | 9,056 | 0.0% |
| Blocklist.de (ssh) | 0 | 5,665 | 0.0% |
| Blocklist.de (mail) | 0 | 12,662 | 0.0% |
| Blocklist.de (bots) | 0 | 1,358 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 860 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,598 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,662 |
| Blocklist.de (all) & Stamparm IPsum | 9,689 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,056 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,864 |
| Stamparm IPsum & AbuseIPDB | 8,259 |
| CINS Army & Stamparm IPsum | 8,196 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,961 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,665 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 79 | 2026-06-14 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,071 | OK |
| Stamparm IPsum | 38,227 | OK |
| Blocklist.de (all) | 21,276 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,662 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,059 | OK |
| Blocklist.de (ssh) | 5,665 | OK |
| BinaryDefense | 4,983 | OK |
| GreenSnow | 4,016 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,358 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 860 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 339 | OK |
| AlienVault OTX | 168 | OK |
| Spamhaus DROPv6 | 94 | OK |
