import java.util.ArrayList;
import java.util.Arrays;

/*
 * @Author: yuchen zhang yuchen.zhang1@ucdconnect.ie
 * @Date: 2022-10-04 16:56:06
 * @LastEditors: yuchen zhang yuchen.zhang1@ucdconnect.ie
 * @LastEditTime: 2022-10-04 19:14:10
 * @FilePath: \algrithm_design\project2\test.java
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
public class test {
    public static void main(String[] args) {
        // int t = (int) Integer.MIN_VALUE;
        // int l = 1;
        // System.out.println(t);
        // System.out.println(t + l);
        // System.out.println(t + t);
        // int max = (int)Integer.MAX_VALUE;
        // System.out.println(max + max);
        ArrayList<ArrayList<Integer>> ans1 = new ArrayList<ArrayList<Integer>>();
		ans1.add(new ArrayList<Integer>());
        ans1.get(0).add(-1);
        System.out.println(ans1);
        ArrayList<String>[][] arraylist1 = new ArrayList[3][3];
        arraylist1[0][0] = new ArrayList<String>();
      
        arraylist1[0][0].add("String One");
        arraylist1[0][0].add("String Two");
        arraylist1[0][0].add("String Three");
        System.out.println(Arrays.deepToString(arraylist1));


    }
}
