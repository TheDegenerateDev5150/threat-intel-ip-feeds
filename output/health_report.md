# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-10T11:04:13.556701+00:00
**Duration:** 44.02s
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
| Unique to single source | 56,714 |
| Found in multiple sources | 47,787 |
| Max source overlap | 8 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 28,618 | 25,439 | 52.9% |
| SGB (Turkiye) | 9,775 | 225 | 97.8% |
| Stamparm IPsum | 7,892 | 30,423 | 20.6% |
| CINS Army | 6,086 | 8,914 | 40.6% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| BinaryDefense | 755 | 3,261 | 18.8% |
| Tor Exit Nodes | 628 | 632 | 49.8% |
| AbuseIPDB | 622 | 9,378 | 6.2% |
| GreenSnow | 369 | 4,048 | 8.4% |
| AlienVault OTX | 151 | 28 | 84.4% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 27 | 25,052 | 0.1% |
| Blocklist.de (strongips) | 22 | 314 | 6.5% |
| Emerging Threats | 16 | 509 | 3.0% |
| Blocklist.de (ssh) | 0 | 7,741 | 0.0% |
| Blocklist.de (mail) | 0 | 13,486 | 0.0% |
| Blocklist.de (apache) | 0 | 9,030 | 0.0% |
| Blocklist.de (bots) | 0 | 2,450 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 868 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,931 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,486 |
| Blocklist.de (all) & Stamparm IPsum | 9,831 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,631 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,030 |
| Stamparm IPsum & AbuseIPDB | 8,541 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,774 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,741 |
| RTBH (Turkiye) & AbuseIPDB | 7,105 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 50 | 2026-06-10 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 54,057 | OK |
| Stamparm IPsum | 38,315 | OK |
| Blocklist.de (all) | 25,079 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,486 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,030 | OK |
| Blocklist.de (ssh) | 7,741 | OK |
| GreenSnow | 4,417 | OK |
| BinaryDefense | 4,016 | OK |
| Blocklist.de (bots) | 2,450 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 868 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 336 | OK |
| AlienVault OTX | 179 | OK |
| Spamhaus DROPv6 | 93 | OK |
