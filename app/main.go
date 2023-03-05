package main

import (
	"fmt"

	"github.com/tidwall/pretty"
)

func main() {

	var js string = `{"name":  {"first":"Tom","last":"Anderson"},  "age":37,
	"children": ["Sara","Alex","Jack"],
	"fav.movie": "Deer Hunter", "friends": [
		{"first": "Janet", "last": "Murphy", "age": 44}
	  ]}`
	b := []byte(js)
	converted := string(pretty.Pretty(b))
	fmt.Println(converted)

}
