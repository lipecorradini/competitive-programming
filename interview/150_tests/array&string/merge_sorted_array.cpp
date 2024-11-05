#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
        vector<int> tempArray;

        int m_count = 0;
        int n_count = 0;

        if(n == 0) tempArray = nums1;
        else{
            while (n_count + m_count < n + m) {
            
            if ((n_count == n || nums1[m_count] <= nums2[n_count]) && m_count < m){
                tempArray.push_back(nums1[m_count]);
                m_count++;
            }
            
            else{
                tempArray.push_back(nums2[n_count]);
                n_count++;
                }
            }
        }

        
        for (int i = 0; i < n + m; i++){
            nums1[i] = tempArray[i];
        }

        
    }
};

// Optimal Solution (also does it in place)

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int midx = m - 1;
        int nidx = n - 1;
        int right = m + n - 1;

        while (nidx >= 0) {
            if (midx >= 0 && nums1[midx] > nums2[nidx]) {
                nums1[right] = nums1[midx];
                midx--;
            } else {
                nums1[right] = nums2[nidx];
                nidx--;
            }
            right--;
        }        
    }
};