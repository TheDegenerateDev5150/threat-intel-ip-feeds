# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-10T01:30:58.299902+00:00
**Duration:** 38.23s
**Successful:** 17/19

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
| Unique to single source | 56,079 |
| Found in multiple sources | 43,359 |
| Max source overlap | 8 |
| Avg sources per IP | 1.72 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,471 | 25,800 | 51.6% |
| SGB (Turkiye) | 9,796 | 204 | 98.0% |
| Stamparm IPsum | 7,504 | 30,811 | 19.6% |
| CINS Army | 4,569 | 10,431 | 30.5% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| Blocklist.de (bots) | 1,246 | 1,538 | 44.8% |
| Blocklist.de (mail) | 991 | 12,404 | 7.4% |
| BinaryDefense | 758 | 3,258 | 18.9% |
| AbuseIPDB | 679 | 9,321 | 6.8% |
| Tor Exit Nodes | 627 | 631 | 49.8% |
| GreenSnow | 280 | 5,294 | 5.0% |
| AlienVault OTX | 145 | 30 | 82.9% |
| Blocklist.de (ssh) | 107 | 4,946 | 2.1% |
| Spamhaus DROPv6 | 86 | 0 | 100.0% |
| Blocklist.de (apache) | 79 | 8,884 | 0.9% |
| Blocklist.de (strongips) | 65 | 271 | 19.3% |
| Emerging Threats | 16 | 509 | 3.0% |
| Blocklist.de (all) | 0 | 0 | N/A |
| Blocklist.de (bruteforcelogin) | 0 | 783 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,810 |
| CINS Army & Stamparm IPsum | 9,560 |
| Stamparm IPsum & AbuseIPDB | 8,541 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 7,084 |
| CINS Army & RTBH (Turkiye) | 5,740 |
| Blocklist.de (ssh) & Stamparm IPsum | 4,842 |
| GreenSnow & RTBH (Turkiye) | 4,743 |
| GreenSnow & Stamparm IPsum | 4,448 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 4,060 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 48 | 2026-06-10 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 53,271 | OK |
| Stamparm IPsum | 38,315 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,395 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,963 | OK |
| GreenSnow | 5,574 | OK |
| Blocklist.de (ssh) | 5,053 | OK |
| BinaryDefense | 4,016 | OK |
| Blocklist.de (bots) | 2,784 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,258 | OK |
| Blocklist.de (bruteforcelogin) | 783 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 336 | OK |
| AlienVault OTX | 175 | OK |
| Spamhaus DROPv6 | 86 | OK |
| Blocklist.de (all) | 0 | EMPTY |
