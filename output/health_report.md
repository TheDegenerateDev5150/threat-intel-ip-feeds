# IP Blacklist Aggregator - Health Report

**Date:** 2026-08-11T07:37:28.443242+00:00
**Duration:** 193.49s
**Successful:** 18/19

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| SGB (Turkiye) | ConnectTimeout: HTTPSConnectionPool(host='siberguvenlik.gov.tr', port=443): Max retries exceeded with url: /api/address/index?type=ip&page=1&per-page=9999 (Caused by ConnectTimeoutError(<HTTPSConnecti | 10,000 IPs from cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 54,714 |
| Found in multiple sources | 48,403 |
| Max source overlap | 9 |
| Avg sources per IP | 1.93 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 27,402 | 28,102 | 49.4% |
| SGB (Turkiye) | 9,566 | 434 | 95.7% |
| Stamparm IPsum | 6,762 | 26,547 | 20.3% |
| CINS Army | 6,175 | 8,825 | 41.2% |
| Spamhaus DROP | 1,686 | 0 | 100.0% |
| AbuseIPDB | 1,119 | 8,881 | 11.2% |
| Tor Exit Nodes | 759 | 624 | 54.9% |
| BinaryDefense | 563 | 2,473 | 18.5% |
| GreenSnow | 318 | 3,386 | 8.6% |
| AlienVault OTX | 248 | 48 | 83.8% |
| Spamhaus DROPv6 | 91 | 0 | 100.0% |
| Blocklist.de (all) | 10 | 27,662 | 0.0% |
| Emerging Threats | 9 | 540 | 1.6% |
| Blocklist.de (strongips) | 6 | 339 | 1.7% |
| Blocklist.de (ssh) | 0 | 10,351 | 0.0% |
| Blocklist.de (mail) | 0 | 12,696 | 0.0% |
| Blocklist.de (apache) | 0 | 9,374 | 0.0% |
| Blocklist.de (bots) | 0 | 3,136 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 1,050 | 0.0% |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 18,570 |
| Blocklist.de (all) & RTBH (Turkiye) | 13,648 |
| Blocklist.de (all) & Blocklist.de (mail) | 12,696 |
| Blocklist.de (all) & Blocklist.de (ssh) | 10,351 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,374 |
| Blocklist.de (ssh) & RTBH (Turkiye) | 8,852 |
| Blocklist.de (all) & Stamparm IPsum | 8,817 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| CINS Army & Stamparm IPsum | 7,808 |
| Stamparm IPsum & AbuseIPDB | 7,802 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 1 | 2026-08-11 | ConnectTimeout: HTTPSConnectionPool(host='siberguvenlik.gov. |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 55,504 | OK |
| Stamparm IPsum | 33,309 | OK |
| Blocklist.de (all) | 27,672 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 12,696 | OK |
| Blocklist.de (ssh) | 10,351 | OK |
| AbuseIPDB | 10,000 | OK |
| SGB (Turkiye) | 10,000 | CACHED |
| Blocklist.de (apache) | 9,374 | OK |
| GreenSnow | 3,704 | OK |
| Blocklist.de (bots) | 3,136 | OK |
| BinaryDefense | 3,036 | OK |
| Spamhaus DROP | 1,686 | OK |
| Tor Exit Nodes | 1,383 | OK |
| Blocklist.de (bruteforcelogin) | 1,050 | OK |
| Emerging Threats | 549 | OK |
| Blocklist.de (strongips) | 345 | OK |
| AlienVault OTX | 296 | OK |
| Spamhaus DROPv6 | 91 | OK |
