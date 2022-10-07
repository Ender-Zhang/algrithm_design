package chapter5.chapter5.src;

/**
 * 给定n种物品和一背包。物品i的重量是wi，其价值为pi，背包的容量为C。 问应如何选择装入背包的物品，使得装入背包中物品的总价值最大?
 *
 * @author fulisha
 *
 */
public class Package01_huisu {

    static int BestValue = 0; // 最优值；当前的最大价值，初始化为0
    static int[] BestX; // 最优解；BestX[i]=1代表物品i放入背包，0代表不放入
    //
    static int CurWeight = 0; // 当前放入背包的物品总重量
    static int CurValue = 0; // 当前放入背包的物品总价值
    static int N = 3;// 物品数量
    static int C = 16;// 物品的总容量
    static int W[] = { 10, 8, 5 }; // 每个物品的重量
    static int v[] = { 5, 4, 1 };// 每个物品的价值
    static int x[] = { 0, 0, 0 };// x[i]=1代表物品i放入背包，0代表不放入

    public static int backtrack(int t) {
        // 如果是子节点 当前价值和最佳价值做判断 保存最佳价值
        if (t > N - 1) {
            if (CurValue > BestValue) {
                BestValue = CurValue;
                BestX = x.clone();
//                for (int i = 0; i < x.length; i++){
//                    System.out.println(x[i]);
//                    BestX[i] = x[i];
//                }
//                System.out.println("...............");
            }

            return BestValue;
        }
        // 如果不是子节点 对子节点进行遍历
        else {
            // 就两种情况 取或不取 用0/1表示
            for (int i = 0; i <= 1; i++) {
                x[t] = i;
                if (i == 0) {
                    // 如果是不取 就不需要进行判断 直接到下一个节点
                    backtrack(t + 1);
                } else
                // 放入背包就进行约束条件 判断放入背包的东西是否合法
                {
                    if (CurWeight + W[t] <= C) {
                        CurWeight += W[t];
                        CurValue += v[t];
                        // 当东西装进入背包后你可以进行对下个商品的判断了
                        backtrack(t + 1);
                        //能执行以下两个语句就说明你回溯到了上一个节点 所以你就需要恢复现场 把你刚刚拿的东西退出来 我们要冲上一个节点又要重新来遍历 如果不减你就会多加一遍
                        CurWeight -= W[t];
                        CurValue -= v[t];
                    }
                }
            }
        }
        return BestValue;
    }

    public static void main(String[] args) {
        backtrack(0);
        System.out.println(BestValue);
//        System.out.println(BestX.length);
        for (int i = 0; i < BestX.length; i++) {
             System.out.println(BestX[i]);
        }
    }

}
