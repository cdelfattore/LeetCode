import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class ThreeOneSixZero
{

    public static void main(String args[])
    {
        int limit = 4;
        int[][] queries = new int[][]{ {1, 4}, {2, 5}, {1, 3}, {3, 4} };
        // int[][] queries = new int[][]{{0,1},{1,2},{2,2},{3,4},{4,5}};
        // int[][] queries = new int[][]{{0,1},{1,4},{1,1},{1,4},{1,1}};

        // HashSet<Integer> colors = new HashSet<>();
        HashMap<Integer, Integer> colors = new HashMap<>();
        HashSet<Integer> tmp = new HashSet<>();
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++)
        {

            // balls[queries[i][0]] = queries[i][1];

            // HashSet<Integer> colors = new HashSet<>();
            // for (int j = 0; j < balls.length; j++)
            // {
            //     if (balls[j] > 0)
            //     {
            //         colors.add(balls[j]);
            //     }
                
            // }
            if (!tmp.contains(queries[i][1])){
                colors.put(queries[i][0], queries[i][1]);
                tmp.add(queries[i][1]);
            }
            else 
            {
                colors.remove(queries[i][0]);
                // tmp.remove(queries[i][1]);
            }
            
            System.out.println("colors " +colors);
            // HashSet<Integer> tmp = new HashSet<>();
            // for (Integer key : colors.keySet())
            // {
            //     tmp.add(colors.get(key));
            // }


            result[i] = tmp.size();
            System.out.println(tmp);
        }

        // System.out.println(ballsSet);
        // HashSet<Integer> colors = new HashSet<>();
        // int[] result = new int[queries.length];
        // for (int i = 0; i < balls.length; i++)
        // {
        //     colors.add(balls[i]);
        //     result[i] = colors.size();
        //     System.out.println(balls[i]);
        // }

        for (int i = 0; i < result.length; i++)
        {
            System.out.println(result[i]);
        }
    }

}