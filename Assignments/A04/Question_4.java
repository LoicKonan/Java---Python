/******************************************************************************
 * Author:      Loic Konan 
 * Email:       loickonan.lk@gmail.com 
 * Label:       Question 4
 * Title:       Programing Assignment 01
 * Course:      CMPS 4143 
 * Semester:    Fall 2021 
 * 
 * Description:
 *              This Program is about taking a string or a sentence(s) then 
 *              printing the words in a reverse order using an array.
 *
 * Files:   
 *              Question_4.java
 * 
 *****************************************************************************/

public class Question_4 
{
    // Driver program.
    public static void main(String[] args)
    {
        String s = "This is my first programming  assignment ";      // Original text.
        System.out.print("Original Text is :    " + s +"\n");        // Displaying the Original sentence.
        char []p = swap(s.toCharArray());                            // Calling our function Swap to reverse the text.
        System.out.print("Converted Text is:    ");                  // Displaying the converted text.
        System.out.print(p);                                         //
        System.out.print("\n\n");                                    // Adding some new lines.
    }                                                                // End of the Driver Program.

    /**
     * We will use this function to perform the reverse on our given string S.
     * We will pass in 3  parameters. One array of characters and two integer 
     * variable to indicate the start and end of our string.
     * 
     * @param str
     * @param Beginning
     * @param Ending
     * @return void
     */
    static void reverse(char [] str,int Beginning,int Ending) 
    {                                                                // Start of our function.
        char StringText;                                             // Declaring a variable call StringText.
        while (Beginning <= Ending)                                  // As long as the end is less or equal to the start.
        {                                                            // Start of our while loop.
            StringText = str[Beginning];                             // Initialize StringText to the begining of our text.
            str[Beginning] = str[Ending];                            // Then re-initialize it to the end of our text.
            str[Ending] = StringText;                                // Here we pretty much reversing the order of our text.
            Beginning++;                                             // Encrementing the Begining variable.
            Ending--;                                                // Decrementing the ending variable.
        }                                                            // End of the while loop.
    }                                                                // End of function reverse.

    /**
     * 
     * @param s
     * @return static char
     */
    static char[] swap(char []s)
    {
    int Beginning = 0;                                               //
    for (int Ending = 0; Ending < s.length; Ending++)                //
    {                                                                //
        if (s[Ending] == ' ')                                        //
        {
            reverse(s, Beginning, Ending);                           //
            Beginning = Ending + 1;                                  //
        }                                                            //
    }                                                                //
    reverse(s, Beginning, s.length - 1);                             //
    reverse(s, 0, s.length - 1);                                     //
    return s;                                                        //
    }                                                                // 
}
