package main

func main() {
	ch := make(chan int)
	go a(ch)

	go b(ch)
	// prevent the program from terminating, ignore for now
	select {
	case value := <-ch:
		println(value + 1)
	}
}

func a(ch chan int) {
	println("a before")
	ch <- 5
	println("a after")
}

func aa() {
	println("aa")
}

func ab() {
	println("ab")
}

func b(ch chan int) {
	println(<-ch)
	println("b before")
	println("b after")
}

func ba() {
	println("ba")
}

func bb() {
	println("bb")
}
