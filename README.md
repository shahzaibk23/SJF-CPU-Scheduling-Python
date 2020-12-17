## SJF (Shortest Job First) CPU Scheduling Algorithm in Python

In order to run this script.
<br /><br />
First write down the processes in the script, in such a way:
```python

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

```
<hr />
Once you're done defining your processes, run the script.
#### To run Non-Preemtive
```ruby
python NonPreem.py
```
Or In Linux:

```ruby
python3 NonPreem.py
```