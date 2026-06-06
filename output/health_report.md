# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-06T22:17:18.794420+00:00
**Duration:** 35.32s
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
| Unique to single source | 56,532 |
| Found in multiple sources | 46,954 |
| Max source overlap | 9 |
| Avg sources per IP | 1.87 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 28,317 | 27,504 | 50.7% |
| SGB (Turkiye) | 9,756 | 244 | 97.6% |
| Stamparm IPsum | 7,657 | 30,299 | 20.2% |
| CINS Army | 6,535 | 8,465 | 43.6% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 1,055 | 8,945 | 10.5% |
| Tor Exit Nodes | 619 | 624 | 49.8% |
| BinaryDefense | 419 | 2,325 | 15.3% |
| GreenSnow | 246 | 4,425 | 5.3% |
| AlienVault OTX | 112 | 30 | 78.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 46 | 22,734 | 0.2% |
| Blocklist.de (strongips) | 24 | 305 | 7.3% |
| Emerging Threats | 11 | 514 | 2.1% |
| Blocklist.de (ssh) | 0 | 4,698 | 0.0% |
| Blocklist.de (mail) | 0 | 12,522 | 0.0% |
| Blocklist.de (apache) | 0 | 8,712 | 0.0% |
| Blocklist.de (bots) | 0 | 4,123 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 516 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,015 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,522 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,869 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,712 |
| Blocklist.de (all) & Stamparm IPsum | 8,432 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,956 |
| CINS Army & Stamparm IPsum | 7,522 |
| RTBH (Turkiye) & AbuseIPDB | 6,627 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,698 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 23 | 2026-06-06 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,821 | OK |
| Stamparm IPsum | 37,956 | OK |
| Blocklist.de (all) | 22,780 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,522 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,712 | OK |
| Blocklist.de (ssh) | 4,698 | OK |
| GreenSnow | 4,671 | OK |
| Blocklist.de (bots) | 4,123 | OK |
| BinaryDefense | 2,744 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,243 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (bruteforcelogin) | 516 | OK |
| Blocklist.de (strongips) | 329 | OK |
| AlienVault OTX | 142 | OK |
| Spamhaus DROPv6 | 93 | OK |
