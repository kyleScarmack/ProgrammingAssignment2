from collections import deque


def run_fifo(k, reqs):
    # k = cache capacity (k >= 1)
    # reqs = sequence of (m) requests (r_1, r_2,.., r_m)

    cache = set()   # Items currently in cache
    q = deque() # FIFO order (oldest at front)
    misses = 0

    for r in reqs:
        if r in cache:  # Item is already in cache, so hit
            continue

        misses += 1 # Otherwise, miss

        if len(cache) == k: # Cache is full, evict the oldest item
            oldest = q.popleft()
            cache.remove(oldest)

        cache.add(r)    # If cache not full, insert new item
        q.append(r)

    return misses