using System;
using System.Collections.Generic;

public class Point
{
        public double x;
        public double y;

        public Point(double x, double y)
        {
            this.x = x;
            this.y = y;

        }

    public static void displayPoint(Point p)
    {
        Console.WriteLine("(" + p.x + ", " + p.y + ")");
    }
}

public class Test
{
    static void lineFromPoints(Point A, Point B)
    {
        double a = B.y - A.y;
        double b = A.x - B.x;
        double c = a*A.x + b * A.y;

        if (b<0)
        {
            Console.WriteLine(a+ "x -" + b + "y = "+c);
        }
        else
        {
            Console.WriteLine(a+ "x +" + b + "y = "+c);
        }
    }

    public static void Main(String[] args)
    {
        Point A = new Point(3,2);
        Point B = new Point(2,6);
        lineFromPoints(A,B);
    }

}