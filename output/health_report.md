# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-07T18:19:56.898906+00:00
**Duration:** 33.01s
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
| Unique to single source | 58,735 |
| Found in multiple sources | 47,635 |
| Max source overlap | 9 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,212 | 26,017 | 54.5% |
| SGB (Turkiye) | 9,765 | 235 | 97.7% |
| Stamparm IPsum | 7,532 | 30,136 | 20.0% |
| CINS Army | 6,261 | 8,739 | 41.7% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 657 | 9,343 | 6.6% |
| Tor Exit Nodes | 629 | 630 | 50.0% |
| BinaryDefense | 468 | 2,572 | 15.4% |
| GreenSnow | 274 | 4,074 | 6.3% |
| AlienVault OTX | 104 | 28 | 78.8% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 44 | 23,518 | 0.2% |
| Emerging Threats | 30 | 495 | 5.7% |
| Blocklist.de (strongips) | 24 | 306 | 7.3% |
| Blocklist.de (ssh) | 0 | 4,851 | 0.0% |
| Blocklist.de (mail) | 0 | 12,740 | 0.0% |
| Blocklist.de (apache) | 0 | 8,783 | 0.0% |
| Blocklist.de (bots) | 0 | 4,528 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 549 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,294 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,738 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,783 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,565 |
| Blocklist.de (all) & Stamparm IPsum | 8,345 |
| Stamparm IPsum & AbuseIPDB | 8,284 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,743 |
| RTBH (Turkiye) & AbuseIPDB | 7,086 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,851 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 31 | 2026-06-07 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,229 | OK |
| Stamparm IPsum | 37,668 | OK |
| Blocklist.de (all) | 23,562 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,740 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,783 | OK |
| Blocklist.de (ssh) | 4,851 | OK |
| Blocklist.de (bots) | 4,528 | OK |
| GreenSnow | 4,348 | OK |
| BinaryDefense | 3,040 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,259 | OK |
| Blocklist.de (bruteforcelogin) | 549 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 330 | OK |
| AlienVault OTX | 132 | OK |
| Spamhaus DROPv6 | 93 | OK |
