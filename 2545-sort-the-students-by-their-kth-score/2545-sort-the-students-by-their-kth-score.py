class Solution:
    def sortTheStudents(self, score, k):
        index_dict = {}
        for index,item in enumerate(score):
            index_dict[item[k]] = index                    
        sort_key = sorted(index_dict.keys(),reverse=True)   
        output = []
        for key in sort_key:
            output.append(score[index_dict[key]])          
        return output
    
    
#using enumerate example