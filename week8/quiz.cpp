

#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

const int testCount = 20; // 测试次数
const int MAXN = 40;       // 能测试的皇后最大值
int countPerRow[MAXN];     // 存放每行能选列的个数，便于最终计算结果
int bucket[MAXN];          // 符合约束能选则为1，不符合约束不能选则为0
int x[MAXN];               // 存放生成的随机序列
int N;                     // 本次是N皇后求解

// 初始化临时标记是否是可选的列
// 每行的判定开始前，都需要调用，假定该行的每一列都不能选
void initBucket(){
    for(int i = 0; i < MAXN; ++i) {
        bucket[i] = 0;
    }
}

// 初始化每行能选的列数，每次试验开始前调用，进行置零
void initCountPerRow(){    
    for(int i = 0; i < MAXN; ++i) {
        countPerRow[i] = 0;
    }
}


bool CanPlace(int k) {   // 判断第k行第x[k]列能不能放
    for (int i = 0; i < k; ++i) {
        if (x[i] == x[k] || abs(i - k) == abs(x[i] - x[k]))   // 是否下面和斜对角有重合
            return false;
    }
    return true;
}

// 返回能够抵达的行数
int RecurBacktrackM(int t) {
    initBucket();
    if (t == N) {            // 如果已经进入第N+1行，则找到解
        return t;

    } else {
        int colCount = 0;    // 能摆放几列
        int randInt, r = 0;  // 随机第几个能摆放的位置
        int index = 0;       // 摆放的位置的下标
        for (int i = 0; i < N; ++i) {      // 挨个试探
            x[t] = i;
            if (CanPlace(t)) {             // 判断是否能放
                bucket[i] = 1;
                colCount++;
                countPerRow[t]++;          // 第t行实际产生的可行解数量++
            }
        }

        if(colCount > 0) {                 // 如果这一行有可行解
            randInt = rand()%colCount + 1;
            while(r < randInt){
                if(bucket[index] == 1){
                    r++;
                }
                index++;
            }
            index--;
            x[t] = index;                 // 得到随机选择的可行解的列号
            return RecurBacktrackM(t + 1);// 进入下一层
        } else {                          // 不能放说明是死胡同，直接返回
            return t;
        }
    }
}

int main() {
    srand((unsigned)time(NULL));
    // cout<<"Please enter the size of the board";
    N = 8;

    double allRate = 0;
    for(int number = 0; number < testCount; number++){
        int row, allNodeCount = 1;
        int geneNodeCount = 1;   // 蒙特卡洛估计的，实际产生的节点的数量
        initCountPerRow();
        row = RecurBacktrackM(0);

        cout<<"The random sedquence of this experient: ";
        for(int i = 0; i < row; i++){
            cout<<x[i]<<" ";
        }
        cout<<endl;

        int tmp;

        cout<<"The node of line is: ";
        for(int i = 0; i < row; i++){
            cout<<countPerRow[i]<<" ";
        }
        cout<<endl;
        for(int i = 0; i < row; i++) {
            tmp = 1;
            for(int j = 0; j <= i; j++) {
                tmp *= countPerRow[j];
            }
            geneNodeCount += tmp;
        }
        cout<<"The estimate node is: "<<geneNodeCount<<endl;
        
        for(int i = 0; i < N; i++) {
            tmp = 1;
            for(int j = 0; j <= i; j++) {
                tmp *= N-j;
            }
            allNodeCount += tmp;
        }
        cout<<"The total node number in the space tree: "<<allNodeCount<<endl;
        // cout<<"The ratio of real node number of total number:"<<((geneNodeCount * 1.0)/allNodeCount)*100<<"%"<<endl;
        allRate += (geneNodeCount * 1.0)/allNodeCount;
        cout<<"-----------------------------------------------"<<endl;
    }
    
    cout<<"Totoal "<<testCount<<" experients The ratio of actural node number of total node number: "<<(allRate/testCount)*100<<"%"<<endl;

    return 0;
}
