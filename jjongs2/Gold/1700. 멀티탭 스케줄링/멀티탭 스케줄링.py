from sys import stdin

read = stdin.readline


def count_unplug(outlet_count, plug_count, plugs):
    if outlet_count >= plug_count:
        return 0
    unplug_count = 0
    plugged = set()
    for i, plug in enumerate(plugs):
        if plug in plugged:
            continue
        if len(plugged) < outlet_count:
            plugged.add(plug)
            continue
        indexes = []
        for p in plugged:
            try:
                indexes.append((plugs.index(p, i + 1), p))
            except ValueError:
                plugged.remove(p)
                break
        else:
            plugged.remove(max(indexes)[1])
        plugged.add(plug)
        unplug_count += 1
    return unplug_count


N, K = map(int, read().split())
plugs = read().split()
print(count_unplug(N, K, plugs))
