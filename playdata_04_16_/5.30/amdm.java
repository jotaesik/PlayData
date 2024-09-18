package basic;
import java.util.Scanner;
public class test_02 {
    public static void menu(){
        System.out.println("메뉴선택");
        System.out.println("1.더하기");
        System.out.println("2.빼기");
        System.out.println("3.곱하기");
        System.out.println("4.나누기");
        System.out.println("0.끝내기");
    }
    public static int[] inputData(){
        Scanner sc = new Scanner(System.in);
        System.out.print("첫 번째 숫자:");
        int first = sc.nextInt();
        System.out.print("두 번째 숫자:");
        int second = sc.nextInt();
        // System.out.printf("%d %d",first,second);
        int []input_list = new int[2];
        input_list[0] = first;
        input_list[1] = second;
        return input_list;
    }
    public static void add(int a, int b){
        System.out.printf("%d + %d = %d\n\n",a,b,a+b);
        return;
    }
    public static void sub(int a, int b){
        System.out.printf("%d - %d = %d\n\n",a,b,a-b);
        return;
    }
    public static void mul(int a, int b){
        System.out.printf("%d * %d = %d\n\n",a,b,a*b);
        return;
    }
    public static void div(int a, int b){
        System.out.printf("%d / %d = %d\n",a,b,a/b);
        System.out.printf("%d %% %d = %d\n\n",a,b,a%b);
        return;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            menu();
            int input = sc.nextInt();
            // System.out.printf("%d\n",input);
            if (input==0){
                System.out.println("계산기를 종료합니다");
                break;
            }
            int [] list;
                switch(input){
                    case 1:
                        // System.out.println("1번"); 
                        // add(input, input)
                        list = inputData();
                        add(list[0],list[1]);
                        break;
                    case 2:
                        // System.out.println("2번"); 
                        list = inputData();
                        sub(list[0],list[1]);
                        break;
                    case 3:
                        // System.out.println("3번"); 
                        list = inputData();
                        mul(list[0],list[1]);
                        break;
                    case 4:
                        // System.out.println("4번"); 
                        list = inputData();
                        div(list[0],list[1]);
                        break;

                    default:
                        System.out.println("잘못된 메뉴를 선택하셨습니다");     
                }
        
        }
    
    }
}
