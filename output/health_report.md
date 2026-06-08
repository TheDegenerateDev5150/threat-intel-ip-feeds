# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-08T19:35:25.946902+00:00
**Duration:** 39.14s
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
| Unique to single source | 59,030 |
| Found in multiple sources | 46,631 |
| Max source overlap | 8 |
| Avg sources per IP | 1.84 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,487 | 25,576 | 54.4% |
| SGB (Turkiye) | 9,761 | 239 | 97.6% |
| Stamparm IPsum | 7,917 | 29,958 | 20.9% |
| CINS Army | 6,318 | 8,682 | 42.1% |
| Spamhaus DROP | 1,621 | 0 | 100.0% |
| AbuseIPDB | 1,003 | 8,997 | 10.0% |
| Tor Exit Nodes | 654 | 605 | 51.9% |
| BinaryDefense | 540 | 2,817 | 16.1% |
| GreenSnow | 404 | 4,200 | 8.8% |
| AlienVault OTX | 130 | 30 | 81.2% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 41 | 22,770 | 0.2% |
| Emerging Threats | 41 | 484 | 7.8% |
| Blocklist.de (strongips) | 20 | 315 | 6.0% |
| Blocklist.de (ssh) | 0 | 5,044 | 0.0% |
| Blocklist.de (mail) | 0 | 12,761 | 0.0% |
| Blocklist.de (apache) | 0 | 8,851 | 0.0% |
| Blocklist.de (bots) | 0 | 3,563 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 646 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,939 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,761 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,851 |
| Blocklist.de (all) & Stamparm IPsum | 8,580 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,335 |
| Stamparm IPsum & AbuseIPDB | 8,212 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,703 |
| RTBH (Turkiye) & AbuseIPDB | 6,729 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,044 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 38 | 2026-06-08 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,063 | OK |
| Stamparm IPsum | 37,875 | OK |
| Blocklist.de (all) | 22,811 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,761 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,851 | OK |
| Blocklist.de (ssh) | 5,044 | OK |
| GreenSnow | 4,604 | OK |
| Blocklist.de (bots) | 3,563 | OK |
| BinaryDefense | 3,357 | OK |
| Spamhaus DROP | 1,621 | OK |
| Tor Exit Nodes | 1,259 | OK |
| Blocklist.de (bruteforcelogin) | 646 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 335 | OK |
| AlienVault OTX | 160 | OK |
| Spamhaus DROPv6 | 93 | OK |
