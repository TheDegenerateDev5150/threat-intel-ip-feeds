# IP Blacklist Aggregator - Health Report

**Date:** 2026-05-13T05:48:42.842016+00:00
**Duration:** 190.54s
**Successful:** 19/20

## Failed Sources This Run

| Source | Error | Cached |
|--------|------|--------|
| SGB (Turkiye) | ConnectTimeout: HTTPSConnectionPool(host='siberguvenlik.gov.tr', port=443): Max retries exceeded with url: /api/address/index?type=ip&page=1&per-page=10000 (Caused by ConnectTimeoutError(<HTTPSConnect | No cache |

## Deduplication & Source Overlap

| Metric | Value |
|--------|-------|
| Unique to single source | 57,761 |
| Found in multiple sources | 46,633 |
| Max source overlap | 9 |
| Avg sources per IP | 1.93 |

### Per-Source Contribution

| Source | Unique | Shared | Unique % |
|--------|--------|--------|----------|
| RTBH (Turkiye) | 22,371 | 17,137 | 56.6% |
| DShield | 20,528 | 12,000 | 63.1% |
| Stamparm IPsum | 6,118 | 30,979 | 16.5% |
| CINS Army | 3,553 | 11,447 | 23.7% |
| Spamhaus DROP | 1,611 | 0 | 100.0% |
| GreenSnow | 932 | 4,108 | 18.5% |
| BinaryDefense | 804 | 1,583 | 33.7% |
| Tor Exit Nodes | 694 | 660 | 51.3% |
| AbuseIPDB | 678 | 9,322 | 6.8% |
| AlienVault OTX | 212 | 2 | 99.1% |
| Blocklist.de (all) | 108 | 23,576 | 0.5% |
| Spamhaus DROPv6 | 94 | 0 | 100.0% |
| Blocklist.de (strongips) | 52 | 275 | 15.9% |
| Blocklist.de (apache) | 3 | 9,427 | 0.0% |
| Emerging Threats | 3 | 419 | 0.7% |
| Blocklist.de (ssh) | 0 | 4,881 | 0.0% |
| Blocklist.de (mail) | 0 | 13,957 | 0.0% |
| Blocklist.de (bots) | 0 | 2,835 | 0.0% |
| Blocklist.de (bruteforcelogin) | 0 | 1,268 | 0.0% |
| SGB (Turkiye) | 0 | 0 | N/A |

### Top Source Pair Overlaps

| Pair | Shared IPs |
|------|-----------|
| Stamparm IPsum & RTBH (Turkiye) | 15,471 |
| Blocklist.de (all) & Blocklist.de (mail) | 13,957 |
| DShield & Stamparm IPsum | 11,352 |
| CINS Army & Stamparm IPsum | 10,400 |
| Blocklist.de (all) & Stamparm IPsum | 9,861 |
| Blocklist.de (all) & Blocklist.de (apache) | 9,427 |
| Stamparm IPsum & AbuseIPDB | 8,321 |
| Blocklist.de (mail) & Blocklist.de (apache) | 7,967 |
| DShield & RTBH (Turkiye) | 6,227 |
| CINS Army & RTBH (Turkiye) | 5,720 |

## 1 Sources Stale (30+ days)

| Source | Last Success | Consecutive Failures |
|--------|-------------|---------------------|
| SGB (Turkiye) | Never | 6 |

## Consecutively Failing Sources

| Source | Failures | Last Failure | Reason |
|--------|----------|-------------|--------|
| SGB (Turkiye) | 6 | 2026-05-13 | ConnectTimeout: HTTPSConnectionPool(host='siberguvenlik.gov. |

## All Sources

| Source | IPs | Status |
|--------|-----|--------|
| RTBH (Turkiye) | 39,508 | OK |
| Stamparm IPsum | 37,097 | OK |
| DShield | 32,528 | OK |
| Blocklist.de (all) | 23,684 | OK |
| CINS Army | 15,000 | OK |
| Blocklist.de (mail) | 13,957 | OK |
| AbuseIPDB | 10,000 | OK |
| Blocklist.de (apache) | 9,430 | OK |
| GreenSnow | 5,040 | OK |
| Blocklist.de (ssh) | 4,881 | OK |
| Blocklist.de (bots) | 2,835 | OK |
| BinaryDefense | 2,387 | OK |
| Spamhaus DROP | 1,611 | OK |
| Tor Exit Nodes | 1,354 | OK |
| Blocklist.de (bruteforcelogin) | 1,268 | OK |
| Emerging Threats | 422 | OK |
| Blocklist.de (strongips) | 327 | OK |
| AlienVault OTX | 214 | OK |
| Spamhaus DROPv6 | 94 | OK |
| SGB (Turkiye) | 0 | FAILED |
