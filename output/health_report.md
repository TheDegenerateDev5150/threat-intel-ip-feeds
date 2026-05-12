# IP Blacklist Aggregator - Health Report

**Date:** 2026-05-12T23:48:19.476026+00:00
**Duration:** 192.96s
**Successful:** 19/20

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| SGB (Turkiye) | ConnectTimeout: HTTPSConnectionPool(host='siberguvenlik.gov.tr', port=443): Max retries exceeded with url: /api/address/index?type=ip&page=1 (Caused by ConnectTimeoutError(<HTTPSConnection(host='siber | No cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 130,515 |
| Found in multiple sources | 47,131 |
| Max source overlap | 9 |
| Avg sources per IP | 1.54 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| DShield | 91,948 | 15,827 | 85.3% |
| RTBH (Turkiye) | 21,604 | 17,556 | 55.2% |
| Stamparm IPsum | 6,653 | 29,193 | 18.6% |
| CINS Army | 5,591 | 9,409 | 37.3% |
| Spamhaus DROP | 1,611 | 0 | 100.0% |
| GreenSnow | 1,185 | 3,751 | 24.0% |
| AbuseIPDB | 754 | 9,246 | 7.5% |
| BinaryDefense | 612 | 1,321 | 31.7% |
| AlienVault OTX | 212 | 2 | 99.1% |
| Blocklist.de (all) | 191 | 23,346 | 0.8% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (strongips) | 52 | 273 | 16.0% |
| Tor Exit Nodes | 4 | 1,349 | 0.3% |
| Blocklist.de (mail) | 2 | 13,849 | 0.0% |
| Emerging Threats | 2 | 420 | 0.5% |
| Blocklist.de (ssh) | 0 | 4,828 | 0.0% |
| Blocklist.de (apache) | 0 | 9,460 | 0.0% |
| Blocklist.de (bots) | 0 | 2,820 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 1,279 | 0.0% |
| SGB (Turkiye) | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 15,503 |
| DShield & Stamparm IPsum | 14,261 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,844 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,460 |
| DShield & RTBH (Turkiye) | 8,687 |
| CINS Army & Stamparm IPsum | 8,308 |
| Blocklist.de (all) & Stamparm IPsum | 8,246 |
| Stamparm IPsum & AbuseIPDB | 8,028 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| RTBH (Turkiye) & AbuseIPDB | 5,116 |

## 1 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| SGB (Turkiye) | Never | 3 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 3 | 2026-05-12 | ConnectTimeout: HTTPSConnectionPool(host='siberguvenlik.gov. |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| DShield | 107,775 | OK |
| RTBH (Turkiye) | 39,160 | OK |
| Stamparm IPsum | 35,846 | OK |
| Blocklist.de (all) | 23,537 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,851 | OK |
| AbuseIPDB | 10,000 | OK |
| Blocklist.de (apache) | 9,460 | OK |
| GreenSnow | 4,936 | OK |
| Blocklist.de (ssh) | 4,828 | OK |
| Blocklist.de (bots) | 2,820 | OK |
| BinaryDefense | 1,933 | OK |
| Spamhaus DROP | 1,611 | OK |
| Tor Exit Nodes | 1,353 | OK |
| Blocklist.de (bruteforcelogin) | 1,279 | OK |
| Emerging Threats | 422 | OK |
| Blocklist.de (strongips) | 325 | OK |
| AlienVault OTX | 214 | OK |
| Spamhaus DROPv6 | 94 | OK |
| SGB (Turkiye) | 0 | FAILED |
