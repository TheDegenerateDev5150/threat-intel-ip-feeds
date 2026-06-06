# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-06T14:53:25.214676+00:00
**Duration:** 36.14s
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
| Unique to single source | 58,102 |
| Found in multiple sources | 46,880 |
| Max source overlap | 9 |
| Avg sources per IP | 1.86 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 30,695 | 26,113 | 54.0% |
| SGB (Turkiye) | 9,761 | 239 | 97.6% |
| Stamparm IPsum | 7,379 | 30,577 | 19.4% |
| CINS Army | 6,206 | 8,794 | 41.4% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 726 | 9,274 | 7.3% |
| Tor Exit Nodes | 623 | 621 | 50.1% |
| BinaryDefense | 413 | 2,331 | 15.1% |
| GreenSnow | 340 | 4,280 | 7.4% |
| AlienVault OTX | 112 | 30 | 78.9% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (all) | 80 | 22,903 | 0.3% |
| Blocklist.de (strongips) | 18 | 311 | 5.5% |
| Emerging Threats | 11 | 514 | 2.1% |
| Blocklist.de (mail) | 2 | 12,464 | 0.0% |
| Blocklist.de (bots) | 1 | 3,867 | 0.0% |
| Blocklist.de (ssh) | 0 | 4,970 | 0.0% |
| Blocklist.de (apache) | 0 | 8,827 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 623 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 22,488 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,458 |
| Blocklist.de (all) & Stamparm IPsum | 8,892 |
| Blocklist.de (all) & RTBH (Turkiye) | 8,859 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,827 |
| Stamparm IPsum & AbuseIPDB | 8,369 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,885 |
| RTBH (Turkiye) & AbuseIPDB | 6,922 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,970 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 19 | 2026-06-06 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 56,808 | OK |
| Stamparm IPsum | 37,956 | OK |
| Blocklist.de (all) | 22,983 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,466 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,827 | OK |
| Blocklist.de (ssh) | 4,970 | OK |
| GreenSnow | 4,620 | OK |
| Blocklist.de (bots) | 3,868 | OK |
| BinaryDefense | 2,744 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,244 | OK |
| Blocklist.de (bruteforcelogin) | 623 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 329 | OK |
| AlienVault OTX | 142 | OK |
| Spamhaus DROPv6 | 93 | OK |
