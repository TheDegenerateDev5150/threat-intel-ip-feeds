# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-12T23:51:25.485301+00:00
**Duration:** 56.01s
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
| Unique to single source | 56,126 |
| Found in multiple sources | 47,148 |
| Max source overlap | 9 |
| Avg sources per IP | 1.94 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,637 | 28,638 | 49.1% |
| SGB (Turkiye) | 9,776 | 224 | 97.8% |
| Stamparm IPsum | 7,457 | 30,067 | 19.9% |
| CINS Army | 6,326 | 8,674 | 42.2% |
| Spamhaus DROP | 1,697 | 0 | 100.0% |
| BinaryDefense | 1,012 | 3,495 | 22.5% |
| AbuseIPDB | 831 | 9,169 | 8.3% |
| Tor Exit Nodes | 657 | 604 | 52.1% |
| GreenSnow | 420 | 5,536 | 7.1% |
| AlienVault OTX | 155 | 23 | 87.1% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (all) | 44 | 24,169 | 0.2% |
| Blocklist.de (strongips) | 13 | 329 | 3.8% |
| Emerging Threats | 6 | 522 | 1.1% |
| Blocklist.de (mail) | 1 | 13,006 | 0.0% |
| Blocklist.de (ssh) | 0 | 8,216 | 0.0% |
| Blocklist.de (apache) | 0 | 8,903 | 0.0% |
| Blocklist.de (bots) | 0 | 1,587 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 741 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,768 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,006 |
| Blocklist.de (all) & RTBH (Turkiye) | 12,253 |
| Blocklist.de (all) & Stamparm IPsum | 9,654 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,903 |
| Stamparm IPsum & AbuseIPDB | 8,281 |
| Blocklist.de (all) & Blocklist.de (ssh) | 8,216 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,667 |
| RTBH (Turkiye) & AbuseIPDB | 7,082 |

## 2 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| Feodo Tracker | 2026-05-12 | 0 |
| USOM (Turkiye) | 2026-05-12 | 0 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 68 | 2026-06-12 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,275 | OK |
| Stamparm IPsum | 37,524 | OK |
| Blocklist.de (all) | 24,213 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,007 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,903 | OK |
| Blocklist.de (ssh) | 8,216 | OK |
| GreenSnow | 5,956 | OK |
| BinaryDefense | 4,507 | OK |
| Spamhaus DROP | 1,697 | OK |
| Blocklist.de (bots) | 1,587 | OK |
| Tor Exit Nodes | 1,261 | OK |
| Blocklist.de (bruteforcelogin) | 741 | OK |
| Emerging Threats | 528 | OK |
| Blocklist.de (strongips) | 342 | OK |
| AlienVault OTX | 178 | OK |
| Spamhaus DROPv6 | 94 | OK |
