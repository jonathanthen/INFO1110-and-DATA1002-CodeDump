public class ArrayMerge{
	public static int[][] mergeArrays(int[][] arrayA, int[][] arrayB){
		int lengthA = arrayA[0].length;
		int lengthB = arrayB[0].length;
		int lengthAB = lengthA + lengthB;
		int rows = arrayA.length;
		int[][] c = new int[rows][lengthAB];
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < lengthAB; j++) {
				if (j < lengthA) {
					c[i][j] = arrayA[i][j];
				} else {
					c[i][j] = arrayB[i][j-lengthA];
				}
			}
		}
		return c;
	}
	
	public static void main(String[] args) {
		int[][] a = new int[3][4]; /*{
			{1, 2, 3, 3},
			{3, 2, 1, 6},
			{4, 5, 6, 1}
		};*/
		int[][] b = new int[3][5]; /*{
			{1, 9, 7, 2, 3},
			{0, 7, 8, 3, 2},
			{3, 8, 9, 7, 2}
		};*/
		
		int[][] twod = mergeArrays(a, b);
		for(int x = 0; x < twod.length; x++) {
			for(int y = 0; y < twod[0].length; y++) {
				System.out.print(twod[x][y] + " ");
			}
			System.out.println();
		}
	}
}