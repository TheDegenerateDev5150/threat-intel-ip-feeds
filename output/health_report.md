# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-11T19:45:33.309379+00:00
**Duration:** 33.44s
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
| Unique to single source | 60,243 |
| Found in multiple sources | 47,441 |
| Max source overlap | 8 |
| Avg sources per IP | 1.88 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,428 | 27,368 | 52.6% |
| SGB (Turkiye) | 9,768 | 232 | 97.7% |
| Stamparm IPsum | 8,354 | 31,773 | 20.8% |
| CINS Army | 6,399 | 8,601 | 42.7% |
| Spamhaus DROP | 1,698 | 0 | 100.0% |
| AbuseIPDB | 1,325 | 8,675 | 13.2% |
| BinaryDefense | 865 | 3,403 | 20.3% |
| Tor Exit Nodes | 618 | 643 | 49.0% |
| GreenSnow | 462 | 4,156 | 10.0% |
| AlienVault OTX | 163 | 25 | 86.7% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 34 | 24,004 | 0.1% |
| Blocklist.de (strongips) | 18 | 323 | 5.3% |
| Emerging Threats | 17 | 510 | 3.2% |
| Blocklist.de (ssh) | 0 | 7,682 | 0.0% |
| Blocklist.de (mail) | 0 | 13,002 | 0.0% |
| Blocklist.de (apache) | 0 | 9,151 | 0.0% |
| Blocklist.de (bots) | 0 | 1,755 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 969 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,407 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,002 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,556 |
| Blocklist.de (all) & Stamparm IPsum | 10,420 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,151 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,900 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,682 |
| CINS Army & Stamparm IPsum | 7,662 |
| RTBH (Turkiye) & AbuseIPDB | 6,506 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 59 | 2026-06-11 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,796 | OK |
| Stamparm IPsum | 40,127 | OK |
| Blocklist.de (all) | 24,038 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,002 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,151 | OK |
| Blocklist.de (ssh) | 7,682 | OK |
| GreenSnow | 4,618 | OK |
| BinaryDefense | 4,268 | OK |
| Blocklist.de (bots) | 1,755 | OK |
| Spamhaus DROP | 1,698 | OK |
| Tor Exit Nodes | 1,261 | OK |
| Blocklist.de (bruteforcelogin) | 969 | OK |
| Emerging Threats | 527 | OK |
| Blocklist.de (strongips) | 341 | OK |
| AlienVault OTX | 188 | OK |
| Spamhaus DROPv6 | 94 | OK |
