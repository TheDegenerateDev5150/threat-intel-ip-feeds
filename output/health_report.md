# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-05T23:38:22.592549+00:00
**Duration:** 191.26s
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
| Unique to single source | 55,588 |
| Found in multiple sources | 44,891 |
| Max source overlap | 9 |
| Avg sources per IP | 1.88 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,758 | 27,784 | 50.0% |
| SGB (Turkiye) | 9,758 | 242 | 97.6% |
| CINS Army | 7,326 | 7,674 | 48.8% |
| Stamparm IPsum | 6,583 | 27,828 | 19.1% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 856 | 9,144 | 8.6% |
| Tor Exit Nodes | 680 | 566 | 54.6% |
| GreenSnow | 357 | 5,459 | 6.1% |
| BinaryDefense | 335 | 2,061 | 14.0% |
| AlienVault OTX | 113 | 33 | 77.4% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 72 | 22,023 | 0.3% |
| Emerging Threats | 8 | 517 | 1.5% |
| Blocklist.de (strongips) | 7 | 321 | 2.1% |
| Blocklist.de (ssh) | 0 | 5,103 | 0.0% |
| Blocklist.de (mail) | 0 | 12,396 | 0.0% |
| Blocklist.de (apache) | 0 | 8,940 | 0.0% |
| Blocklist.de (bots) | 0 | 2,812 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 748 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,491 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,396 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,005 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,940 |
| Blocklist.de (all) & Stamparm IPsum | 8,693 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,386 |
| RTBH (Turkiye) & AbuseIPDB | 7,063 |
| CINS Army & Stamparm IPsum | 5,675 |
| Blocklist.de (all) & Blocklist.de (ssh) | 5,093 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 14 | 2026-06-05 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |
| CINS Army | 1 | 2026-06-05 | ConnectTimeout: HTTPSConnectionPool(host='cinsscore.com', po |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,542 | OK |
| Stamparm IPsum | 34,411 | OK |
| Blocklist.de (all) | 22,095 | OK |
| CINS Army | 15,000 | CACHED |
| Blocklist.de (mail) | 12,396 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,940 | OK |
| GreenSnow | 5,816 | OK |
| Blocklist.de (ssh) | 5,103 | OK |
| Blocklist.de (bots) | 2,812 | OK |
| BinaryDefense | 2,396 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,246 | OK |
| Blocklist.de (bruteforcelogin) | 748 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 328 | OK |
| AlienVault OTX | 146 | OK |
| Spamhaus DROPv6 | 93 | OK |
