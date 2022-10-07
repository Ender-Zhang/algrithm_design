/*
 * @Author: Ender-Zhang 2245430790@qq.com
 * @Date: 2022-10-03 00:07:49
 * @LastEditors: Ender-Zhang 2245430790@qq.com
 * @LastEditTime: 2022-10-03 00:22:48
 * @FilePath: \algrithm_design\chapter5\hamiltonian.java
 * @Description: ����Ĭ������,������`customMade`, ��koroFileHeader�鿴���� ��������: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
package chapter5.chapter5.src;

import java.io.*;
import java.util.Arrays;
 
public class hamiltonian {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] split = br.readLine().split(" ");
		
		int n = Integer.parseInt(split[0]);
		int m = Integer.parseInt(split[1]);
		
		boolean [][]g = new boolean[n + 1][n + 1];
		boolean []vis = new boolean[n + 1];
		
		while(m-- > 0) {
			split = br.readLine().split(" ");
			int a = Integer.parseInt(split[0]);
			int b = Integer.parseInt(split[1]);
			g[a][b] = g[b][a] = true;
		}
		
		m = Integer.parseInt(br.readLine());
		StringBuilder ans = new StringBuilder();
		while(m-- > 0) {
			Arrays.fill(vis, false);
			split = br.readLine().split(" ");
			int []arr = new int[split.length]; 
			for(int i = 1; i < arr.length; i++) 
				arr[i] = Integer.parseInt(split[i]);
			
			int i = 0, cnt = n; // �ж��Ƿ������������n����
			for(i = 1; i < arr.length - 1; i++) {
				if(g[arr[i]][arr[i + 1]] && !vis[arr[i + 1]]) { // ͼ����·������û�б����ʹ�
					vis[arr[i + 1]] = true;
					cnt--;
				}else break;
			}
			if(i == arr.length - 1 && cnt == 0) ans.append("YES\n");
			else ans.append("NO\n");
		}
		System.out.print(ans);
	}
}