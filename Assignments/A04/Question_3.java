/******************************************************************************
 * Author:      Loic Konan 
 * Email:       loickonan.lk@gmail.com 
 * Label:       Question 3
 * Title:       Programing Assignment 01
 * Course:      CMPS 4143 
 * Semester:    Fall 2021
 * 
 * Description:
 *              This Project is about Find 5 high frequency words using
 *              several array operations.
 *
 * Files:   
 *              Question_3.java
 *   
 *****************************************************************************/

public class Question_3                                              // Start of our Java Program.
{                                                                    
    public static void main(String[] args)
    {                                                                // Start of our Driver Program.
        // Our given string 'S' below.
        String S = "Before trying to do any of the steps below, you should read the article "
                + "through at least once for basic understanding. Then go back and review, following these steps. "
                + "He ran his machine up to the stone porch and ascending the steps rang the door bell. They "
                + "directed their steps toward the sea, which was lit up by the rising moon. She breathed a sigh of "
                + "relief, and her light steps fell gradually into the measure of his. This was fully four feet under "
                + "water and the lower story of the place was two steps lower down.";

       
        System.out.println("\n");                                    // Adding few new line to make it loop nice.
        System.out.println(S);                                       // Displaying the given text on the console.

        String[] text = S.split("\\s");                              // This splits a given string around matches
                                                                     // of the given regular expression.

        String[] Frequenttext = new String[text.length];             // Create an array of string and make it the length of our given text.
        int[] frequency = new int[text.length];                      // Create an array of integers and make it the length of our given text.

        int Count = 0;                                               // Declare and initialize a variable call Count to keep count.

        for (int i = 0; i < text.length; i++)                        // Iterate through our for loop as long as i is less than our text length.
        {                                                            
            boolean valid = false;                                   // Created a boolean and set it to false.

            for (int j = 0; j < Count; j++)                          // Iterate through our for loop as long as i is less than the variable count.
            {         
                /**
                 * 
                 * 
                 *  
                 */
                if (text[i].replaceAll("[.,;]", "").equalsIgnoreCase(Frequenttext[j])) 
                {                                                    
                    frequency[j] += 1;                               //
                    valid = true;                                    //
                }                                                    //
            }                                                        

            if (!valid)                                             //
            {                                                       //
                Frequenttext[Count] = text[i].replaceAll("[.,;]", "");
                frequency[Count] = 1;
                Count += 1;
            }
        }                                                            // End of our for loop.

        for (int i = 0; i < Count; i++)                              //
        {                                                            // 
            for (int j = 0; j < Count - i - 1; j++)                  //
            {                                                        //
                if (frequency[j] < frequency[j + 1])                 //
                {
                    int temp = frequency[j];
                    frequency[j] = frequency[j + 1];
                    frequency[j + 1] = temp;
                    String temp_S = Frequenttext[j];
                    Frequenttext[j] = Frequenttext[j + 1];
                    Frequenttext[j + 1] = temp_S;
                }                                                    //
            }                                                        //
        }                                                            //

        System.out.println("The Top 5 Most Frequent words: ");
        for (int i = 0; i < 5; i++)                                  //
        {
            System.out.println(i + 1 + ". " + Frequenttext[i] + " (appeared " + frequency[i] + " times.)");
        }       
    }                                                                // End of our Driver program.
}                                                                    // End of our Java Program.
