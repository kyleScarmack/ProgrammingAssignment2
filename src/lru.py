from collections import OrderedDict


def run_lru(k, reqs):
    # k = cache capacity (k >= 1)
    # reqs = sequence of (m) requests (r_1, r_2,.., r_m)

    cache = OrderedDict()  # Keys are cache items in LRU -> MRU order
    misses = 0

    for r in reqs:
        if r in cache:
            cache.move_to_end(r)  # Mark as most recently used
            continue

        misses += 1

        if len(cache) == k:  # Cache full: evict least recently used
            cache.popitem(last=False)

        cache[r] = True

    return misses
