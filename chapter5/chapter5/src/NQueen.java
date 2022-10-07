package chapter5.chapter5.src;


/**
 * NQueen
 *
 * @author zgd
 * @date 2021/10/28 09:41
 */
public class NQueen {


    public static void main(String[] args) {
        int n = 4;
        int nqueen = nqueen(n, 0, new int[n], 0);
        System.out.println("nqueen = " + nqueen);
    }


    /**
     * @param n   表示n * n 的格子
     * @param row 当前是多少行
     * @param res 用一个数组,记录每一行的皇后所在的列
     * @param count 结果总数
     * @return
     */
    public static int nqueen(int n,int row,int[] res,int count){
        if (row == n){
            //打印
            print(n, res);
            count++;
            System.out.println("-----------");
            return count;
        }
        for (int col = 0; col < n; col++) {
            //先尝试着把皇后放在这一列
            res[row] = col;
            //判断和上面行的皇后是否冲突
            if (isOk(row,col,res)){
                //迭代,下一行
                count = nqueen(n,row+1,res,count);
            }
        }
        return count;
    }

    private static boolean isOk(int row, int col, int[] res) {
        for (int i = 0; i < row; i++) {
            //判断上面每行皇后所在列, 如果和当前列相同则为false
            if (res[i] == col){
                return false;
            }
            //判断撇和捺方向, 是两个斜率为1和-1的直线, 则他们两个坐标 |y2 - y1| == |x2 - x1|
            if (row - i == col - res[i] || row - i == res[i] - col ){
                return false;
            }
        }
        return true;
    }

    private static void print(int n, int[] res) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (res[i] == j){
                    System.out.print("Q");
                }else{
                    System.out.print("*");
                }
                System.out.print(" ");
            }
            System.out.println();
        }
    }

}

