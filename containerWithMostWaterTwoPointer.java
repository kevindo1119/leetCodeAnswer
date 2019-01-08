class Solution 
{
    public int maxArea(int[] height) 
    {
        
        int num_container =  height.length;
        int first_select_container_index = 0;
        int second_select_container_index = num_container - 1;
        int final_result = Math.min(height[first_select_container_index], height[second_select_container_index]) * (second_select_container_index - first_select_container_index);
        int temp_result;
        
        while (first_select_container_index <= second_select_container_index) 
        {
            
            temp_result = Math.min(height[first_select_container_index], height[second_select_container_index]) * (second_select_container_index - first_select_container_index);
            
            if (temp_result > final_result)
            { // update results
                final_result = temp_result;
            }
            
            if (height[first_select_container_index] <= height[second_select_container_index])
            { // update index
                first_select_container_index ++;
            }
            else
            {
                second_select_container_index --;
            }
        }
        
        return final_result;
    }
}
