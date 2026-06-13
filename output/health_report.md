# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-13T11:24:31.443411+00:00
**Duration:** 65.5s
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
| Unique to single source | 59,761 |
| Found in multiple sources | 45,569 |
| Max source overlap | 9 |
| Avg sources per IP | 1.87 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,970 | 25,492 | 55.6% |
| SGB (Turkiye) | 9,777 | 223 | 97.8% |
| Stamparm IPsum | 7,168 | 31,555 | 18.5% |
| CINS Army | 6,044 | 8,956 | 40.3% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,124 | 3,640 | 23.6% |
| AbuseIPDB | 760 | 9,240 | 7.6% |
| Tor Exit Nodes | 618 | 645 | 48.9% |
| GreenSnow | 307 | 4,801 | 6.0% |
| AlienVault OTX | 155 | 23 | 87.1% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 23 | 21,699 | 0.1% |
| Emerging Threats | 17 | 511 | 3.2% |
| Blocklist.de (strongips) | 7 | 330 | 2.1% |
| Blocklist.de (ssh) | 0 | 5,692 | 0.0% |
| Blocklist.de (mail) | 0 | 12,853 | 0.0% |
| Blocklist.de (apache) | 0 | 8,989 | 0.0% |
| Blocklist.de (bots) | 0 | 1,698 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 829 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,349 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,853 |
| Blocklist.de (all) & Stamparm IPsum | 9,878 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,989 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,690 |
| Stamparm IPsum & AbuseIPDB | 8,419 |
| CINS Army & Stamparm IPsum | 7,994 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 7,156 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,692 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 71 | 2026-06-13 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 57,462 | OK |
| Stamparm IPsum | 38,723 | OK |
| Blocklist.de (all) | 21,722 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,853 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,989 | OK |
| Blocklist.de (ssh) | 5,692 | OK |
| GreenSnow | 5,108 | OK |
| BinaryDefense | 4,764 | OK |
| Blocklist.de (bots) | 1,698 | OK |
| Spamhaus DROP | 1,697 | OK |
| Tor Exit Nodes | 1,263 | OK |
| Blocklist.de (bruteforcelogin) | 829 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 337 | OK |
| AlienVault OTX | 178 | OK |
| Spamhaus DROPv6 | 94 | OK |
