# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-04T21:53:44.397765+00:00
**Duration:** 82.44s
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
| Unique to single source | 51,274 |
| Found in multiple sources | 42,080 |
| Max source overlap | 8 |
| Avg sources per IP | 1.91 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 26,960 | 28,374 | 48.7% |
| SGB (Turkiye) | 9,745 | 255 | 97.5% |
| Stamparm IPsum | 9,556 | 25,729 | 27.1% |
| AbuseIPDB | 1,669 | 8,331 | 16.7% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| Tor Exit Nodes | 608 | 557 | 52.2% |
| GreenSnow | 474 | 4,722 | 9.1% |
| BinaryDefense | 253 | 1,860 | 12.0% |
| Blocklist.de (all) | 130 | 24,230 | 0.5% |
| AlienVault OTX | 118 | 39 | 75.2% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (strongips) | 8 | 319 | 2.4% |
| Emerging Threats | 7 | 523 | 1.3% |
| Blocklist.de (ssh) | 6 | 7,681 | 0.1% |
| Blocklist.de (bruteforcelogin) | 5 | 954 | 0.5% |
| Blocklist.de (mail) | 0 | 12,487 | 0.0% |
| Blocklist.de (apache) | 0 | 9,173 | 0.0% |
| Blocklist.de (bots) | 0 | 2,175 | 0.0% |
| CINS Army | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,238 |
| Blocklist.de (all) & RTBH (Turkiye) | 13,125 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,487 |
| Blocklist.de (all) & Stamparm IPsum | 10,700 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,173 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,670 |
| Stamparm IPsum & AbuseIPDB | 7,061 |
| RTBH (Turkiye) & AbuseIPDB | 6,891 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 6,739 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 5 | 2026-06-04 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,334 | OK |
| Stamparm IPsum | 35,285 | OK |
| Blocklist.de (all) | 24,360 | OK |
| Blocklist.de (mail) | 12,487 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,173 | OK |
| Blocklist.de (ssh) | 7,687 | OK |
| GreenSnow | 5,196 | OK |
| Blocklist.de (bots) | 2,175 | OK |
| BinaryDefense | 2,113 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,165 | OK |
| Blocklist.de (bruteforcelogin) | 959 | OK |
| Emerging Threats | 530 | OK |
| Blocklist.de (strongips) | 327 | OK |
| AlienVault OTX | 157 | OK |
| Spamhaus DROPv6 | 93 | OK |
| CINS Army | 0 | EMPTY |
