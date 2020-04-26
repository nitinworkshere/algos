
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def merge_interval(intervals):
    intervals.sort(key=lambda x: x.start)

    merged = []
    start = intervals[0].start
    end = intervals[0].end

    for interval in intervals[1:]:
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged.append(Interval(start, end))

    return merged

intervals = [[1,4], [2,5], [7,9]]
converted_intervals = []
for interval in intervals:
    converted_intervals.append(Interval(interval[0], interval[1]))




