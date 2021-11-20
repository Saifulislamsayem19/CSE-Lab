package fourthSemester.krusKalsAlgo;
import java.util.Scanner;
class MainClass{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        pr("Enter Number of Vertices : ");
        int vertices = sc.nextInt();
        pr("Enter Number of Edges : ");
        int edges = sc.nextInt();
        Graph G = new Graph(vertices, edges);

        for(int i=0; i<edges; i++){

            pr("\nEnter Source : ");
            G.edge[i].src = sc.nextInt();
            pr("Enter Destination : ");
            G.edge[i].dest = sc.nextInt();
            pr("Enter Weight : ");
            G.edge[i].weight = sc.nextInt();
        }

        G.KruskalAlgo();
    }

    public static void pr(Object output){
        System.out.print(output);
    }

}
