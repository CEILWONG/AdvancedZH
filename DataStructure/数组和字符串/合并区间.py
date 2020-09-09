class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals

        outlist=[]
        outlist.append(intervals[0])
        del_nums=[]

        for a in range(1,len(intervals)):
            this_interval=intervals[a]


            for each_out in outlist:
                #each_out=outlist[i]
                if this_interval[0]>each_out[1] or this_interval[1]<each_out[0]:
                    pass
                else:
                    #outlist.pop(outlist.index(each_out))
                    del_nums.append(outlist.index(each_out))
                    left=this_interval[0] if this_interval[0]<each_out[0] else each_out[0]
                    right=this_interval[1] if this_interval[1]>each_out[1] else each_out[1]
                    this_interval[0]=left
                    this_interval[1]=right
            for i in del_nums[-1::-1]:
                outlist.pop(i)
            outlist.append(this_interval)
            del_nums=[]

        return outlist