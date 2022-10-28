/*
 * @Author: Ender-Zhang 102596313+Ender-Zhang@users.noreply.github.com
 * @Date: 2022-10-26 11:45:48
 * @LastEditors: Ender-Zhang 102596313+Ender-Zhang@users.noreply.github.com
 * @LastEditTime: 2022-10-26 11:47:25
 * @FilePath: \algrithm_design-1\week8\quiz8.java
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
package quiz;

public class quiz8 
{
	static int MAX = 8;
	static int []col = new int[MAX+1];


	public static void main(String[] args)
	{
		int ret = 0, tot = 0;
		
		System.out.println("Each estimate of this algorithm is:");

		// find average of 20 estimates
		for(int i = 0; i < 20; i++) {
			ret = estimateNQueens(MAX);
			tot += ret;
			System.out.printf("\tseq[%d]: numnodes = %d\n", i, ret);
		}

		// print the average of 20 estimates
		System.out.println(" total is:" + tot);
		System.out.println(" avarage is:" + tot/20);
		
	}


	public static int estimateNQueens(int n) 
	{
		int i = 0, j, m = 1;
		int numnodes = 1, mprod = 1;
		int random;

		while(m != 0 && i != n) 
		{
			System.out.println("mprod is:"+ mprod);
			mprod = mprod * m;
			
			System.out.println("numnodes is:"+ numnodes);
			numnodes = numnodes + mprod * n;
			
			i++;
			m = 0;
			int[] prom_children = new int[MAX+1];
			
			for(j = 1; j <= n; j++) 
			{
				col[i] = j;
				if(promising(i)) 
				{
					m++;
					prom_children[j] = 1;
				}
			}
			if(m != 0) 
			{
				while(true) 
				{
					random = (int)( Math.random()*MAX) + 1;					
					if(prom_children[random] == 1) 
					{
						j = random;
						break;
					}
				}
				col[i] = j;
			}
		}
		return numnodes;
	}

	public static boolean promising(int i) 
	{
		int k = 1;
		boolean Switch = true;
		while(k < i && Switch) 
		{
			if(col[i] == col[k] || Math.abs(col[i] - col[k]) == i - k)
				Switch = false;
			k++;
		}
		return Switch;
	}

}


