class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((value, timestamp))
        # Key, Value, Timestamp
        # Multiple keys...

    def get(self, key: str, timestamp: int) -> str:
        best, best_timestamp = "", -1
        for value,time in self.mapping[key]:
            if time > best_timestamp and time <= timestamp:
                best_timestamp = time
                best = value
        return best 

        # Brute Force: Get The Key --> Returns List of All the (Values, TimeStamp)
        # Iterate Thru All the Values and TimeStamp until you get to Maximum Timestamp. Return that value. 
        # If there are no values, return "". 
        # Brute Force: {key: (value, timestamp)}
        # When you call key onto value/timestamp, it'll iterate through all of its elements...O(N) Time, O(N) Space



# Same key: multiple values (different time stamps) --> retrieve at cetain timestamp
