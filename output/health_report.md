# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-12T16:27:47.156784+00:00
**Duration:** 193.59s
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
| CINS Army | ConnectTimeout: HTTPSConnectionPool(host='cinsscore.com', port=443): Max retries exceeded with url: /list/ci-badguys.txt (Caused by ConnectTimeoutError(<HTTPSConnection(host='cinsscore.com', port=443) | 15,000 IPs from cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 59,096 |
| Found in multiple sources | 46,804 |
| Max source overlap | 8 |
| Avg sources per IP | 1.9 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 31,649 | 27,011 | 54.0% |
| SGB (Turkiye) | 9,780 | 220 | 97.8% |
| Stamparm IPsum | 7,044 | 30,480 | 18.8% |
| CINS Army | 5,670 | 9,330 | 37.8% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,010 | 3,497 | 22.4% |
| AbuseIPDB | 803 | 9,197 | 8.0% |
| Tor Exit Nodes | 658 | 605 | 52.1% |
| GreenSnow | 471 | 4,373 | 9.7% |
| AlienVault OTX | 155 | 23 | 87.1% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 36 | 24,003 | 0.1% |
| Blocklist.de (strongips) | 14 | 327 | 4.1% |
| Emerging Threats | 13 | 513 | 2.5% |
| Blocklist.de (bruteforcelogin) | 2 | 769 | 0.3% |
| Blocklist.de (ssh) | 0 | 7,842 | 0.0% |
| Blocklist.de (mail) | 0 | 13,027 | 0.0% |
| Blocklist.de (apache) | 0 | 8,956 | 0.0% |
| Blocklist.de (bots) | 0 | 1,718 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,362 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,027 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,900 |
| Blocklist.de (all) & Stamparm IPsum | 9,968 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,956 |
| CINS Army & Stamparm IPsum | 8,284 |
| Stamparm IPsum & AbuseIPDB | 8,281 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,842 |
| RTBH (Turkiye) & AbuseIPDB | 6,944 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 65 | 2026-06-12 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |
| CINS Army | 1 | 2026-06-12 | ConnectTimeout: HTTPSConnectionPool(host='cinsscore.com', po |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 58,660 | OK |
| Stamparm IPsum | 37,524 | OK |
| Blocklist.de (all) | 24,039 | OK |
| CINS Army | 15,000 | CACHED |
| Blocklist.de (mail) | 13,027 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,956 | OK |
| Blocklist.de (ssh) | 7,842 | OK |
| GreenSnow | 4,844 | OK |
| BinaryDefense | 4,507 | OK |
| Blocklist.de (bots) | 1,718 | OK |
| Spamhaus DROP | 1,697 | OK |
| Tor Exit Nodes | 1,263 | OK |
| Blocklist.de (bruteforcelogin) | 771 | OK |
| Emerging Threats | 526 | OK |
| Blocklist.de (strongips) | 341 | OK |
| AlienVault OTX | 178 | OK |
| Spamhaus DROPv6 | 94 | OK |
