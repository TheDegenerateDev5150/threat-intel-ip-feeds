# IP Blacklist Aggregator - Health Report

**Date:** 2026-06-08T01:34:26.110028+00:00
**Duration:** 34.61s
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
| Unique to single source | 54,793 |
| Found in multiple sources | 46,806 |
| Max source overlap | 9 |
| Avg sources per IP | 1.91 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 28,523 | 26,090 | 52.2% |
| SGB (Turkiye) | 9,765 | 235 | 97.7% |
| Stamparm IPsum | 7,302 | 30,573 | 19.3% |
| CINS Army | 4,864 | 10,136 | 32.4% |
| Spamhaus DROP | 1,642 | 0 | 100.0% |
| AbuseIPDB | 1,027 | 8,973 | 10.3% |
| Tor Exit Nodes | 653 | 607 | 51.8% |
| BinaryDefense | 550 | 2,807 | 16.4% |
| GreenSnow | 183 | 4,856 | 3.6% |
| AlienVault OTX | 105 | 27 | 79.5% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Emerging Threats | 41 | 484 | 7.8% |
| Blocklist.de (strongips) | 23 | 310 | 6.9% |
| Blocklist.de (all) | 22 | 23,151 | 0.1% |
| Blocklist.de (ssh) | 0 | 4,952 | 0.0% |
| Blocklist.de (mail) | 0 | 12,581 | 0.0% |
| Blocklist.de (apache) | 0 | 8,764 | 0.0% |
| Blocklist.de (bots) | 0 | 4,242 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 568 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 21,708 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,581 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,755 |
| CINS Army & Stamparm IPsum | 9,330 |
| Blocklist.de (all) & Stamparm IPsum | 9,097 |
| Blocklist.de (all) & Blocklist.de (apache) | 8,764 |
| Stamparm IPsum & AbuseIPDB | 8,212 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 6,644 |
| CINS Army & RTBH (Turkiye) | 5,506 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 34 | 2026-06-08 | HttpError: HTTP 429: <html>
<head><title>429 Too Many Reque |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 54,613 | OK |
| Stamparm IPsum | 37,875 | OK |
| Blocklist.de (all) | 23,173 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,581 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 8,764 | OK |
| GreenSnow | 5,039 | OK |
| Blocklist.de (ssh) | 4,952 | OK |
| Blocklist.de (bots) | 4,242 | OK |
| BinaryDefense | 3,357 | OK |
| Spamhaus DROP | 1,642 | OK |
| Tor Exit Nodes | 1,260 | OK |
| Blocklist.de (bruteforcelogin) | 568 | OK |
| Emerging Threats | 525 | OK |
| Blocklist.de (strongips) | 333 | OK |
| AlienVault OTX | 132 | OK |
| Spamhaus DROPv6 | 93 | OK |
