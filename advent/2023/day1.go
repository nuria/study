package main

import  (
    "bufio"
    "fmt"
    "os"
    "slices"
    "strconv"
)

func check(e error){
    
    if e!=nil {
        panic(e)
     }
}

func readLines(path string) ([]string, error){
    file, err := os.Open(path)
    check(err)
    defer file.Close()
    var lines[] string
    scanner := bufio.NewScanner(file)
    for scanner.Scan(){
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}



func main() {
    fmt.Println("hello world")
    lines,err := readLines("./input1.txt")
    check(err)

    
    var tally int = 0
    digits := []string{"0", "1","2","3","4","5","6","7","8","9"} 
    
    


    for _, element:= range lines {
        var first string= ""
        var last string= ""

        for _,char:= range element {
            if slices.Contains(digits, string(char)) {
                if first == ""{
                   first= string(char)
                } else {
                   last= string(char)
                }
                fmt.Println(string(last))
            }
        
        }
        var n string = "0"
        
        if first!="" && last !="" {
            n = first+ last 
        } else if last =="" {
            n = first + first 
        }

        fmt.Println(string(n))
        n_int, err:= strconv.Atoi(n)
        check(err)

        tally = tally + n_int
    }

    fmt.Println(">>>")
    fmt.Println(tally)
}
