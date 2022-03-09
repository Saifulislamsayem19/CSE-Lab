package FourthSemester.ActivitySelectionProblem;

import java.util.ArrayList;
import java.util.Scanner;

public class MainClass {

    public static void main(String[] args) {
        ArrayList<ActivitySelection.Activity> activities = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int n, i, s, f;
        System.out.println("Enter no. of activities:");
        n = sc.nextInt();

        System.out.println("Enter Start and End time:");
        for (i = 1; i <= n; i++) {
            //System.out.println("Enter " + i + " activitiy");

            //System.out.println("Enter Start time:");
            s = sc.nextInt();
            //System.out.println("Enter Finish time:");
            f = sc.nextInt();

            activities.add(new ActivitySelection.Activity(s, f));
        }

        new ActivitySelection().maxActivities(activities);
    }
}
/*
5 9
1 2
3 4
0 6
5 7
8 9
*/
