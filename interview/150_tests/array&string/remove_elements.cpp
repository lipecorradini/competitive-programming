#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        stack<int> removed;
        // elements equal indices goes into stack
        for (int i = 0; i < nums.size(); i++){
            if(nums[i] == val) removed.push(i);
        }

        int last = nums.size() - 1;
        int diff_number = removed.size();
        int k = nums.size() - removed.size();
        // while the stack is not empty, change with last value
        while(removed.empty() == 0){
           int val_removed = removed.top();
           removed.pop();
           while(last >= 0 && nums[last] == val) last--;
           
           if (last < 0) break;
           if (val_removed < k) nums[val_removed] = nums[last --];
           
        }

        return k;
    }
};

// Optimal solution (waaay simpler)

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int index = 0;

        for(int i = 0; i< nums.size(); i++){
            if(nums[i] != val){
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }
};