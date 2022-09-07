# Write your processes here, in this dictionary format.
jobQueue = [
    {
        "Process":"P1",
        "BurstTime": 2,
        "ArrivalTime":0
    },
    {
        "Process":"P2",
        "BurstTime": 5,
        "ArrivalTime":3
    },
    {
        "Process":"P3",
        "BurstTime": 5,
        "ArrivalTime":2
    },

]

print("Job Queue initially")
for i in jobQueue:
    print(i)

readyQueue = []
waitingQueue = []

CPU_process_record = []

time = min([process["ArrivalTime"] for process in jobQueue ])

while jobQueue != []: #or readyQueue != [] or waitingQueue != []:
    # lstOfDeletion = []
    for j, i in enumerate(jobQueue):

        if i["ArrivalTime"] <= time:

            readyQueue.append(i)
            #lstOfDeletion.append(i)
            jobQueue.remove(i)

    # for i in lstOfDeletion:
    #     jobQueue.remove(i)

    # lstOfDeletion = []

    # listOfBurstTimes =[process["BurstTime"] for process in readyQueue]
    sortedListOfBurstTimes = sorted([process["BurstTime"] for process in readyQueue])
    # sortedListOfBurstTimes = sorted(listOfBurstTimes)

    sortedReadyQueue = [process for burst in sortedListOfBurstTimes for process in readyQueue if process["BurstTime"] == burst]

    # sortedReadyQueue = []

    for process in sortedReadyQueue:
        readyQueue.remove(process)


    for j in sortedReadyQueue:
        # lstOfDeletion.append(j)
        sortedReadyQueue.remove(j)
        startTime = time
        time += j["BurstTime"]
        CPU_process_record.append({"Process":j["Process"], "StartTime":startTime, "EndTime":time})
    # for j in lstOfDeletion:
    #     sortedReadyQueue.remove(j)

print("\n \nShortest Job First ")
SumOfStartTime = 0
for i in CPU_process_record:
    print(i)
    SumOfStartTime += i["StartTime"]

AvgTime = SumOfStartTime/len(CPU_process_record)
print("Average Time: ",AvgTime," Units")




# lst = [process["BurstTime"] for process in jobQueue]
# ls = sorted(lst)
# a = [process for burst in ls for process in jobQueue if process["BurstTime"]==burst]
# # jobQueue[jobQueue.index()]
# print(a)
