# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-06T08:02:52.115804+00:00
**Duration:** 191.37s
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
| Unique to single source | 56,844 |
| Found in multiple sources | 46,491 |
| Max source overlap | 9 |
| Avg sources per IP | 1.89 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 29,992 | 26,236 | 53.3% |
| SGB (Turkiye) | 9,759 | 241 | 97.6% |
| Stamparm IPsum | 7,257 | 30,699 | 19.1% |
| CINS Army | 5,892 | 9,108 | 39.3% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| Tor Exit Nodes | 624 | 621 | 50.1% |
| AbuseIPDB | 615 | 9,385 | 6.2% |
| BinaryDefense | 413 | 2,331 | 15.1% |
| GreenSnow | 335 | 5,410 | 5.8% |
| AlienVault OTX | 113 | 30 | 79.0% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 71 | 22,722 | 0.3% |
| Blocklist.de (strongips) | 19 | 309 | 5.8% |
| Emerging Threats | 11 | 514 | 2.1% |
| Blocklist.de (bruteforcelogin) | 6 | 681 | 0.9% |
| Blocklist.de (ssh) | 1 | 5,010 | 0.0% |
| Blocklist.de (bots) | 1 | 3,512 | 0.0% |
| Blocklist.de (mail) | 0 | 12,528 | 0.0% |
| Blocklist.de (apache) | 0 | 8,904 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,380 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,528 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,284 |
| Blocklist.de (all) & Stamparm IPsum | 9,227 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,904 |
| Stamparm IPsum & AbuseIPDB | 8,664 |
| CINS Army & Stamparm IPsum | 8,324 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 7,099 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,996 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 16 | 2026-06-06 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |
| CINS Army | 1 | 2026-06-06 | ConnectTimeout: HTTPSConnectionPool(host='cinsscore.com', po |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,228 | OK |
| Stamparm IPsum | 37,956 | OK |
| Blocklist.de (all) | 22,793 | OK |
| CINS Army | 15,000 | CACHED |
| Blocklist.de (mail) | 12,528 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,904 | OK |
| GreenSnow | 5,745 | OK |
| Blocklist.de (ssh) | 5,011 | OK |
| Blocklist.de (bots) | 3,513 | OK |
| BinaryDefense | 2,744 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,245 | OK |
| Blocklist.de (bruteforcelogin) | 687 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 143 | OK |
| Spamhaus DROPv6 | 93 | OK |
