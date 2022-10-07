package chapter5.chapter5.src;

public class package01 {
    private static int[] weights = {20,40,80,10};
    private static int[] values = {100,60,200,40};
    public static int dp(int a, int n, int[] weights, int[] values) {
        int[][] map = new int[a+1][n+1];
        for(int i = 1; i <= n; i++) {
            int value = values[i-1];
            int weight = weights[i-1];
            for(int j = 1; j <= a; j++) {
                if(j < weight) {
                    map[j][i] = map[j][i-1];
                    continue;
                }
                map[j][i] = Math.max(map[j][i-1],map[j-weight][i-1]+value);
            }
        }
        return map[a][n];
    }
    public static void main(String[] args){
        System.out.println(dp(100,4,weights,values));
    }
}
//运行结果为300，符合最佳解决方案。

