# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-07T20:38:11.693878+00:00
**Duration:** 35.86s
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
| Unique to single source | 60,140 |
| Found in multiple sources | 47,858 |
| Max source overlap | 9 |
| Avg sources per IP | 1.85 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 32,344 | 28,600 | 53.1% |
| SGB (Turkiye) | 9,759 | 241 | 97.6% |
| Stamparm IPsum | 7,372 | 30,296 | 19.6% |
| CINS Army | 6,385 | 8,615 | 42.6% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 1,056 | 8,944 | 10.6% |
| Tor Exit Nodes | 631 | 629 | 50.1% |
| BinaryDefense | 468 | 2,572 | 15.4% |
| GreenSnow | 210 | 4,152 | 4.8% |
| AlienVault OTX | 104 | 28 | 78.8% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 30 | 495 | 5.7% |
| Blocklist.de (strongips) | 24 | 307 | 7.3% |
| Blocklist.de (all) | 22 | 23,412 | 0.1% |
| Blocklist.de (ssh) | 0 | 4,877 | 0.0% |
| Blocklist.de (mail) | 0 | 12,798 | 0.0% |
| Blocklist.de (apache) | 0 | 8,757 | 0.0% |
| Blocklist.de (bots) | 0 | 4,338 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 562 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 23,090 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,798 |
| Blocklist.de (all) & RTBH (Turkiye) | 10,723 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,757 |
| Blocklist.de (all) & Stamparm IPsum | 8,289 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Stamparm IPsum & AbuseIPDB | 7,841 |
| CINS Army & Stamparm IPsum | 7,622 |
| RTBH (Turkiye) & AbuseIPDB | 6,742 |
| Blocklist.de (all) & Blocklist.de (ssh) | 4,877 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 32 | 2026-06-07 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 60,944 | OK |
| Stamparm IPsum | 37,668 | OK |
| Blocklist.de (all) | 23,434 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,798 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,757 | OK |
| Blocklist.de (ssh) | 4,877 | OK |
| GreenSnow | 4,362 | OK |
| Blocklist.de (bots) | 4,338 | OK |
| BinaryDefense | 3,040 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 562 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 331 | OK |
| AlienVault OTX | 132 | OK |
| Spamhaus DROPv6 | 93 | OK |
