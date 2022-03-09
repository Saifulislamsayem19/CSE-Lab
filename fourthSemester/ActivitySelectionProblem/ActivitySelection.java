package FourthSemester.ActivitySelectionProblem;

import java.util.ArrayList;
import java.util.Collections;

public class ActivitySelection {

    static class Activity {
        int start;
        int end;

        public Activity(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public String toString(){
            return "[" + this.start + ", " + this.end + "]";
        }
    }

    public static void maxActivities(ArrayList<Activity> activities){

        System.out.println("Given Activities: " + activities);
        Collections.sort(activities, (o1, o2) -> o1.end - o2.end);

        ArrayList<Activity> selectedActivities = new ArrayList<>();
        int currentEnd = -1;
        for (int i = 0; i <activities.size() ; i++) {
            Activity currentActivity = activities.get(i);
            if(currentActivity.start >currentEnd){
                selectedActivities.add(currentActivity);
                currentEnd = currentActivity.end;
            }
        }

        System.out.println("Selected Activities: " + selectedActivities);
    }

}
