/*
                      ::::::
                    :+:  :+:
                   +:+   +:+
                  +#++:++#++:::::::
                 +#+     +#+     :+:
                #+#      #+#     +:+
               ###       ###+:++#""
                         +#+
                         #+#
                         ###

__author__ = "Alex Pujols"
__copyright__ = "TBD"
__credits__ = ["Alex Pujols"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Alex Pujols"
__email__ = "alex.pujols@gmail.com"
__status__ = "Prototype"


Title	      :	Procedural problems in Go
Date		    :	2-16-2021
Description :	Solves simple procedural problems in goLang
Options	    :	{TBD}
Notes	      :	{TBD}
*/

// Import packages
package main

import (
    "fmt"
    "strings"
)

// Simple "Hello World" output
func Howdy() {
  fmt.Println("\n************ Simple Hello World ***********")
  fmt.Println("\nHello World from Go!")
}
// Perform odd filter string manipulation
func filter (str []int) []int {
  fmt.Println("\n************ ODD FILTER FUNCTION ***********")
  var newString []int
  fmt.Println("The old string is: ", str)
  for index, element := range str {
    if str[index] % 2 != 0 {
        newString = append(newString, element)
      }
  }
  return newString
}
// Perform explode string manipulation
func explode(str string) []string {
  fmt.Println("\n************ EXPLODE FUNCTION ***********")
  fmt.Println("The old string is: ", str)
  newString := strings.Split(str, "")
  return newString
}
// Perform implode string manipulation
func implode(str string) string {
  fmt.Println("\n************ IMPLODE FUNCTION ***********")
  fmt.Println("The old string is: ", str)
  newString := strings.Replace(str, " ", "", -1)
  return newString
}


// Start main function
func main() {

  // Declare strings
  str1 := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
  str2 := "apple"
  //str3 := "a"
  str4 := "a p p l e"

  // Print Hello World
  Howdy()

  // Perform odd filter string manipulation
  newString1 := filter(str1)
  fmt.Println("The NEW filtered string is: ", newString1)

  // Perform explode string manipulation
  newString2 := explode(str2)
  fmt.Println("The NEW explode string is: ", newString2)

  // Perform implode string manipulation
  newString4 := implode(str4)
  fmt.Println("The NEW implode string is: ", newString4)
}
