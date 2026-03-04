import heapq


def run_optff(k, reqs):
    # k = cache capacity (k >= 1)
    # reqs = sequence of (m) requests (r_1, r_2,.., r_m)

    m = len(reqs)
    INF = float('inf')  # Means never requested again, so farthest in future

    # First, compute next occurrence for each position in reqs
    next_i = [INF] * m  # Stores index of next request, or INF if it never appears again
    last_pos = {}

    # Iterate backwards so we know the next occurrence of each item in O(m)
    for i in range(m - 1, -1, -1):
        r = reqs[i]
        next_i[i] = last_pos.get(r, INF)
        last_pos[r] = i

    # Next, simulate OPTFF using a priority queue to track which item is farthest in future
    cache = set()    # Items currently in cache
    cur_next = {}   # Maps item to its current next-use index (or INF)
    heap = []   # heapq is a Min Heap, so store (-next_use, item) to act like Max Heap
    misses = 0

    for i, r in enumerate(reqs):
        next_use = next_i[i]

        if r in cache:  # Item is already in cache, so hit and update its next-use
            cur_next[r] = next_use
            heapq.heappush(heap, (-next_use, r))
            continue

        misses += 1 # Otherwise, miss

        if len(cache) < k:  # If cache not full, insert new item
            cache.add(r)
            cur_next[r] = next_use
            heapq.heappush(heap, (-next_use, r))
            continue

        # Cache is full, evict farthest-in-future
        while True:
            neg_next_use, evict_item = heapq.heappop(heap)
            evict_next_use = -neg_next_use

            # Check if item still in cache and if its next-use is same as when added to heap
            if evict_item in cache and cur_next.get(evict_item, None) == evict_next_use:
                cache.remove(evict_item)
                del cur_next[evict_item]
                break

        # Insert new item after eviction
        cache.add(r)
        cur_next[r] = next_use
        heapq.heappush(heap, (-next_use, r))

    return misses