class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        result=[0]*n
        for log in logs:
            fid,action,time=log.split(":")
            fid,time=int(fid),int(time)
            if action=="start":
                if stack:
                    prev_id,prev_start=stack[-1]
                    result[prev_id]+=time-prev_start
                stack.append([fid,time])
            else:
                if not stack:continue
                top_id,top_start=stack.pop()
                result[top_id]+=time-top_start+1    
                if stack:
                    stack[-1][1]=time+1
        return result