import java.util.ArrayList;

/*
 * @Author: yuchen zhang yuchen.zhang1@ucdconnect.ie
 * @Date: 2022-10-04 16:17:48
 * @LastEditors: yuchen zhang yuchen.zhang1@ucdconnect.ie
 * @LastEditTime: 2022-10-04 19:49:06
 * @FilePath: \algrithm_design\project2\problem1.java
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
// '''
// Author: yuchen zhang yuchen.zhang1@ucdconnect.ie
// Date: 2022-10-04 16:17:48
// LastEditors: yuchen zhang yuchen.zhang1@ucdconnect.ie
// LastEditTime: 2022-10-04 16:18:07
// FilePath: \algrithm_design\project2\problem1.py
// Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
// '''
class Solution {
    public int[][] getMaxMatrix(int[][] matrix0) {
		int[][] matrix = changeMatrix(matrix0);
		// for (int i = 0; i < matrix.length; i++){
		// 	for (int j = 0; j < matrix.length; j++){
		// 		System.out.print(matrix[i][j]);
		// 	}	
		// 	System.out.println("");
		// }


        int max=Integer.MIN_VALUE;
		// System.out.println(max);
        int dp=0,start=0;
        int[][] ans = new int[][] {{-1},{-1},{200},{200}};
		ArrayList<ArrayList<Integer>> ans1 = new ArrayList<ArrayList<Integer>>();
		ans1.add(new ArrayList<Integer>());
		ans1.add(new ArrayList<Integer>());
		ans1.add(new ArrayList<Integer>());
		ans1.add(new ArrayList<Integer>());
        ans1.get(0).add(-1);
		ans1.get(1).add(-1);
		ans1.get(2).add(200);
		ans1.get(3).add(200);
        //结果
        int[] sum=null;//纵向累加数组
		int situation = 0;
        for(int i=0;i<matrix.length;i++) {
        	sum=new int[matrix[0].length];
        	for(int j=i;j<matrix.length;j++) {
        		dp=0;start=0;
        		for(int k=0;k<sum.length;k++) {
        			// if (sum[k] == Integer.MIN_VALUE) {

					// }
					sum[k]+=matrix[j][k];
					dp+=sum[k];
        			if(max<dp) {
						situation = 0;
        				ans[0] = new int[] {i};
						ans[1] = new int[] {start};
        				ans[2] = new int[] {j};
						ans[3] = new int[] {k};
						ArrayList<Integer> al = new ArrayList<Integer>();
						al.add(i);
						ans1.set(0,al);
						
        				max = dp;
        			}
					if( max == dp) {
						ans[0][situation + 1] = i;
						ans[1][situation + 1] = start;
        				ans[2][situation + 1] = j;
						ans[3][situation + 1] = k;
						situation += 1;
					}
        			if(dp<0) {
        				dp=0;start=k+1;
        			}
        		}
        	}
        }
        return ans;
    }
	
	public int[][] changeMatrix(int[][] matrix){
		for (int i = 0; i < matrix.length; i++){
			for (int j = 0; j < matrix.length; j++){
				if (matrix[i][j] == 0) {
					matrix[i][j] = -1000;
					// matrix[i][j] = Integer.MIN_VALUE;
					// matrix[i][j] = (int) Double.NEGATIVE_INFINITY;
				}
			}
		}
		return matrix;
	}
	public static void main(String[] args) {
		Solution s = new Solution();
		int[][] testCase1 = {{1,0,1,0,0},
							{1,0,1,1,1},
							{1,1,1,1,0},
							{1,1,0,1,0}};
		int[][] t = s.getMaxMatrix(testCase1);
		for (int i = 0; i < 2; i++){
			int size = Integer.min(t[i][2] - t[i][0], t[i][3] - t[i][1]);
			int[] slice = {t[i][2], t[i][3]};
			System.out.print(size);
			System.out.print(" + ");
			System.out.println(slice);
		}
		
		// for (int i = 0; i < t.length; i++){
		// 	System.out.print(t[i]);
			
		// }

	}
}