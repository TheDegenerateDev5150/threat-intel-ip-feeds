# IP Blacklist Aggregator - Health Report

**Date:** 2026-07-31T16:56:55.351398+00:00
**Duration:** 42.16s
**Successful:** 18/19

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| GreenSnow | ConnectionError: HTTPSConnectionPool(host='blocklist.greensnow.co', port=443): Max retries exceeded with url: /greensnow.txt (Caused by NameResolutionError("HTTPSConnection(host='blocklist.greensnow.c | 3,111 IPs from cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 63,017 |
| Found in multiple sources | 42,559 |
| Max source overlap | 9 |
| Avg sources per IP | 1.79 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 35,834 | 25,143 | 58.8% |
| SGB (Turkiye) | 9,616 | 384 | 96.2% |
| CINS Army | 7,372 | 7,628 | 49.1% |
| Stamparm IPsum | 6,123 | 25,475 | 19.4% |
| Spamhaus DROP | 1,665 | 0 | 100.0% |
| AbuseIPDB | 746 | 9,254 | 7.5% |
| Tor Exit Nodes | 710 | 653 | 52.1% |
| GreenSnow | 371 | 2,740 | 11.9% |
| BinaryDefense | 208 | 1,550 | 11.8% |
| AlienVault OTX | 197 | 44 | 81.7% |
| Spamhaus DROPv6 | 93 | 0 | 100.0% |
| Blocklist.de (strongips) | 32 | 311 | 9.3% |
| Blocklist.de (all) | 31 | 21,737 | 0.1% |
| Emerging Threats | 15 | 571 | 2.6% |
| Blocklist.de (mail) | 2 | 12,672 | 0.0% |
| Blocklist.de (bots) | 2 | 3,358 | 0.1% |
| Blocklist.de (ssh) | 0 | 4,438 | 0.0% |
| Blocklist.de (apache) | 0 | 9,104 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 992 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 19,578 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,656 |
| Blocklist.de (all) & RTBH (Turkiye) | 9,130 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,104 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| Blocklist.de (all) & Stamparm IPsum | 7,901 |
| Stamparm IPsum & AbuseIPDB | 7,756 |
| RTBH (Turkiye) & AbuseIPDB | 7,730 |
| CINS Army & Stamparm IPsum | 6,583 |
| CINS Army & RTBH (Turkiye) | 4,745 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| GreenSnow | 1 | 2026-07-31 | ConnectionError: HTTPSConnectionPool(host='blocklist.greensn |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 60,977 | OK |
| Stamparm IPsum | 31,598 | OK |
| Blocklist.de (all) | 21,768 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,674 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | OK |
| Blocklist.de (apache) | 9,104 | OK |
| Blocklist.de (ssh) | 4,438 | OK |
| Blocklist.de (bots) | 3,360 | OK |
| GreenSnow | 3,111 | CACHED |
| BinaryDefense | 1,758 | OK |
| Spamhaus DROP | 1,665 | OK |
| Tor Exit Nodes | 1,363 | OK |
| Blocklist.de (bruteforcelogin) | 992 | OK |
| Emerging Threats | 586 | OK |
| Blocklist.de (strongips) | 343 | OK |
| AlienVault OTX | 241 | OK |
| Spamhaus DROPv6 | 93 | OK |
