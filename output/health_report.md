# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-14T13:03:58.731150+00:00
**Duration:** 56.51s
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
| Unique to single source | 59,173 |
| Found in multiple sources | 45,092 |
| Max source overlap | 9 |
| Avg sources per IP | 1.88 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,631 | 25,595 | 55.3% |
| SGB (Turkiye) | 9,780 | 220 | 97.8% |
| Stamparm IPsum | 7,092 | 31,135 | 18.6% |
| CINS Army | 5,763 | 9,237 | 38.4% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,175 | 3,808 | 23.6% |
| AbuseIPDB | 756 | 9,244 | 7.6% |
| Tor Exit Nodes | 621 | 639 | 49.3% |
| GreenSnow | 338 | 4,845 | 6.5% |
| AlienVault OTX | 146 | 22 | 86.9% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 30 | 21,284 | 0.1% |
| Emerging Threats | 30 | 498 | 5.7% |
| Blocklist.de (strongips) | 20 | 319 | 5.9% |
| Blocklist.de (ssh) | 0 | 5,643 | 0.0% |
| Blocklist.de (mail) | 0 | 12,661 | 0.0% |
| Blocklist.de (apache) | 0 | 9,082 | 0.0% |
| Blocklist.de (bots) | 0 | 1,377 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 876 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,625 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,661 |
| Blocklist.de (all) & Stamparm IPsum | 9,619 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,082 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,766 |
| Stamparm IPsum & AbuseIPDB | 8,259 |
| CINS Army & Stamparm IPsum | 8,252 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,976 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,643 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 80 | 2026-06-14 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,226 | OK |
| Stamparm IPsum | 38,227 | OK |
| Blocklist.de (all) | 21,314 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,661 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,082 | OK |
| Blocklist.de (ssh) | 5,643 | OK |
| GreenSnow | 5,183 | OK |
| BinaryDefense | 4,983 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,377 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 876 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 339 | OK |
| AlienVault OTX | 168 | OK |
| Spamhaus DROPv6 | 94 | OK |
