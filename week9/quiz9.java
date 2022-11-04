package quiz.src;
// package quiz.src;

public class quiz9
{
	int V = 4;
	int[] path;

	boolean isSafe(int v, int[][] graph, int[] path, int pos)
	{
		if (graph[path[pos - 1]][v] == 0)
			return false;

		for (int i = 0; i < pos; i++)
			if (path[i] == v)
				return false;

		return true;
	}

	boolean hamCycleUtil(int[][] graph, int[] path, int pos)
	{
		if (pos == V)
		{
			if (graph[path[pos - 1]][path[0]] == 1)
				return true;
			else
				return false;
		}


		for (int v = 1; v < V; v++)
		{
			if (isSafe(v, graph, path, pos))
			{
				path[pos] = v;
				if (hamCycleUtil(graph, path, pos + 1) == true)
					return true;
				path[pos] = -1;
			}
		}

		return false;
	}

	
	int hamCycle(int graph[][])
	{
		path = new int[V];
		for (int i = 0; i < V; i++)
			path[i] = -1;
		path[0] = 0;
		if (hamCycleUtil(graph, path, 1) == false)
		{
			System.out.println("Can not form a cycle");
			System.out.println("Solution does not exist");
			return 0;
		}

		printSolution(path);
		return 1;
	}

	void printSolution(int path[])
	{
		System.out.println("The solution Exists a cycle and the cycle is:");
		for (int i = 0; i < V; i++)
			System.out.print(" " + path[i] + " ");
		System.out.println(" " + path[0] + " ");
	}

	public static void main(String args[])
	{
		quiz9 hamiltonian = new quiz9();


		int[][] graph1 = {
			{0, 1, 1, 1},
			{1, 0, 1, 1},
			{1, 1, 0, 1},
			{1, 1, 1, 0},

		};
		int[][] graph2 = {
			{1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0},
		    {1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0},
		    {0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0},
		    {0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0},
		    {1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0},
		    {0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0},
		    {0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0},
		    {0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		    {0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1},
		    {0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0},
		    {0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0},
		    {0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1},
		  };
		System.out.println("Test Case 1 (4 nodes): ");
		hamiltonian.hamCycle(graph1);

		System.out.println("Test Case 2(The graph in the textbook which is not exist): ");
		hamiltonian.hamCycle(graph2);
	}
}