# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-09T22:50:46.258552+00:00
**Duration:** 44.16s
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
| Unique to single source | 55,618 |
| Found in multiple sources | 44,925 |
| Max source overlap | 9 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 26,698 | 26,369 | 50.3% |
| SGB (Turkiye) | 9,796 | 204 | 98.0% |
| Stamparm IPsum | 7,856 | 28,750 | 21.5% |
| CINS Army | 6,727 | 8,273 | 44.8% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| AbuseIPDB | 797 | 9,203 | 8.0% |
| BinaryDefense | 719 | 3,023 | 19.2% |
| Tor Exit Nodes | 651 | 607 | 51.7% |
| GreenSnow | 382 | 4,428 | 7.9% |
| AlienVault OTX | 145 | 30 | 82.9% |
| Spamhaus DROPv6 | 86 | 0 | 100.0% |
| Blocklist.de (strongips) | 62 | 274 | 18.5% |
| Blocklist.de (all) | 31 | 22,623 | 0.1% |
| Emerging Threats | 8 | 517 | 1.5% |
| Blocklist.de (ssh) | 0 | 5,021 | 0.0% |
| Blocklist.de (mail) | 0 | 13,275 | 0.0% |
| Blocklist.de (apache) | 0 | 8,919 | 0.0% |
| Blocklist.de (bots) | 0 | 2,942 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 747 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,616 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,270 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,475 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,919 |
| Blocklist.de (all) & Stamparm IPsum | 8,831 |
| Stamparm IPsum & AbuseIPDB | 8,206 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,327 |
| RTBH (Turkiye) & AbuseIPDB | 7,075 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,016 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 47 | 2026-06-09 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 53,067 | OK |
| Stamparm IPsum | 36,606 | OK |
| Blocklist.de (all) | 22,654 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,275 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,919 | OK |
| Blocklist.de (ssh) | 5,021 | OK |
| GreenSnow | 4,810 | OK |
| BinaryDefense | 3,742 | OK |
| Blocklist.de (bots) | 2,942 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,258 | OK |
| Blocklist.de (bruteforcelogin) | 747 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 336 | OK |
| AlienVault OTX | 175 | OK |
| Spamhaus DROPv6 | 86 | OK |
