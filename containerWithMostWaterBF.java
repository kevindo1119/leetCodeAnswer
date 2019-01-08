class Solution 
{
    public int maxArea(int[] height) 
    {
        
        int num_container =  height.length;
        int first_select_container = height[0];
        int second_select_container = height[1];
        int final_result = Math.min(first_select_container, second_select_container) * (1-0);
        int temp_result;
        
        for (int i = 0; i < num_container; i++) 
        {
            for (int j = i + 1 ; j < num_container; j++) 
            {
                temp_result = Math.min(height[j], height[i]) * (j-i);
                if (temp_result > final_result)
                {
                    final_result = temp_result;
                }
            }
        }
        
        return final_result;
    }
}
