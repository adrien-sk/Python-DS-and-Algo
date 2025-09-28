def HaveOverlapingIntervals(intervals):
    if len(intervals) < 2:
        return True

    intervals.sort(key=lambda interval:interval[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
        
    return True

def mergeIntervals(intervals):
    merged = []
    intervals.sort()

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
            
        merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged