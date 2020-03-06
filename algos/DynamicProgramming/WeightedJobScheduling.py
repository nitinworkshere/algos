class Job:
    def __init__(self, start_time, finish_time, profit):
        self.start_time = start_time
        self.finish_time = finish_time
        self.profit = profit

def weighted_job_scheduling(jobs):
    jobs.sort(key=lambda job: job.start_time)
    dp = [0 for _ in range[len(jobs)+1]]
    dp[0] = jobs[0].profit

    for i in range(1, len(jobs)+1):
        dp[i] = max(jobs[i].profit, jobs[i-1])
        for j in range(1, i-1):
            if(dp[j].finish_time <= dp[i].start_time):
                dp[i] = max(dp[i], jobs[i].profit+dp[j])


    #search for max val in array to find max profit

