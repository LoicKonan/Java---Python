
/******************************************************************************
 * Author:          Loic Konan 
 * Email:           loickonan.lk@gmail.com 
 * Label:           Question 3 
 * Title:           Programing Assignment 02 
 * Course:          CMPS 4143 
 * Semester:        Fall 2021 
 * Date:            10/10/2021
 * 
 * Description: 
 *                  Creating a calculator class to perform these operations:
 *                  Addition, Subtraction, Multiplication, Division, and Modulo. 
 *                  With these two exception handling classes: 
 *                  SyntaxError and RuntimeError.
 * 
 * Solution:
 *
 * 
 * 
 * Files:           Question_3.java
 * 
 *****************************************************************************/

 import javax.swing.*;
 import java.awt.event.*;
 import java.io.*;


class SyntaxError extends Exception 
{
    private String ErrorMessage;

    public SyntaxError(String ErrorMessage) 
    {
        this.ErrorMessage = ErrorMessage;
    }

    @Override
    public String getLocalizedMessage() 
    {
        return this.ErrorMessage;
    }
}


class RuntimeError extends Exception 
{
    private String ErrorMessage;

    public RuntimeError(String ErrorMessage) 
    {
        this.ErrorMessage = ErrorMessage;
    }

    @Override
    public String getLocalizedMessage() 
    {
        return this.ErrorMessage + "\n";
    }
}


public class Calculator
{
    public double Add(double a, double b)
    {
        return a + b;
    }
    
    public double Subtraction(double a, double b)
    {
        return a - b;
    }

    public double Multiplication(double a, double b)
    {
        return a * b;
    }

    public double Divide(double a, double b)
    {
        return a / b;
    }
    
    public double Modulo(double a, double b)
    {
        return a % b;
    }

    public static void main(String[] args)  throws SyntaxError, RuntimeError 
    {
        File file = new File("input.txt");
        Scanner scanner = new Scanner(file);

        while (scanner.hasNextLine())
        {
            for (int i : temp) System.out.println(temp.charAt(i));

            System.out.println((temp));
        }
    }
}