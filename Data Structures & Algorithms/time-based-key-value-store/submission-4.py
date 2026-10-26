class TimeMap:

    def __init__(self):
        self.keys = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = [[value,timestamp]]
        else:
            self.keys[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        keys = self.keys
        if key not in keys:
            return ""
        else:
            key = self.keys[key]
            if timestamp>=key[-1][1]:
                return key[-1][0]
            elif timestamp<key[0][1]:
                return ""
            else:
                bgn = 0
                end = len(key)-2
                while bgn<=end:
                    if bgn==end:
                        return key[bgn][0]
                    i = bgn+int((end-bgn)//2)
                    if key[i][1]==timestamp:
                        return key[i][0]
                    elif key[i][1]<timestamp and key[i+1][1]>timestamp:
                        return key[i][0]
                    elif key[i][1]<timestamp:
                        bgn = i+1
                    else:
                        end = i-1

                return key[i][0]

        
