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
Description :	Solves simple procedural problems in Swift
Options	    :	{TBD}
Notes	      :	{TBD}
*/

// Import libraries
import Swift
import Foundation

// Simple "Hello World" output
func Howdy() {
  print("\n************ Simple Hello World ***********")
  print("Hello World from Swift!")
}
// Perform odd filter string manipulation
func filter (array: [Int]) -> [Int] {
  var newArray = [Int] ()
  let size = array.count
  print("\n************ ODD FILTER FUNCTION ***********")
  print("The old array is: ", array)
  for value in 0..<size {
    if array[value] % 2 == 0 {
        newArray.append(value)
    }
  }
  return newArray
}
// Perform explode string manipulation
func explode(str: String) -> String {
  print("\n************ EXPLODE FUNCTION ***********")
  print("The old string is: ", str)
  let newString = str.lazy.map { "\($0)" }.joined(separator: " ")
  return newString
}
// Perform implode string manipulation
func implode(str: String) -> String {
  print("\n************ IMPLODE FUNCTION ***********")
  print("The old string is: ", str)
  let newString = String(str.filter { !" ".contains($0) })
  return newString
}
// Start main function

  // Declare strings
  let array1: [Int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  let str2 = "apple"
  //let str3 = "a"
  let str4 = "a p p l e"

  // print Hello World
  //Howdy()

  // Perform odd filter string manipulation
  let newArray1 = filter(array: array1)
  print("\nThe ODD explode string is: ", newArray1)
  // Perform explode string manipulation
  let newString2 = explode(str: str2)
  print("\nThe NEW explode string is: ", newString2)
  // Perform implode string manipulation
  let newString4 = implode(str: str4)
  print("\nThe NEW implode string is: ", newString4)
