# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-11T07:05:21.679762+00:00
**Duration:** 733.08s
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
| Emerging Threats | ConnectTimeout: HTTPSConnectionPool(host='rules.emergingthreats.net', port=443): Max retries exceeded with url: /blockrules/compromised-ips.txt (Caused by ConnectTimeoutError(<HTTPSConnection(host='ru | 527 IPs from cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 57,630 |
| Found in multiple sources | 47,742 |
| Max source overlap | 9 |
| Avg sources per IP | 1.93 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 28,843 | 27,591 | 51.1% |
| SGB (Turkiye) | 9,767 | 233 | 97.7% |
| Stamparm IPsum | 7,968 | 32,159 | 19.9% |
| CINS Army | 5,920 | 9,080 | 39.5% |
| Spamhaus DROP | 1,660 | 0 | 100.0% |
| AbuseIPDB | 1,285 | 8,715 | 12.8% |
| BinaryDefense | 868 | 3,400 | 20.3% |
| Tor Exit Nodes | 616 | 643 | 48.9% |
| GreenSnow | 383 | 5,084 | 7.0% |
| AlienVault OTX | 152 | 27 | 84.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 38 | 24,631 | 0.2% |
| Blocklist.de (strongips) | 19 | 323 | 5.6% |
| Emerging Threats | 17 | 510 | 3.2% |
| Blocklist.de (bots) | 1 | 1,903 | 0.1% |
| Blocklist.de (ssh) | 0 | 7,803 | 0.0% |
| Blocklist.de (mail) | 0 | 13,451 | 0.0% |
| Blocklist.de (apache) | 0 | 9,141 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 977 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,177 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,447 |
| Blocklist.de (all) & RTBH (Turkiye) | 11,644 |
| Blocklist.de (all) & Stamparm IPsum | 11,319 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,138 |
| CINS Army & Stamparm IPsum | 8,072 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,900 |
| Blocklist.de (all) & Blocklist.de (ssh) | 7,801 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 6,598 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 56 | 2026-06-11 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |
| Emerging Threats | 1 | 2026-06-11 | ConnectTimeout: HTTPSConnectionPool(host='rules.emergingthre |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,434 | OK |
| Stamparm IPsum | 40,127 | OK |
| Blocklist.de (all) | 24,669 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,451 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,141 | OK |
| Blocklist.de (ssh) | 7,803 | OK |
| GreenSnow | 5,467 | OK |
| BinaryDefense | 4,268 | OK |
| Blocklist.de (bots) | 1,904 | OK |
| Spamhaus DROP | 1,660 | OK |
| Tor Exit Nodes | 1,259 | OK |
| Blocklist.de (bruteforcelogin) | 977 | OK |
| Emerging Threats | 527 | CACHED |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 179 | OK |
| Spamhaus DROPv6 | 93 | OK |
