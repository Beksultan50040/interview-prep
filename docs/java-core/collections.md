# Collections

## Internals to know

- **`HashMap`:** array of buckets, hash spreading, collisions as linked list then red-black tree (bin size 8 and table size 64). Resizes at load factor 0.75, doubling capacity. Not thread-safe; concurrent modification can corrupt or loop in old versions.
- **`equals` and `hashCode` contract:** equal objects must have equal hash codes. Mutable keys break lookups.
- **`ArrayList` vs `LinkedList`:** `ArrayList` wins in nearly all cases due to cache locality.
- **`ArrayDeque`** is the default stack and queue.
- **`TreeMap`:** red-black tree, O(log n), sorted, needs consistent `Comparator`.
- **`LinkedHashMap`:** insertion or access order; `removeEldestEntry` gives a simple LRU cache.
- **`PriorityQueue`:** binary heap; iteration order is not sorted.
- **Immutable collections:** `List.of`, `Map.of`, `Collections.unmodifiableList` (a view, not a copy), `List.copyOf`.

## Complexity cheat sheet

| Structure | get | add | remove | contains |
|---|---|---|---|---|
| ArrayList | O(1) | O(1) amortized | O(n) | O(n) |
| LinkedList | O(n) | O(1) at ends | O(1) with iterator | O(n) |
| HashMap or HashSet | O(1) | O(1) | O(1) | O(1) |
| TreeMap or TreeSet | O(log n) | O(log n) | O(log n) | O(log n) |
| PriorityQueue | O(1) peek | O(log n) | O(log n) | O(n) |

## Common questions

- What happens when you put a key with the same hash but different `equals`?
- Fail-fast vs fail-safe iterators?
- How would you implement an LRU cache? (`LinkedHashMap` with access order, or a map plus doubly linked list.)
- Why is `Arrays.asList` fixed-size?
- Sequenced collections in Java 21: `getFirst`, `getLast`, `reversed`.
