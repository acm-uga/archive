class Solution 
{
    public int stockProfit(int[] prices) 
    {
        //Create min value 
        //(an Integer value that is set to 2^31 -1)
        int rangeMin = Integer.MAX_VALUE;
        
        //Create profit value
        int profit = 0;
        
        //Iterate thur array
        for (int i = 0 ; i < prices.length; i++)
        {
            
            //Calculate profit for our range window
            if (prices[i] - rangeMin > profit)
                profit = prices[i] - rangeMin;
            
            //Encountered new min value so window so min value in range shifts forward
            if (prices[i] < rangeMin)
                rangeMin = prices[i];

        }
        
        return profit;
    }
}
